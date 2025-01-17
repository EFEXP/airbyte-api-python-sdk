"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DestinationMeilisearchMeilisearchEnum(str, Enum):
    MEILISEARCH = 'meilisearch'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMeilisearch:
    r"""The values required to configure the destination."""
    
    destination_type: DestinationMeilisearchMeilisearchEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Hostname of the MeiliSearch instance."""
    api_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key'), 'exclude': lambda f: f is None }})
    r"""MeiliSearch API Key. See the <a href=\\"https://docs.airbyte.com/integrations/destinations/meilisearch\\">docs</a> for more information on how to obtain this key."""
    