"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connectionresponse as shared_connectionresponse
from typing import Optional


@dataclasses.dataclass
class GetConnectionRequest:
    
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetConnectionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connection_response: Optional[shared_connectionresponse.ConnectionResponse] = dataclasses.field(default=None)
    r"""Get a Connection by the id in the path."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    