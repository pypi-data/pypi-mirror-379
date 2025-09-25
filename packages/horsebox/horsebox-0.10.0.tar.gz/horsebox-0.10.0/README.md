# Horsebox

A versatile and autonomous command line tool for search.

[![tests badge](https://github.com/michelcaradec/horsebox/actions/workflows/python-tests.yml/badge.svg?branch=main)](https://github.com/michelcaradec/horsebox/actions/workflows/python-tests.yml) ![pypi badge](https://img.shields.io/pypi/v/horsebox) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit) ![mypy](https://img.shields.io/badge/type-mypy-039dfc) [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/michelcaradec/horsebox)

<details>
<summary>Table of contents</summary>

- [Abstract](#abstract)
- [TL;DR](#tldr)
- [Requirements](#requirements)
- [Tool Installation](#tool-installation)
- [Project Setup](#project-setup)
  - [Python Environment](#python-environment)
  - [Pre-Commit Setup](#pre-commit-setup)
    - [Pre-Commit Tips](#pre-commit-tips)
- [Usage](#usage)
  - [Naming Conventions](#naming-conventions)
  - [Getting Help](#getting-help)
  - [Rendering](#rendering)
  - [Searching](#searching)
  - [Building An Index](#building-an-index)
  - [Refreshing An Index](#refreshing-an-index)
  - [Inspecting An Index](#inspecting-an-index)
  - [Analyzing Some Text](#analyzing-some-text)
- [Concepts](#concepts)
  - [Collectors](#collectors)
    - [Raw Collector](#raw-collector)
    - [Guess Collector](#guess-collector)
    - [Collectors Usage Matrix](#collectors-usage-matrix)
    - [Collectors Simplified Patterns](#collectors-simplified-patterns)
  - [Index](#index)
  - [Strategies](#strategies)
- [Annexes](#annexes)
  - [Project Bootstrap](#project-bootstrap)
  - [Unit Tests](#unit-tests)
  - [Manual Testing In Docker](#manual-testing-in-docker)
  - [Samples](#samples)
  - [Advanced Searches](#advanced-searches)
  - [Using A Custom Analyzer](#using-a-custom-analyzer)
    - [Custom Analyzer Definition](#custom-analyzer-definition)
    - [Custom Analyzer Limitations](#custom-analyzer-limitations)
  - [Configuration](#configuration)
  - [VSCode Integration](#vscode-integration)
  - [Where Does This Name Come From](#where-does-this-name-come-from)

</details>

## Abstract

Anybody faced at least once a situation where searching for some information was required, whether it was from a project folder, or any other place that contains information of interest.  

[Horsebox](#where-does-this-name-come-from) is a tool whose purpose is to offer such search feature (thanks to the full-text search engine library [Tantivy](https://github.com/quickwit-oss/tantivy)), without any external dependencies, from the command line.

While it was built with a developer persona in mind, it can be used by anybody who is not afraid of typing few characters in a terminal ([samples](#samples) are here to guide you).

Disclaimer: this tool was tested on Linux (Ubuntu, Debian) and MacOS only.

## TL;DR

*For the ones who want to go **straight** to the point.*

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# Install Horsebox
uv tool install horsebox

# Alternative: install from the repository
# For the impatient users who want the latest features before they are published on PyPi
uv tool install git+https://github.com/michelcaradec/horsebox
```

You are ready to [search](#searching).

## Requirements

All the commands described in this project rely on the Python package and project manager [uv](https://docs.astral.sh/uv/).

1. Install uv:

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. Or update it:

    ```bash
    uv self update
    ```

## Tool Installation

*For the ones who just want to **use** the tool.*

1. Install the tool:

   - From PyPi:

       ```bash
       uv tool install horsebox
       ```

   - From the online Github project:

       ```bash
       uv tool install git+https://github.com/michelcaradec/horsebox
       ```

2. [Use](#usage) the tool.

## Project Setup

*For the ones who want to **develop** on the project.*

### Python Environment

1. Clone the project:

    ```bash
    git clone https://github.com/michelcaradec/horsebox.git

    cd horsebox
    ```

2. Create a Python virtual environment:

    ```bash
    uv sync

    # Install the development requirements
    uv sync --extra dev

    # Activate the environment
    source .venv/bin/activate
    ```

3. Check the tool execution:

    ```bash
    uv run horsebox
    ```

    Alternate commands:

    - `uv run hb`.
    - `uv run ./src/horsebox/main.py`.
    - `python ./src/horsebox/main.py`.

4. The tool can also be installed from the local project with the command:

    ```bash
    uv tool install --editable .
    ```

5. [Use](#usage) the tool.

### Pre-Commit Setup

1. Install the git hook scripts:

    ```bash
    pre-commit install
    ```

2. [Update the hooks](https://pre-commit.com/#updating-hooks-automatically) to the latest version automatically:

    ```bash
    pre-commit autoupdate
    ```

#### Pre-Commit Tips

- Manually run against all the files:

    ```bash
    pre-commit run --all-files --show-diff-on-failure
    ```

- Bypass pre-commit when committing:

    ```bash
    git commit --no-verify
    ```

- Un-install the git hook scripts:

    ```bash
    pre-commit uninstall
    ```

## Usage

### Naming Conventions

The following terms are used:

- **Datasource**: the place where the information will be collected from. It can be a folder, a web page, an RSS feed, etc.
- **Container**: the "box" containing the information. It can be a file, a web page, an RSS article, etc.
- **Content**: the information contained in a container. It is mostly text, but can also be a date of last update for a file.
- **[Collector](#collectors)**: a working unit in charge of gathering information to be converted in searchable one.

### Getting Help

To list the available commands:

```bash
hb --help
```

To get help for a given command (here `search`):

```bash
hb search --help
```

### Rendering

For any command, the option `--format` specifies the output format:

- `txt`: text mode (default).
- `json`: JSON. The shortcut option `--json` can also be used.

### Searching

The query string syntax, specified with the option `--query`, is the one supported by the [Tantivy's query parser](https://docs.rs/tantivy/latest/tantivy/query/struct.QueryParser.html).

Example: search in text files (with extension `.txt`) under the folder `demo`.

```bash
hb search --from ./demo/ --pattern "*.txt" --query "better" --highlight
```

Options used:

- `--from`: folder to (recursively) index.
- `--pattern`: files to index.

> [!IMPORTANT]
> The pattern must be enclosed in quotes to prevent wildcard expansion.

- `--query`: search query.
- `--highlight`: shows the places where the result was found in the content of the files.

One result is returned, as there is only one document (i.e. container) in the index.

A different [collector](#collectors) can be used to index line by line:

```bash
hb search --from ./demo/ --pattern "*.txt" --using fileline --query "better" --highlight --limit 5
```

Options used:

- `--using`: collector to use for indexing.
- `--limit`: returns a maximum number of results (default is 10).

The option `--count` can be added to show the total number of results found:

```bash
hb search --from ./demo/ --pattern "*.txt" --using fileline --query "better" --count
```

*See the section [samples](#samples) for advanced usage.*

### Building An Index

Example: build an index `.index-demo` from the text files (with extension `.txt`) under the folder `demo`.

```bash
hb build --from ./demo/ --pattern "*.txt" --index ./.index-demo
```

Options used:

- `--from`: folder to (recursively) index.
- `--pattern`: files to index.

> [!IMPORTANT]
> The pattern must be enclosed in quotes to prevent wildcard expansion.

- `--index`: location where to persist the index.

By default, the [collector](#collectors) `filecontent` is used.  
An alternate collector can be specified with the option `--using`.  
The option `--dry-run` can be used to show the items to be index, without creating the index.

The built index can be searched:

```bash
hb search --index ./.index-demo --query "better" --highlight
```

Searching on a persisted index will trigger a warning if the age of the index (i.e. the time elapsed since it was built) goes over a given threshold (which can be [configured](#configuration)).  
The index can be [refreshed](#refreshing-an-index) to contain the most up-to-date data.

### Refreshing An Index

A built index can be refreshed to contain the most up-to-date data.

Example: refresh the index `.index-demo` [previously built](#building-an-index).

```bash
hb refresh --index ./.index-demo
```

There are cases where an index can't be refreshed:

- The index was built with a version prior to `0.4.0`.
- The index data source was provided by pipe (see the section [Collectors Usage Matrix](#collectors-usage-matrix)).

### Inspecting An Index

To get technical information on an existing index:

```bash
hb inspect --index ./.index-demo
```

To get the most frequent keywords (option `--top`):

```bash
hb search --index ./.index-demo --top
```

### Analyzing Some Text

> [!NOTE]
> The version `0.7.0` introduced a [new option](#using-a-custom-analyzer) `--analyzer`, which replaces the legacy ones (`--tokenizer`, `--tokenizer-params`, `--filter` and `--filter-params`). Even-though the use of this new option is strongly recommended, the legacies are still available with the command `analyze`.

The command `analyze` is used to play with the [tokenizers](https://docs.rs/tantivy/latest/tantivy/tokenizer/trait.Tokenizer.html) and [filters](https://docs.rs/tantivy/latest/tantivy/tokenizer/trait.TokenFilter.html) supported by Tantivy to index documents.

To tokenize a text:

```bash
hb analyze \
    --text "Tantivy is a full-text search engine library inspired by Apache Lucene and written in Rust." \
    --tokenizer whitespace
```

To filter a text:

```bash
hb analyze \
    --text "Tantivy is a full-text search engine library inspired by Apache Lucene and written in Rust." \
    --filter lowercase
```

*Multiple examples can be found in the script [usage.sh](./demo/usage.sh).*

## Concepts

Horsebox has been thought around few concepts:

- [Collectors](#collectors).
- [Index](#index).

Understanding them will help in choosing the right usage [strategy](#strategies).

### Collectors

A collector is in charge of **gathering information** from a given **datasource**, and returning **documents** to [index](#index).  
It acts as a level of abstraction, which returns documents to be ingested.

Horsebox supports different types of collectors:

| Collector     | Description                                                     |
| ------------- | --------------------------------------------------------------- |
| `filename`    | One document per file, containing the name of the file only.    |
| `filecontent` | One document per file, with the content of the file (default).  |
| `fileline`    | One document per line and per file.                             |
| `rss`         | RSS feed, one document per article.                             |
| `html`        | Collect the content of an HTML page.                            |
| `raw`         | Collect ready to index [JSON documents](#raw-collector).        |
| `pdf`         | Collect the content of a PDF document.                          |
| `guess`       | Used to identify the [best collector](#guess-collector) to use. |

The collector to use is specified with the option `--using`.  
The default collector is `filecontent`.

*See the script [usage.sh](./demo/usage.sh) for sample commands.*

#### Raw Collector

The collector `raw` can be used to collect ready to index JSON documents.

Each document must have the following fields [^4]:

- `name` (`text`): name of the [container](#naming-conventions).
- `type` (`text`): type of the container.
- `content` (`text`): content of the container.
- `path` (`text`): full path to the content.
- `size` (`integer`): size of the content.
- `date` (`text`): date-time of the content (formatted as `YYYY-mm-dd H:M:S`, for example `2025-03-14 12:34:56`).

The JSON file can contain either an **array** of JSON objects (default), or one JSON object per **line** ([JSON Lines](https://jsonlines.org/) format).  
The JSON Lines format is automatically detected from the file extension (`.jsonl` or `ndjson`).  
The option `--jsonl` can be used to **force** the detection (this is for example required when the data source is provided by pipe).

Some examples can be found with the files [raw.json](./demo/raw.json) (array of objects) and [raw.jsonl](./demo/raw.jsonl) (JSON Lines).

[^4]: Run the command `hb schema` for a full description.

#### Guess Collector

*Disclaimer: starting with version `0.5.0`.*

The collector `guess` can be used to identify the best collector to use.  
The detection is done in a [best effort](#collectors-usage-matrix) from the options `--from` and `--pattern`.  
An error will be returned if no collector could be guessed.

The collector `guess` is used by default, meaning that the option `--using` can be skipped.

Examples:

```bash
hb search --from "https://planetpython.org/rss20.xml" --query "some text" --using rss
# Can be simplified as (guess from the https scheme and the extension .xml)
hb search --from "https://planetpython.org/rss20.xml" --query "some text"
```

```bash
hb search --from ./raw.json --query "some text" --using raw
# Can be simplified as (guess from the file extension .json)
hb search --from ./raw.json --query "some text"
```

```bash
hb search --from ./raw.jsonl --query "some text" --using raw --jsonl
# Can be simplified as (guess from the file extension .jsonl)
hb search --from ./raw.jsonl --query "some text"
```

This feature is mainly for command line usage, to help reduce the number of keystrokes.  
When used in a script, it is advised to explicitly set the required collector with the option `--using`.

#### Collectors Usage Matrix

The following table shows the options supported by each collector.

| Collector     | Multi-Sources Mode               | Single Source Mode | Pipe Support                   |
| ------------- | -------------------------------- | ------------------ | ------------------------------ |
| `filename`    | `--from $folder --pattern *.xxx` | -                  | -                              |
| `filecontent` | `--from $folder --pattern *.xxx` | -                  | `--from - --using filecontent` |
| `fileline`    | `--from $folder --pattern *.xxx` | -                  | `--from - --using fileline`    |
| `rss`         | -                                | `--from $feed`     | -                              |
| `html`        | -                                | `--from $page`     | -                              |
| `raw`         | -                                | `--from $json`     | `--from - --using raw`         |
| `pdf`         | `--from $folder --pattern *.pdf` | `--from $file.pdf` | -                              |

*`-`: not supported.*

These options are also used by the [guess collector](#guess-collector) in its detection.

#### Collectors Simplified Patterns

*Disclaimer: starting with version `0.8.0`.*

The file system [collectors](#collectors) use the combined options `--from` and `--pattern` to specify the folder to (recursively) scan, and the files to index.

For example, the options `--from ./demo` and `--from ./demo/ --pattern "*.txt"` will index the files with the extension `.txt` located under the folder `./demo`.

While this syntax makes a clear separation between the [datasource and the containers](#naming-conventions), it can be long to type, especially for standard patterns.

The list of arguments can be **simplified** by combining both options.

Examples:

- `--from ./demo --from ./demo/ --pattern "*.txt"` can be passed as `--from "./demo/*.txt"`.
- `--from . --pattern "*.pdf"` can be passed as `--from "*.pdf"`.

> [!IMPORTANT]
> The pattern must be enclosed in quotes to prevent wildcard expansion.

This new syntax still allows the use of the option `--pattern` (for example, `--from "*.pdf" --pattern "*.pdf"` will index all the files with the extension `.txt` or `.pdf`from the current folder).

### Index

The index is the place where the [collected](#collectors) information lies. It is required to allow the search.

An index is built with the help of [Tantivy](https://github.com/quickwit-oss/tantivy) (a full-text search engine library), and can be either stored in **memory** or persisted on **disk** (see the section [strategies](#strategies)).

### Strategies

Horsebox can be used in different ways to achieve to goal of searching (and hopefully finding) some information.

- One-step search:  
    Index and [search](#searching), with **no** index **retention**.  
    This fits an **unstable** source of information, with frequent changes.

    ```bash
    hb search --from ./demo/ --pattern "*.txt" --query "better" --highlight
    ```

- Two-steps search:  
    [Build](#building-an-index) and persist an index, then [search](#searching) in the existing index.  
    This fits a **stable** and **voluminous** (i.e. long to index) source of information.

    Build the index once:

    ```bash
    hb build --from ./demo/ --pattern "*.txt" --index ./.index-demo
    ```

    Then search it (multiple times):

    ```bash
    hb search --index ./.index-demo --query "better" --highlight
    ```

- All-in-one search:  
    Like a two-steps search, but in **one step**.  
    For the ones who want to do everything in a single command.

    ```bash
    hb search --from ./demo/ --pattern "*.txt" --index ./.index-demo --query "better" --highlight
    ```

    The use of the options `--from` and `--index` with the command `search` will [build and persist](#building-an-index) an index, which will be immediately [searched](#searching), and will also be available for future searches.

## Annexes

### Project Bootstrap

The project was created with the command:

```bash
# Will create a directory `horsebox`
uv init --app --package --python 3.10 horsebox
```

### Unit Tests

The Python module [doctest](https://docs.python.org/3.10/library/doctest.html) has been used to write some unit tests:

```bash
python -m doctest -v ./src/**/*.py
```

### Manual Testing In Docker

Horsebox can be installed in a fresh environment to demonstrate its straight-forward setup:

```bash
# From the project
docker run --interactive --tty --name horsebox --volume=$(pwd):/home/project --rm debian:stable /bin/bash
# Alternative: Docker image with OhMyZsh (for colors)
docker run --interactive --tty --name horsebox --volume=$(pwd):/home/project --rm ohmyzsh/ohmyzsh:main

# Install few dependencies
source /home/project/demo/docker-setup.sh

# Install Horsebox
uv tool install .
```

### Samples

The script [usage.sh](./demo/usage.sh) contains multiple sample commands:

```bash
bash ./demo/usage.sh
```

### Advanced Searches

The query string syntax conforms to [Tantivy's query parser](https://docs.rs/tantivy/latest/tantivy/query/struct.QueryParser.html).

- Search on multiple datasources:  
    Multiple datasources can be collected to build/search an index by repeating the option `--from`.

    ```bash
    hb search \
        --from "https://www.blog.pythonlibrary.org/feed/" \
        --from "https://planetpython.org/rss20.xml" \
        --from "https://realpython.com/atom.xml?format=xml" \
        --using rss --query "duckdb" --highlight
    ```

    *Source: [Top 60 Python RSS Feeds](https://rss.feedspot.com/python_rss_feeds/).*

- Search on date:  
    A date must be formatted using the [RFC3339](https://en.wikipedia.org/wiki/ISO_8601) standard.  
    Example: `2025-01-01T10:00:00.00Z`.

    The field `date` must be specified, and the date must be enclosed in single quotes:

    ```bash
    hb search --from ./demo/raw.json --using raw --query "date:'2025-01-01T10:00:00.00Z'"
    ```

- Search on range of dates:  
    **Inclusive boundaries** are specified with square brackets (`[` `]`):

    ```bash
    hb search --from ./demo/raw.json --using raw --query "date:[2025-01-01T10:00:00.00Z TO 2025-01-04T10:00:00.00Z]"
    ```

    **Exclusive boundaries** are specified with curly brackets (`{` `}`):

    ```bash
    hb search --from ./demo/raw.json --using raw --query "date:{2025-01-01T10:00:00.00Z TO 2025-01-04T10:00:00.00Z}"
    ```

    Inclusive and exclusive boundaries can be **mixed**:

    ```bash
    hb search --from ./demo/raw.json --using raw --query "date:[2025-01-01T10:00:00.00Z TO 2025-01-04T10:00:00.00Z}"
    ````

- Fuzzy search:  
    The fuzzy search is not supported by Tantivy query parser [^6].  
    Horsebox comes with a simple implementation, which supports the expression of a fuzzy search on a **single word**.  
    Example: the search `engne~` will find the word "engine", as it differs by 1 change according to the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) measure.

    The distance can be set after the marker `~`, with a maximum of 2: `engne~1`, `engne~2`.

    ```bash
    hb search --from ./demo/raw.json --using raw --query "engne~1"
    ```

> [!IMPORTANT]
> The highlight (option `--highlight`) will not work [^5].

- Proximity search:  
    The two words to search are enclosed in single quotes, followed by the maximum distance.

    ```bash
    hb search --from ./demo/raw.json --using raw --query "'engine inspired'~1" --highlight
    ```

    *Will find all documents where the words "engine" and "inspired" are separated by a maximum of 1 word.*

- Query explanation:  
    The result of a query can be explained with the help of the option `--explain`.

    ```bash
    hb search --from "./demo/*.txt" --using fileline --query "better" --explain --json --limit 2
    ```

    For each document found, a field `explain` will be returned, with details on why it was selected [^11].

- Sort the result:  
    The result of a query can be ordered by a **single** field with the help of the option `--sort`.

    ```bash
    # Ascending order
    hb search --from "./demo/size/*.txt" --query "file" --sort "+size"
    # Descending order
    hb search --from "./demo/size/*.txt" --query "file" --sort "-size"
    hb search --from "./demo/size/*.txt" --query "file" --sort "size"
    ```

    The field prefix `+` is used for **ascending** order, `-` for **descending** order (set by default if missing).

> [!IMPORTANT]
> This option was introduced with the version `0.10.0`. It requires an existing index to be [refreshed](#refreshing-an-index) to make it work.  
> Only the fields `name`, `type`, `content`, `size` and `date` can be used.

[^5]: See <https://github.com/quickwit-oss/tantivy/issues/2576>.  
[^6]: Even though Tantivy implements it with [FuzzyTermQuery](https://docs.rs/tantivy/latest/tantivy/query/struct.FuzzyTermQuery.html).  
[^11]: See <https://docs.rs/tantivy/latest/tantivy/query/struct.Explanation.html>.

### Using A Custom Analyzer

*Disclaimer: starting with version `0.7.0`.*

By default, the [content of a container](#naming-conventions) is indexed in the [field](#raw-collector) `content` using the [default](https://docs.rs/tantivy/latest/tantivy/tokenizer/#default) [text analyzer](https://docs.rs/tantivy/latest/tantivy/tokenizer/), which splits the text on every white space and punctuation [^8], removes words (a.k.a tokens) that are longer than 40 characters [^9], and lowercases the text [^10].

While this text analyzer fits most of the cases, it may not be suitable for more specific content such as code.

The option `--analyzer` can be used with the commands `build` and `search` to apply a custom tokenizer and filters to the content to be indexed.  
The [definition of the custom analyzer](#custom-analyzer-definition) is described in a JSON file.  
The analyzed content will be indexed to an extra field `custom`.

To build an index `.index-analyzer` with a custom analyzer `analyzer-python.json`:

```bash
hb build \
    --index .index-analyzer \
    --from ./demo --pattern "*.py" \
    --using fileline \
    --analyzer ./demo/analyzer-python.json
```

A full set of examples can be found in the script [usage.sh](./demo/usage.sh).

#### Custom Analyzer Definition

The custom analyzer definition is described in a JSON file.

It is composed of two parts:

- `tokenizer`: the tokenizer to use to split the content. There must be one and only one tokenizer.
- `filters`: the filters to use to transform and select the tokenized content. There can be zero or more filters.

```json
{
    "tokenizer": {
        "$tokenize_type": {...}
    },
    "filters": [
        {
            "$filter_type": {...}
        },
        {
            "$filter_type": {...}
        }
    ]
}
```

Each object `$tokenize_type` and `$filter_type` may contain extra configuration fields.

The file [analyzer-schema.json](./demo/analyzer-schema.json) is a [JSON Schema](https://json-schema.org/) which can be used to **validate** any custom analyzer definition.  
The site [JSON Editor Online](https://jsoneditoronline.org/) proposes a [playground](https://jsoneditoronline.org/indepth/validate/json-schema-validator/#Try_it_out) to test it from your browser.  
The Python library [jsonschema](https://pypi.org/project/jsonschema/) proposes an implementation of JSON Schema validation.

#### Custom Analyzer Limitations

- When a custom analyzer is defined, the [highlight](#searching) is done of the field `custom`.
- The tokenizer [regex](https://docs.rs/tantivy/latest/tantivy/tokenizer/struct.RegexTokenizer.html) uses the pattern syntax supported by the [Regex](https://docs.rs/tantivy-fst/latest/tantivy_fst/struct.Regex.html) implementation.
- The option `--top` is not applied on the field `custom`, due to the [fast](https://docs.rs/tantivy/latest/tantivy/fastfield/) mode required for aggregation, but not compatible with the tokenizer [regex](https://docs.rs/tantivy/latest/tantivy/tokenizer/struct.RegexTokenizer.html).

[^8]: Using the tokenizer [simple](https://docs.rs/tantivy/latest/tantivy/tokenizer/struct.SimpleTokenizer.html).  
[^9]: Using the filter [remove_long](https://docs.rs/tantivy/latest/tantivy/tokenizer/struct.RemoveLongFilter.html).  
[^10]: Using the filter [lowercase](https://docs.rs/tantivy/latest/tantivy/tokenizer/struct.LowerCaser.html).

### Configuration

Horsebox can be configured through **environment variables**:

| Setting                  | Description                                                                  | Default Value |
| ------------------------ | ---------------------------------------------------------------------------- | ------------: |
| `HB_INDEX_BATCH_SIZE`    | Batch size when indexing.                                                    |          1000 |
| `HB_HIGHLIGHT_MAX_CHARS` | Maximum number of characters to show for highlights.                         |           200 |
| `HB_PARSER_MAX_LINE`     | Maximum size of a line in a container (unlimited if null).                   |               |
| `HB_PARSER_MAX_CONTENT`  | Maximum size of a container (unlimited if null).                             |               |
| `HB_RENDER_MAX_CONTENT`  | Maximum size of a document content to render (unlimited if null).            |               |
| `HB_INDEX_EXPIRATION`    | Index freshness threshold (in seconds).                                      |          3600 |
| `HB_CUSTOM_STOPWORDS`    | Custom list of stop-words (separated by a comma).                            |               |
| `HB_STRING_NORMALIZE`    | Normalize strings [^7] when reading files (0=disabled, other value=enabled). |             1 |
| `HB_TOP_MIN_CHARS`       | Minimum number of characters of a top keyword.                               |             1 |

To get help on configuration:

```bash
hb config
```

*The default and current values are displayed.*

[^7]: The normalization of a string consists in replacing the accented characters by their non-accented equivalent, and converting Unicode escaped characters. This is a CPU intensive process, which may not be required for some datasources.

### VSCode Integration

If you use [Visual Studio Code](https://code.visualstudio.com), you can integrate Horsebox using [tasks](https://code.visualstudio.com/docs/debugtest/tasks).

The file [tasks.json](./demo/vscode/tasks.json) provides some sample tasks to index and search Markdown files in the current project.

### Where Does This Name Come From

I had some requirements to find a name:

- Short and easy to remember.
- Preferably a compound one, so it could be shortcut at the command line with the first letters of each part.
- Connected to Tantivy, whose logo is a rider on a horse.

I then remembered the nickname of a very good friend met during my studies in Cork, Ireland: "Horsebox".

That was it: the name will be "Horsebox", with its easy-to-type shortcut "hb".
