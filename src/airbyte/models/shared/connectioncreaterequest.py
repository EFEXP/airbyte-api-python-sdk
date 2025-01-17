"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import connectionschedulecreate as shared_connectionschedulecreate
from ..shared import geographyenum_enum as shared_geographyenum_enum
from ..shared import namespacedefinitionenum_enum as shared_namespacedefinitionenum_enum
from ..shared import nonbreakingschemaupdatesbehaviorenum_enum as shared_nonbreakingschemaupdatesbehaviorenum_enum
from ..shared import streamconfigurations as shared_streamconfigurations
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionCreateRequest:
    
    destination_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationId') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    configurations: Optional[shared_streamconfigurations.StreamConfigurations] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configurations'), 'exclude': lambda f: f is None }})
    r"""A list of configured stream options for a connection."""
    data_residency: Optional[shared_geographyenum_enum.GeographyEnumEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataResidency'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Optional name of the connection"""
    namespace_definition: Optional[shared_namespacedefinitionenum_enum.NamespaceDefinitionEnumEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceDefinition'), 'exclude': lambda f: f is None }})
    r"""Define the location where the data will be stored in the destination"""
    namespace_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceFormat'), 'exclude': lambda f: f is None }})
    r"""Used when namespaceDefinition is 'custom_format'. If blank then behaves like namespaceDefinition = 'destination'. If \\"${SOURCE_NAMESPACE}\\" then behaves like namespaceDefinition = 'source'."""
    non_breaking_schema_updates_behavior: Optional[shared_nonbreakingschemaupdatesbehaviorenum_enum.NonBreakingSchemaUpdatesBehaviorEnumEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nonBreakingSchemaUpdatesBehavior'), 'exclude': lambda f: f is None }})
    r"""Set how Airbyte handles syncs when it detects a non-breaking schema change in the source"""
    prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prefix'), 'exclude': lambda f: f is None }})
    r"""Prefix that will be prepended to the name of each stream when it is written to the destination (ex. “airbyte_” causes “projects” => “airbyte_projects”)."""
    schedule: Optional[shared_connectionschedulecreate.ConnectionScheduleCreate] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule'), 'exclude': lambda f: f is None }})
    r"""schedule for when the the connection should run, per the schedule type"""
    