"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceConfluenceConfluenceEnum(str, Enum):
    CONFLUENCE = 'confluence'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceConfluence:
    r"""The values required to configure the source."""
    
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""Please follow the Jira confluence for generating an API token: <a href=\\"https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/\\">generating an API token</a>."""
    domain_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_name') }})
    r"""Your Confluence domain name"""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""Your Confluence login email"""
    source_type: SourceConfluenceConfluenceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    