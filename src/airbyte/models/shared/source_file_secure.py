"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceFileSecureFileFormatEnum(str, Enum):
    r"""The Format of the file which should be replicated (Warning: some formats may be experimental, please refer to the docs)."""
    CSV = 'csv'
    JSON = 'json'
    JSONL = 'jsonl'
    EXCEL = 'excel'
    EXCEL_BINARY = 'excel_binary'
    FEATHER = 'feather'
    PARQUET = 'parquet'
    YAML = 'yaml'

class SourceFileSecureProviderSFTPSecureFileTransferProtocolStorageEnum(str, Enum):
    SFTP = 'SFTP'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderSFTPSecureFileTransferProtocol:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    storage: SourceFileSecureProviderSFTPSecureFileTransferProtocolStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    port: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    
class SourceFileSecureProviderSCPSecureCopyProtocolStorageEnum(str, Enum):
    SCP = 'SCP'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderSCPSecureCopyProtocol:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    storage: SourceFileSecureProviderSCPSecureCopyProtocolStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    port: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    
class SourceFileSecureProviderSSHSecureShellStorageEnum(str, Enum):
    SSH = 'SSH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderSSHSecureShell:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    storage: SourceFileSecureProviderSSHSecureShellStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    port: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    
class SourceFileSecureProviderAzBlobAzureBlobStorageStorageEnum(str, Enum):
    AZ_BLOB = 'AzBlob'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderAzBlobAzureBlobStorage:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    
    storage: SourceFileSecureProviderAzBlobAzureBlobStorageStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    storage_account: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_account') }})
    r"""The globally unique name of the storage account that the desired blob sits within. See <a href=\\"https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview\\" target=\\"_blank\\">here</a> for more details."""
    sas_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sas_token'), 'exclude': lambda f: f is None }})
    r"""To access Azure Blob Storage, this connector would need credentials with the proper permissions. One option is a SAS (Shared Access Signature) token. If accessing publicly available data, this field is not necessary."""
    shared_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shared_key'), 'exclude': lambda f: f is None }})
    r"""To access Azure Blob Storage, this connector would need credentials with the proper permissions. One option is a storage account shared key (aka account key or access key). If accessing publicly available data, this field is not necessary."""
    
class SourceFileSecureProviderS3AmazonWebServicesStorageEnum(str, Enum):
    S3 = 'S3'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderS3AmazonWebServices:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    
    storage: SourceFileSecureProviderS3AmazonWebServicesStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    aws_access_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_access_key_id'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on AWS S3, this connector would need credentials with the proper permissions. If accessing publicly available data, this field is not necessary."""
    aws_secret_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_secret_access_key'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on AWS S3, this connector would need credentials with the proper permissions. If accessing publicly available data, this field is not necessary."""
    
class SourceFileSecureProviderGCSGoogleCloudStorageStorageEnum(str, Enum):
    GCS = 'GCS'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderGCSGoogleCloudStorage:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    
    storage: SourceFileSecureProviderGCSGoogleCloudStorageStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    service_account_json: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_account_json'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on Google Cloud, this connector would need a service account json credentials with the proper permissions as described <a href=\\"https://cloud.google.com/iam/docs/service-accounts\\" target=\\"_blank\\">here</a>. Please generate the credentials.json file and copy/paste its content to this field (expecting JSON formats). If accessing publicly available data, this field is not necessary."""
    
class SourceFileSecureProviderHTTPSPublicWebStorageEnum(str, Enum):
    HTTPS = 'HTTPS'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecureProviderHTTPSPublicWeb:
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    
    storage: SourceFileSecureProviderHTTPSPublicWebStorageEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage') }})
    user_agent: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_agent'), 'exclude': lambda f: f is None }})
    r"""Add User-Agent to request"""
    
class SourceFileSecureFileSecureEnum(str, Enum):
    FILE_SECURE = 'file-secure'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFileSecure:
    r"""The values required to configure the source."""
    
    dataset_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_name') }})
    r"""The Name of the final table to replicate this file into (should include letters, numbers dash and underscores only)."""
    format: SourceFileSecureFileFormatEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    r"""The Format of the file which should be replicated (Warning: some formats may be experimental, please refer to the docs)."""
    provider: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    r"""The storage Provider or Location of the file(s) which should be replicated."""
    source_type: SourceFileSecureFileSecureEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""The URL path to access the file which should be replicated."""
    reader_options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reader_options'), 'exclude': lambda f: f is None }})
    r"""This should be a string in JSON format. It depends on the chosen file format to provide additional options and tune its behavior."""
    