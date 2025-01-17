"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class DestinationFirestoreFirestoreEnum(str, Enum):
    FIRESTORE = 'firestore'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationFirestore:
    r"""The values required to configure the destination."""
    
    destination_type: DestinationFirestoreFirestoreEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    r"""The GCP project ID for the project containing the target BigQuery dataset."""
    credentials_json: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json'), 'exclude': lambda f: f is None }})
    r"""The contents of the JSON service account key. Check out the <a href=\\"https://docs.airbyte.io/integrations/destinations/firestore\\">docs</a> if you need help generating this key. Default credentials will be used if this field is left empty."""
    