"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class SourceSonarCloudSonarCloudEnum(str, Enum):
    SONAR_CLOUD = 'sonar-cloud'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSonarCloud:
    r"""The values required to configure the source."""
    
    component_keys: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('component_keys') }})
    r"""Comma-separated list of component keys."""
    organization: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization') }})
    r"""Organization key. See <a href=\\"https://docs.sonarcloud.io/appendices/project-information/#project-and-organization-keys\\">here</a>."""
    source_type: SourceSonarCloudSonarCloudEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    user_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_token') }})
    r"""Your User Token. See <a href=\\"https://docs.sonarcloud.io/advanced-setup/user-accounts/\\">here</a>. The token is case sensitive."""
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""To retrieve issues created before the given date (inclusive)."""
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""To retrieve issues created after the given date (inclusive)."""
    