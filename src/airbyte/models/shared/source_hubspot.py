"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Any

class SourceHubspotCredentialsPrivateAppCredentialsEnum(str, Enum):
    r"""Name of the credentials set"""
    PRIVATE_APP_CREDENTIALS = 'Private App Credentials'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceHubspotCredentialsPrivateApp:
    r"""Choose how to authenticate to HubSpot."""
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""HubSpot Access token. See the <a href=\\"https://developers.hubspot.com/docs/api/private-apps\\">Hubspot docs</a> if you need help finding this token."""
    credentials_title: SourceHubspotCredentialsPrivateAppCredentialsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title') }})
    r"""Name of the credentials set"""
    
class SourceHubspotCredentialsOAuthCredentialsEnum(str, Enum):
    r"""Name of the credentials"""
    O_AUTH_CREDENTIALS = 'OAuth Credentials'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceHubspotCredentialsOAuth:
    r"""Choose how to authenticate to HubSpot."""
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your HubSpot developer application. See the <a href=\\"https://legacydocs.hubspot.com/docs/methods/oauth2/oauth2-quickstart\\">Hubspot docs</a> if you need help finding this ID."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The client secret for your HubSpot developer application. See the <a href=\\"https://legacydocs.hubspot.com/docs/methods/oauth2/oauth2-quickstart\\">Hubspot docs</a> if you need help finding this secret."""
    credentials_title: SourceHubspotCredentialsOAuthCredentialsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title') }})
    r"""Name of the credentials"""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Refresh token to renew an expired access token. See the <a href=\\"https://legacydocs.hubspot.com/docs/methods/oauth2/oauth2-quickstart\\">Hubspot docs</a> if you need help finding this token."""
    
class SourceHubspotHubspotEnum(str, Enum):
    HUBSPOT = 'hubspot'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceHubspot:
    r"""The values required to configure the source."""
    
    credentials: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    r"""Choose how to authenticate to HubSpot."""
    source_type: SourceHubspotHubspotEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    