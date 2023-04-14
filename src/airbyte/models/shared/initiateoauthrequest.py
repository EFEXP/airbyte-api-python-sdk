"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InitiateOauthRequest:
    r"""POST body for initiating OAuth via the public API"""
    
    redirect_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('redirectUrl') }})
    r"""The URL to redirect the user to with the OAuth secret stored in the secret_id query string parameter after authentication is complete."""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The name of the source to authenticate to"""  
    o_auth_input_configuration: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oAuthInputConfiguration'), 'exclude': lambda f: f is None }})
    r"""Arbitrary vars to pass for OAuth depending on what the source/destination spec requires."""  
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId'), 'exclude': lambda f: f is None }})
    r"""The workspace to create the secret and eventually the full source."""  
    