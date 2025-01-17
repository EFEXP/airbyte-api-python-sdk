"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connectionresponse as shared_connectionresponse
from typing import Optional


@dataclasses.dataclass
class CreateConnectionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connection_response: Optional[shared_connectionresponse.ConnectionResponse] = dataclasses.field(default=None)
    r"""Successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    