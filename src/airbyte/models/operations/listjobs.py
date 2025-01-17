"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import jobsresponse as shared_jobsresponse
from ..shared import jobtypeenum_enum as shared_jobtypeenum_enum
from typing import Optional


@dataclasses.dataclass
class ListJobsRequest:
    
    connection_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'connectionId', 'style': 'form', 'explode': True }})
    r"""Filter the Jobs by connectionId."""
    job_type: Optional[shared_jobtypeenum_enum.JobTypeEnumEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'jobType', 'style': 'form', 'explode': True }})
    r"""Filter the Jobs by jobType."""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Set the limit on the number of Jobs returned. The default is 20 Jobs."""
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Set the offset to start at when returning Jobs. The default is 0."""
    

@dataclasses.dataclass
class ListJobsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    jobs_response: Optional[shared_jobsresponse.JobsResponse] = dataclasses.field(default=None)
    r"""List all the Jobs by connectionId."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    