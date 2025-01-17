"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceTrelloTrelloEnum(str, Enum):
    TRELLO = 'trello'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTrello:
    r"""The values required to configure the source."""
    
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    r"""Trello API key. See the <a href=\\"https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/#using-basic-oauth\\">docs</a> for instructions on how to generate it."""
    source_type: SourceTrelloTrelloEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    r"""Trello API token. See the <a href=\\"https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/#using-basic-oauth\\">docs</a> for instructions on how to generate it."""
    board_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('board_ids'), 'exclude': lambda f: f is None }})
    r"""IDs of the boards to replicate data from. If left empty, data from all boards to which you have access will be replicated."""
    