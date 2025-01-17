"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceDockerhubDockerhubEnum(str, Enum):
    DOCKERHUB = 'dockerhub'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDockerhub:
    r"""The values required to configure the source."""
    
    docker_username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('docker_username') }})
    r"""Username of DockerHub person or organization (for https://hub.docker.com/v2/repositories/USERNAME/ API call)"""
    source_type: SourceDockerhubDockerhubEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    