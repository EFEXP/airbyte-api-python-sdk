"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields

class SourceChartmogulIntervalEnum(str, Enum):
    r"""Some APIs such as <a href=\\"https://dev.chartmogul.com/reference/endpoint-overview-metrics-api\\">Metrics</a> require intervals to cluster data."""
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    QUARTER = 'quarter'

class SourceChartmogulChartmogulEnum(str, Enum):
    CHARTMOGUL = 'chartmogul'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceChartmogul:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Your Chartmogul API key. See <a href=\\"https://help.chartmogul.com/hc/en-us/articles/4407796325906-Creating-and-Managing-API-keys#creating-an-api-key\\"> the docs </a> for info on how to obtain this."""  
    interval: SourceChartmogulIntervalEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('interval') }})
    r"""Some APIs such as <a href=\\"https://dev.chartmogul.com/reference/endpoint-overview-metrics-api\\">Metrics</a> require intervals to cluster data."""  
    source_type: SourceChartmogulChartmogulEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. When feasible, any data before this date will not be replicated."""  
    