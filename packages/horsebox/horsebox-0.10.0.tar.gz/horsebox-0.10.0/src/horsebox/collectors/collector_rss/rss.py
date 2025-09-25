import html
from typing import (
    Any,
    Dict,
    Generator,
    Iterable,
    List,
    cast,
)

import feedparser

from horsebox.cli import FILENAME_PREFIX
from horsebox.indexer.factory import prepare_doc
from horsebox.model import TDocument
from horsebox.model.collector import Collector
from horsebox.utils.normalize import strip_html_tags

_RSS_CONTENT = ['title', 'summary']


class CollectorRSS(Collector):
    """RSS Feed Collector Class."""

    feeds: List[str]

    def __init__(  # noqa: D107
        self,
        feeds: List[str],
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)

        self.feeds = feeds

    @staticmethod
    def create_instance(**kwargs: Any) -> Collector:
        """Create an instance of the collector."""
        return CollectorRSS(
            kwargs.pop('root_path'),
            **kwargs,
        )

    def collect(self) -> Iterable[TDocument]:
        """
        Collect the data to index.

        Returns:
            Iterable[TDocument]: The collected documents.
        """
        for feed in self.feeds:
            yield from self.parse(
                '',
                feed[1:] if feed.startswith(FILENAME_PREFIX) else feed,
            )

    def parse(
        self,
        root_path: str,
        file_path: str,
    ) -> Generator[TDocument, Any, None]:
        """
        Parse a file for indexing by its content.

        Args:
            root_path (str): Base path of the file.
            file_path (str): File to parse.

        Yields:
            Generator[TDocument, Any, None]: The document to index (one document per file).
        """
        feed = file_path

        if self.dry_run:
            yield prepare_doc(
                path=file_path,
            )
            return

        parsed = feedparser.parse(feed[1:] if feed.startswith(FILENAME_PREFIX) else feed)
        for item in parsed.entries:
            yield self.__build_doc(item)

    def __build_doc(
        self,
        item: feedparser.FeedParserDict,
    ) -> TDocument:
        """Build a document to be indexed."""
        # If a deterministic `doc_id` is required (for document update/deletion),
        # it could be generated with `abs(hash(kwargs['path']))`

        doc: TDocument = {}
        contents: Dict[str, str] = {}

        for tag in _RSS_CONTENT:
            if value := item.get(tag):
                contents[tag] = html.unescape(strip_html_tags(cast(str, value)))

        if content := '\n'.join(filter(None, [contents.get(x) for x in _RSS_CONTENT])):
            doc['content'] = content
        if title := contents.get('title'):
            doc['name'] = title

        if value := item.get('link'):
            doc['path'] = value

        for tag in ['updated_parsed', 'published_parsed']:
            if value := item.get(tag):
                doc['date'] = value
                break

        return prepare_doc(**doc)
