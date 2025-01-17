"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceNetsuiteNetsuiteEnum(str, Enum):
    NETSUITE = 'netsuite'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceNetsuite:
    r"""The values required to configure the source."""
    
    consumer_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consumer_key') }})
    r"""Consumer key associated with your integration"""
    consumer_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('consumer_secret') }})
    r"""Consumer secret associated with your integration"""
    realm: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('realm') }})
    r"""Netsuite realm e.g. 2344535, as for `production` or 2344535_SB1, as for the `sandbox`"""
    source_type: SourceNetsuiteNetsuiteEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_datetime: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_datetime') }})
    r"""Starting point for your data replication, in format of \\"YYYY-MM-DDTHH:mm:ssZ\\" """
    token_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_key') }})
    r"""Access token key"""
    token_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_secret') }})
    r"""Access token secret"""
    object_types: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_types'), 'exclude': lambda f: f is None }})
    r"""The API names of the Netsuite objects you want to sync. Setting this speeds up the connection setup process by limiting the number of schemas that need to be retrieved from Netsuite."""
    window_in_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('window_in_days'), 'exclude': lambda f: f is None }})
    r"""The amount of days used to query the data with date chunks. Set smaller value, if you have lots of data."""
    