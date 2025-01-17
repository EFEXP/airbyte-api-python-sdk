"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationElasticsearchAuthenticationMethodUsernamePasswordMethodEnum(str, Enum):
    BASIC = 'basic'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationElasticsearchAuthenticationMethodUsernamePassword:
    r"""Basic auth header with a username and password"""
    
    method: DestinationElasticsearchAuthenticationMethodUsernamePasswordMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Basic auth password to access a secure Elasticsearch server"""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Basic auth username to access a secure Elasticsearch server"""
    
class DestinationElasticsearchAuthenticationMethodAPIKeySecretMethodEnum(str, Enum):
    SECRET = 'secret'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationElasticsearchAuthenticationMethodAPIKeySecret:
    r"""Use a api key and secret combination to authenticate"""
    
    api_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiKeyId') }})
    r"""The Key ID to used when accessing an enterprise Elasticsearch instance."""
    api_key_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiKeySecret') }})
    r"""The secret associated with the API Key ID."""
    method: DestinationElasticsearchAuthenticationMethodAPIKeySecretMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    
class DestinationElasticsearchElasticsearchEnum(str, Enum):
    ELASTICSEARCH = 'elasticsearch'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationElasticsearch:
    r"""The values required to configure the destination."""
    
    destination_type: DestinationElasticsearchElasticsearchEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    endpoint: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint') }})
    r"""The full url of the Elasticsearch server"""
    authentication_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authenticationMethod'), 'exclude': lambda f: f is None }})
    r"""The type of authentication to be used"""
    ca_certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate'), 'exclude': lambda f: f is None }})
    r"""CA certificate"""
    upsert: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upsert'), 'exclude': lambda f: f is None }})
    r"""If a primary key identifier is defined in the source, an upsert will be performed using the primary key value as the elasticsearch doc id. Does not support composite primary keys."""
    