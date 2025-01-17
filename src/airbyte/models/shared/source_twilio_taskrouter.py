"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceTwilioTaskrouterTwilioTaskrouterEnum(str, Enum):
    TWILIO_TASKROUTER = 'twilio-taskrouter'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTwilioTaskrouter:
    r"""The values required to configure the source."""
    
    account_sid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_sid') }})
    r"""Twilio Account ID"""
    auth_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_token') }})
    r"""Twilio Auth Token"""
    source_type: SourceTwilioTaskrouterTwilioTaskrouterEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    