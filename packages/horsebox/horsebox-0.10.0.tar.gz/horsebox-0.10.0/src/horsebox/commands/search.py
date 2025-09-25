import json
import re
from collections import OrderedDict
from itertools import chain
from shlex import quote
from time import monotonic_ns
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Set,
    Tuple,
)

import tantivy

from horsebox.cli import (
    ELLIPSIS,
    OPTION_COLLECT_AS_JSONL,
)
from horsebox.cli.config import config
from horsebox.cli.render import (
    Format,
    render,
    render_error,
)
from horsebox.collectors import CollectorType
from horsebox.collectors.factory import get_collector
from horsebox.collectors.pattern import explode_pattern
from horsebox.formatters.text import (
    LINE_BREAK,
    snippet_add_style,
)
from horsebox.indexer.analyzer import CustomAnalyzerDef
from horsebox.indexer.analyzer.factory import load_custom_analyzer_def
from horsebox.indexer.build_args import IndexBuildArgs
from horsebox.indexer.index import (
    feed_index,
    open_index,
)
from horsebox.indexer.schema import (
    DEFAULT_FIELD_NAMES,
    SCHEMA_FIELD_CONTENT,
    SCHEMA_FIELD_CONTENT_CUSTOM,
    SCHEMA_FIELDS_CUSTOM,
    get_schema,
)
from horsebox.model import TOutput
from horsebox.utils.stopword import (
    STOP_WORDS_COUNT,
    is_stopword,
)

# Syntax: word~, word~1, word~2
# Ignored: "word1 word2"~ (proximity search)
# Inspired by https://lucene.apache.org/core/2_9_4/queryparsersyntax.html#Fuzzy%20Searches
__RE_IS_FUZZY = re.compile(r"^(?P<word>[^\"']+)~((?P<distance>\d))?$")
__LEVENSHTEIN_DISTANCE_DEFAULT = 1
__LEVENSHTEIN_DISTANCE_MAX = 2

__EMPTY_QUERY = 'Query(EmptyQuery)'
__FIELD_HIGHLIGHT = 'highlight'
__FIELD_EXPLAIN = 'explain'


def search(
    source: Optional[List[str]],
    pattern: List[str],
    index: Optional[str],
    collector_type: CollectorType,
    collect_as_jsonl: bool,
    query_string: str,
    limit: int,
    highlight: bool,
    count: bool,
    top: bool,
    fields: List[str],
    sort_field: Optional[str],
    explain: bool,
    analyzer: Optional[str],
    format: Format,
) -> None:
    """
    Search an index.

    Args:
        source (Optional[List[str]]): The datasources to search from.
        pattern (List[str]): The pattern to identify the containers to index.
        index (Optional[str]): Location of the index to build/search.
        collector_type (CollectorType): The collector to use for indexing.
        collect_as_jsonl (bool): Whether the JSON documents should be collected as JSON Lines or not.
        query_string (str): The search query.
            See https://docs.rs/tantivy/latest/tantivy/query/struct.QueryParser.html.
        limit (int): the number of search results to return.
        highlight (bool): Whether the keywords found should be highlighted or not.
        count (bool): Whether a count operation should be done or not.
        top (bool): Whether the top list of keywords found should be returned or not.
        fields (List[str]): The list of fields to output.
        sort_field (Optional[str]): The field to sort by the result.
        explain (bool): Whether some explanation on why the document was found should be given or not.
        analyzer (Optional[str]): The file containing the definition of the custom analyzer.
        format (Format): The rendering format to use.
    """
    # region Open index

    t_index: Optional[tantivy.Index]
    took_index: Optional[int] = None
    build_args: Optional[IndexBuildArgs] = None

    if source and pattern:
        # Live search
        source, pattern = explode_pattern(source, pattern)
        collector, extra_args = get_collector(
            collector_type,
            source,
            pattern,
        )

        custom_analyzer: Optional[CustomAnalyzerDef] = load_custom_analyzer_def(analyzer) if analyzer else None

        t_index, took_index = feed_index(
            collector.create_instance(
                root_path=source,
                pattern=pattern,
                **({OPTION_COLLECT_AS_JSONL: collect_as_jsonl} | extra_args),
            ),
            # If an index is provided, the index will be (re) built
            index,
            build_args := IndexBuildArgs(
                source=source,
                pattern=pattern,
                collector_type=collector_type,
                collect_as_jsonl=collect_as_jsonl,
                custom_analyzer=custom_analyzer,
            ),
            format,
        )
    elif index:
        # Search on an existing index
        t_index, _, build_args = open_index(index, format)
        if not t_index:
            return
    else:
        raise ValueError('`--from` or `--index` must be specified')

    use_custom_field: bool = bool(build_args and build_args.custom_analyzer)

    # endregion
    # region Prepare query

    t_query: tantivy.Query = __parse_query_string(
        t_index,
        query_string,
        use_custom_field,
    )

    # endregion
    # region Search

    searcher: tantivy.Searcher = t_index.searcher()

    if top:
        __top_keywords_impl(
            searcher,
            t_query,
            limit,
            format,
            took_index,
        )
    else:
        __search_impl(
            t_index,
            use_custom_field,
            searcher,
            t_query,
            limit,
            highlight,
            count,
            fields,
            sort_field,
            explain,
            format,
            took_index,
        )

    # endregion


def __parse_query_string(
    t_index: tantivy.Index,
    query_string: str,
    use_custom_field: bool,
) -> tantivy.Query:
    t_query: tantivy.Query

    try:
        if match := __RE_IS_FUZZY.match(query_string.strip()):
            # Basic implementation of the fuzzy search through a query string.
            # `FuzzyTermQuery` is not accessible from the query parser:
            # https://github.com/quickwit-oss/tantivy/issues/1112#issuecomment-880331994
            # Attention! Highlight will not work (see https://github.com/quickwit-oss/tantivy/issues/2576)

            content_field = SCHEMA_FIELD_CONTENT_CUSTOM if use_custom_field else SCHEMA_FIELD_CONTENT

            distance = min(int(match['distance'] or __LEVENSHTEIN_DISTANCE_DEFAULT), __LEVENSHTEIN_DISTANCE_MAX)
            if (text := match['word']).startswith(f'{SCHEMA_FIELD_CONTENT}:'):
                # The field must not be specified in the query string
                text = text[len(f'{content_field}:') :]

            t_query = tantivy.Query.fuzzy_term_query(
                get_schema(custom_fields=SCHEMA_FIELDS_CUSTOM if use_custom_field else None),
                content_field,
                text.strip(),
                distance,
            )
        else:
            # https://docs.rs/tantivy/latest/tantivy/query/struct.QueryParser.html
            # Sample search: https://github.com/quickwit-oss/tantivy-py/blob/master/tests/tantivy_test.py
            t_query = t_index.parse_query(
                query_string,
                default_field_names=DEFAULT_FIELD_NAMES + ([SCHEMA_FIELD_CONTENT_CUSTOM] if use_custom_field else []),
            )

            if str(t_query) == __EMPTY_QUERY:
                render_error(f'Empty query: {query_string}')
    except ValueError as e:
        render_error(f'Query parse error: {e}')

    return t_query


def __search_impl(
    t_index: tantivy.Index,
    use_custom_field: bool,
    searcher: tantivy.Searcher,
    query: tantivy.Query,
    limit: int,
    highlight: bool,
    count: bool,
    fields: List[str],
    sort_field: Optional[str],
    explain: bool,
    format: Format,
    took_index: Optional[int] = None,
) -> None:
    # region Search

    order_by_field, order = __get_order_by_field(sort_field)

    start = monotonic_ns()
    result: tantivy.SearchResult = searcher.search(
        query,
        limit=1 if count else max(limit, 1),
        order_by_field=order_by_field,
        order=order,
    )
    took = monotonic_ns() - start

    # endregion
    # region Process result

    if count:
        render(
            {
                'took': {
                    'index': took_index,
                    'search': took,
                },
                'count': result.count,
            },
            format,
        )
    else:
        # Unique list of source fields (can be passed by multiple options or as a comma-separated list)
        source_filtering: Set[str] = {f.strip() for f in chain.from_iterable((f.split(',') for f in fields))}

        snippet_generator: Optional[tantivy.SnippetGenerator] = None
        if highlight:
            # https://docs.rs/tantivy/latest/tantivy/snippet/struct.SnippetGenerator.html
            # https://tantivy-search.github.io/examples/snippet.html
            snippet_generator = tantivy.SnippetGenerator.create(
                searcher,
                query,
                t_index.schema,
                SCHEMA_FIELD_CONTENT_CUSTOM if use_custom_field else SCHEMA_FIELD_CONTENT,
            )
            snippet_generator.set_max_num_chars(config.highlight_max_chars)

        outputs: List[TOutput] = []
        for score, doc_address in result.hits:
            hit = searcher.doc(doc_address)
            doc = hit.to_dict()

            # region Prepare document for output

            if contents := doc.get(SCHEMA_FIELD_CONTENT):
                if config.render_max_content is None:
                    content = contents[0]
                else:
                    content = contents[0][: config.render_max_content] + ELLIPSIS
            else:
                content = None

            path: Optional[str] = v[0] if (v := doc.get('path')) else None
            if path and format == Format.TXT:
                # Make the path link clickable
                path = quote(path)

            output = OrderedDict(
                name=doc['name'][0],
                content=content,
                path=path,
                size=v[0] if (v := doc.get('size')) else None,
                date=v[0] if (v := doc.get('date')) else None,
                score=score,
            )
            if snippet_generator:
                snippet: tantivy.Snippet = snippet_generator.snippet_from_doc(hit)

                highlight_output = (
                    snippet_add_style(snippet) if format == Format.TXT else __build_output_from_snippet(snippet)
                )
                if highlight_output:
                    # Highlights will be generated for search based on text fields.
                    output[__FIELD_HIGHLIGHT] = highlight_output

            if source_filtering:
                if SCHEMA_FIELD_CONTENT in source_filtering and __FIELD_HIGHLIGHT in output:
                    # Use the highlighted content if any in place of the content
                    output[SCHEMA_FIELD_CONTENT] = output.pop(__FIELD_HIGHLIGHT)
                output = OrderedDict(**{k: v for (k, v) in output.items() if k in source_filtering})

            if explain:
                # https://docs.rs/tantivy/latest/tantivy/query/trait.Query.html#method.explain
                # https://github.com/quickwit-oss/tantivy-py/blob/master/docs/tutorials.md#debugging-queries-with-explain
                explanation = query.explain(searcher, doc_address)
                output[__FIELD_EXPLAIN] = json.loads(explanation.to_json())

            if format == Format.TXT:
                outputs.append(LINE_BREAK)

            # endregion

            outputs.append(output)

        render(
            {
                'took': {
                    'index': took_index,
                    'search': took,
                },
                'hits': outputs,
            },
            format,
        )

    # endregion


def __top_keywords_impl(
    searcher: tantivy.Searcher,
    query: tantivy.Query,
    limit: int,
    format: Format,
    took_index: Optional[int] = None,
) -> None:
    # region Search

    agg_name = 'top_keywords'
    top_count = max(limit, 1)

    start = monotonic_ns()
    result: Dict[str, Any] = searcher.aggregate(
        query,
        {
            agg_name: {
                'terms': {
                    'field': SCHEMA_FIELD_CONTENT,
                    # Extra size to discard potential stop-words.
                    # No extra size for digits, as it would lead to request for too many buckets.
                    'size': top_count + STOP_WORDS_COUNT,
                },
            },
        },
    )
    took = monotonic_ns() - start

    # endregion
    # region Process result

    top_keywords = result[agg_name]

    outputs: List[TOutput] = []
    count = 0
    sum_other_doc_count = 0  # Discarded stop-words count

    for bucket in top_keywords['buckets']:
        key: str = bucket['key']
        if len(key) < config.top_min_chars or key.isdigit() or is_stopword(key):
            # Exclude single characters, digits, stop-words
            sum_other_doc_count += bucket['doc_count']
            continue

        output = OrderedDict(
            key=key,
            doc_count=bucket['doc_count'],
        )
        count += 1

        if format == Format.TXT:
            outputs.append(LINE_BREAK)

        outputs.append(output)
        if count >= limit:
            break

    render(
        {
            'took': {
                'index': took_index,
                'search': took,
            },
            'sum_other_doc_count': top_keywords['sum_other_doc_count'] + sum_other_doc_count,
            'doc_count_error_upper_bound': top_keywords['doc_count_error_upper_bound'],
            'keywords': outputs,
        },
        format,
    )

    # endregion


def __build_output_from_snippet(snippet: tantivy.Snippet) -> Optional[Dict[str, Any]]:
    highlighted = snippet.highlighted()
    if not highlighted:
        return None

    return {
        'html': snippet.to_html(),
        'fragment': snippet.fragment(),
        'ranges': [
            {
                'start': h.start,
                'end': h.end,
            }
            for h in highlighted
        ],
    }


def __get_order_by_field(sort_field: Optional[str]) -> Tuple[Optional[str], tantivy.Order]:
    """
    Get the field and the order to use to sort the search result.

    >>> __get_order_by_field(None)
    (None, Order.Desc)

    >>> __get_order_by_field('')
    (None, Order.Desc)

    >>> __get_order_by_field('+size')
    ('size', Order.Asc)

    >>> __get_order_by_field('-size')
    ('size', Order.Desc)

    >>> __get_order_by_field('size')
    ('size', Order.Desc)
    """
    order_by_field: Optional[str] = None
    order: tantivy.Order = tantivy.Order.Desc

    if sort_field:
        if (sign := sort_field[0]) in ['+', '-']:
            order_by_field = sort_field[1:]
            order = tantivy.Order.Desc if sign == '-' else tantivy.Order.Asc
        else:
            order_by_field = sort_field

    return (order_by_field, order)
