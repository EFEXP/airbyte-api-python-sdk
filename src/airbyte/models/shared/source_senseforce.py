"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceSenseforceSenseforceEnum(str, Enum):
    SENSEFORCE = 'senseforce'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSenseforce:
    r"""The values required to configure the source."""
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Your API access token. See <a href=\\"https://manual.senseforce.io/manual/sf-platform/public-api/get-your-access-token/\\">here</a>. The toke is case sensitive."""
    backend_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('backend_url') }})
    r"""Your Senseforce API backend URL. This is the URL shown during the Login screen. See <a href=\\"https://manual.senseforce.io/manual/sf-platform/public-api/get-your-access-token/\\">here</a> for more details. (Note: Most Senseforce backend APIs have the term 'galaxy' in their ULR)"""
    dataset_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_id') }})
    r"""The ID of the dataset you want to synchronize. The ID can be found in the URL when opening the dataset. See <a href=\\"https://manual.senseforce.io/manual/sf-platform/public-api/get-your-access-token/\\">here</a> for more details. (Note: As the Senseforce API only allows to synchronize a specific dataset, each dataset you  want to synchronize needs to be implemented as a separate airbyte source)."""
    source_type: SourceSenseforceSenseforceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    r"""UTC date and time in the format 2017-01-25. Only data with \\"Timestamp\\" after this date will be replicated. Important note: This start date must be set to the first day of where your dataset provides data.  If your dataset has data from 2020-10-10 10:21:10, set the start_date to 2020-10-10 or later"""
    slice_range: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slice_range'), 'exclude': lambda f: f is None }})
    r"""The time increment used by the connector when requesting data from the Senseforce API. The bigger the value is, the less requests will be made and faster the sync will be. On the other hand, the more seldom the state is persisted and the more likely one could run into rate limites.  Furthermore, consider that large chunks of time might take a long time for the Senseforce query to return data - meaning it could take in effect longer than with more smaller time slices. If there are a lot of data per day, set this setting to 1. If there is only very little data per day, you might change the setting to 10 or more."""
    