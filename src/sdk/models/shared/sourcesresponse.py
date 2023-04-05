"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import sourceresponse as shared_sourceresponse
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcesResponse:
    r"""Successful operation"""
    
    data: list[shared_sourceresponse.SourceResponse] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})  
    next: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next') }})  
    previous: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous') }})  
    