"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceOrbitOrbitEnum(str, Enum):
    ORBIT = 'orbit'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOrbit:
    r"""The values required to configure the source."""
    
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""Authorizes you to work with Orbit workspaces associated with the token."""
    source_type: SourceOrbitOrbitEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    workspace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace') }})
    r"""The unique name of the workspace that your API token is associated with."""
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    r"""Date in the format 2022-06-26. Only load members whose last activities are after this date."""
    