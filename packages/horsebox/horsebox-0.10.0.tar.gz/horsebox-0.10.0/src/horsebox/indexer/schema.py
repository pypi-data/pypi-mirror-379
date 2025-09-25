from dataclasses import dataclass
from enum import Enum
from typing import (
    List,
    Optional,
)

import tantivy


class FieldType(str, Enum):
    """Types of Fields."""

    TEXT = 'text'
    INTEGER = 'integer'
    DATE = 'date'


@dataclass
class Field:
    """Index Field."""

    name: str
    type: FieldType
    description: str
    stored: bool = True
    indexed: bool = True
    # https://docs.rs/tantivy/latest/tantivy/fastfield/
    fast: bool = False
    # It will chop your text on punctuation and whitespaces,
    # removes tokens that are longer than 40 chars, and lowercase your text.
    # https://docs.rs/tantivy/latest/tantivy/tokenizer/#default
    analyzer: str = 'default'
    """
    'default', 'raw' or 'en_stem'

    See https://docs.rs/tantivy/latest/tantivy/tokenizer/
    """
    index_option: str = 'position'
    """
    'basic', 'freq' or 'position'

    See https://docs.rs/tantivy/latest/tantivy/schema/enum.IndexRecordOption.html
    """


SCHEMA_FIELD_CONTENT = 'content'
SCHEMA_FIELDS: List[Field] = [
    Field(
        'name',
        FieldType.TEXT,
        'Name of the container (file, etc.)',
        fast=True,
    ),
    Field(
        'type',
        FieldType.TEXT,
        'Type of the container',
        fast=True,
    ),
    # `fast` mode is required to aggregate on `content`
    Field(
        SCHEMA_FIELD_CONTENT,
        FieldType.TEXT,
        'Content of the container',
        fast=True,
    ),
    Field('path', FieldType.TEXT, 'Full path to the content', indexed=False),
    Field(
        'size',
        FieldType.INTEGER,
        'Size of the content',
        fast=True,
    ),
    Field(
        'date',
        FieldType.DATE,
        'Date-time of the content',
        fast=True,
    ),
]
DEFAULT_FIELD_NAMES = [
    'name',
    SCHEMA_FIELD_CONTENT,
]
"""
Fields used to search if no field is specifically defined in the query.
By default, all tokenized and indexed fields are default fields.
"""
SCHEMA_ANALYZER_CUSTOM = 'custom'
SCHEMA_FIELD_CONTENT_CUSTOM = 'custom'
SCHEMA_FIELDS_CUSTOM: List[Field] = [
    Field(
        SCHEMA_FIELD_CONTENT_CUSTOM,
        FieldType.TEXT,
        'Content of the container with custom analyzer',
        # Required to support highlight, with the trade-off a bigger storage
        stored=True,
        analyzer=SCHEMA_ANALYZER_CUSTOM,
    ),
]


def get_schema(custom_fields: Optional[List[Field]] = None) -> tantivy.Schema:
    """
    Get the schema of the index.

    Args:
        custom_fields (Optional[List[Field]]): The custom fields to add to the default schema.
            Defaults to None.
    """
    builder = tantivy.SchemaBuilder()

    for field in SCHEMA_FIELDS + (custom_fields or []):
        if field.type == FieldType.TEXT:
            builder = builder.add_text_field(
                field.name,
                stored=field.stored,
                # `fast` added in https://github.com/quickwit-oss/tantivy-py/pull/458
                fast=field.fast,
                tokenizer_name=field.analyzer,
                index_option=field.index_option,
            )
        elif field.type == FieldType.INTEGER:
            builder = builder.add_integer_field(
                field.name,
                stored=field.stored,
                indexed=field.indexed,
                fast=field.fast,
            )
        elif field.type == FieldType.DATE:
            builder = builder.add_date_field(
                field.name,
                stored=field.stored,
                indexed=field.indexed,
                fast=field.fast,
            )
        else:
            raise NotImplementedError(f'Invalid field type: {field.type}')

    return builder.build()
