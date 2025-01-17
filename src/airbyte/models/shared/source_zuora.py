"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceZuoraDataQueryTypeEnum(str, Enum):
    r"""Choose between `Live`, or `Unlimited` - the optimized, replicated database at 12 hours freshness for high volume extraction <a href=\\"https://knowledgecenter.zuora.com/Central_Platform/Query/Data_Query/A_Overview_of_Data_Query#Query_Processing_Limitations\\">Link</a>"""
    LIVE = 'Live'
    UNLIMITED = 'Unlimited'

class SourceZuoraZuoraEnum(str, Enum):
    ZUORA = 'zuora'

class SourceZuoraTenantEndpointLocationEnum(str, Enum):
    r"""Please choose the right endpoint where your Tenant is located. More info by this <a href=\\"https://www.zuora.com/developer/api-reference/#section/Introduction/Access-to-the-API\\">Link</a>"""
    US_PRODUCTION = 'US Production'
    US_CLOUD_PRODUCTION = 'US Cloud Production'
    US_API_SANDBOX = 'US API Sandbox'
    US_CLOUD_API_SANDBOX = 'US Cloud API Sandbox'
    US_CENTRAL_SANDBOX = 'US Central Sandbox'
    US_PERFORMANCE_TEST = 'US Performance Test'
    EU_PRODUCTION = 'EU Production'
    EU_API_SANDBOX = 'EU API Sandbox'
    EU_CENTRAL_SANDBOX = 'EU Central Sandbox'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZuora:
    r"""The values required to configure the source."""
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""Your OAuth user Client ID"""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Your OAuth user Client Secret"""
    data_query: SourceZuoraDataQueryTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_query') }})
    r"""Choose between `Live`, or `Unlimited` - the optimized, replicated database at 12 hours freshness for high volume extraction <a href=\\"https://knowledgecenter.zuora.com/Central_Platform/Query/Data_Query/A_Overview_of_Data_Query#Query_Processing_Limitations\\">Link</a>"""
    source_type: SourceZuoraZuoraEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""Start Date in format: YYYY-MM-DD"""
    tenant_endpoint: SourceZuoraTenantEndpointLocationEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tenant_endpoint') }})
    r"""Please choose the right endpoint where your Tenant is located. More info by this <a href=\\"https://www.zuora.com/developer/api-reference/#section/Introduction/Access-to-the-API\\">Link</a>"""
    window_in_days: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('window_in_days'), 'exclude': lambda f: f is None }})
    r"""The amount of days for each data-chunk begining from start_date. Bigger the value - faster the fetch. (0.1 - as for couple of hours, 1 - as for a Day; 364 - as for a Year)."""
    