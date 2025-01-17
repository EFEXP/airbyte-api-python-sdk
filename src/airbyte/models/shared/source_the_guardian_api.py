"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceTheGuardianAPITheGuardianAPIEnum(str, Enum):
    THE_GUARDIAN_API = 'the-guardian-api'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTheGuardianAPI:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Your API Key. See <a href=\\"https://open-platform.theguardian.com/access/\\">here</a>. The key is case sensitive."""
    source_type: SourceTheGuardianAPITheGuardianAPIEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""Use this to set the minimum date (YYYY-MM-DD) of the results. Results older than the start_date will not be shown."""
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    r"""(Optional) Use this to set the maximum date (YYYY-MM-DD) of the results. Results newer than the end_date will not be shown. Default is set to the current date (today) for incremental syncs."""
    query: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('query'), 'exclude': lambda f: f is None }})
    r"""(Optional) The query (q) parameter filters the results to only those that include that search term. The q parameter supports AND, OR and NOT operators."""
    section: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('section'), 'exclude': lambda f: f is None }})
    r"""(Optional) Use this to filter the results by a particular section. See <a href=\\"https://content.guardianapis.com/sections?api-key=test\\">here</a> for a list of all sections, and <a href=\\"https://open-platform.theguardian.com/documentation/section\\">here</a> for the sections endpoint documentation."""
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tag'), 'exclude': lambda f: f is None }})
    r"""(Optional) A tag is a piece of data that is used by The Guardian to categorise content. Use this parameter to filter results by showing only the ones matching the entered tag. See <a href=\\"https://content.guardianapis.com/tags?api-key=test\\">here</a> for a list of all tags, and <a href=\\"https://open-platform.theguardian.com/documentation/tag\\">here</a> for the tags endpoint documentation."""
    