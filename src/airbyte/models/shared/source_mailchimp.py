"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceMailchimpCredentialsAPIKeyAuthTypeEnum(str, Enum):
    APIKEY = 'apikey'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMailchimpCredentialsAPIKey:
    
    apikey: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apikey') }})
    r"""Mailchimp API Key. See the <a href=\\"https://docs.airbyte.com/integrations/sources/mailchimp\\">docs</a> for information on how to generate this key."""
    auth_type: SourceMailchimpCredentialsAPIKeyAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    
class SourceMailchimpCredentialsOAuth20AuthTypeEnum(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMailchimpCredentialsOAuth20:
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""An access token generated using the above client ID and secret."""
    auth_type: SourceMailchimpCredentialsOAuth20AuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The Client ID of your OAuth application."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The Client Secret of your OAuth application."""
    
class SourceMailchimpMailchimpEnum(str, Enum):
    MAILCHIMP = 'mailchimp'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMailchimp:
    r"""The values required to configure the source."""
    
    source_type: SourceMailchimpMailchimpEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    campaign_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('campaign_id'), 'exclude': lambda f: f is None }})
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    