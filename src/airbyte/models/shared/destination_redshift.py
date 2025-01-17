"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationRedshiftRedshiftEnum(str, Enum):
    REDSHIFT = 'redshift'

class DestinationRedshiftTunnelMethodPasswordAuthenticationTunnelMethodEnum(str, Enum):
    r"""Connect through a jump server tunnel host using username and password authentication"""
    SSH_PASSWORD_AUTH = 'SSH_PASSWORD_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshiftTunnelMethodPasswordAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_method: DestinationRedshiftTunnelMethodPasswordAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    
class DestinationRedshiftTunnelMethodSSHKeyAuthenticationTunnelMethodEnum(str, Enum):
    r"""Connect through a jump server tunnel host using username and ssh key"""
    SSH_KEY_AUTH = 'SSH_KEY_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshiftTunnelMethodSSHKeyAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_method: DestinationRedshiftTunnelMethodSSHKeyAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    
class DestinationRedshiftTunnelMethodNoTunnelTunnelMethodEnum(str, Enum):
    r"""No ssh tunnel needed to connect to database"""
    NO_TUNNEL = 'NO_TUNNEL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshiftTunnelMethodNoTunnel:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    tunnel_method: DestinationRedshiftTunnelMethodNoTunnelTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    
class DestinationRedshiftUploadingMethodS3StagingEncryptionAESCBCEnvelopeEncryptionEncryptionTypeEnum(str, Enum):
    AES_CBC_ENVELOPE = 'aes_cbc_envelope'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshiftUploadingMethodS3StagingEncryptionAESCBCEnvelopeEncryption:
    r"""Staging data will be encrypted using AES-CBC envelope encryption."""
    
    encryption_type: DestinationRedshiftUploadingMethodS3StagingEncryptionAESCBCEnvelopeEncryptionEncryptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_type') }})
    key_encrypting_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key_encrypting_key'), 'exclude': lambda f: f is None }})
    r"""The key, base64-encoded. Must be either 128, 192, or 256 bits. Leave blank to have Airbyte generate an ephemeral key for each sync."""
    
class DestinationRedshiftUploadingMethodS3StagingEncryptionNoEncryptionEncryptionTypeEnum(str, Enum):
    NONE = 'none'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshiftUploadingMethodS3StagingEncryptionNoEncryption:
    r"""Staging data will be stored in plaintext."""
    
    encryption_type: DestinationRedshiftUploadingMethodS3StagingEncryptionNoEncryptionEncryptionTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_type') }})
    
class DestinationRedshiftUploadingMethodS3StagingMethodEnum(str, Enum):
    S3_STAGING = 'S3 Staging'

class DestinationRedshiftUploadingMethodS3StagingS3BucketRegionEnum(str, Enum):
    r"""The region of the S3 staging bucket to use if utilising a COPY strategy. See <a href=\\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html#:~:text=In-,Region,-%2C%20choose%20the%20AWS\\">AWS docs</a> for details."""
    UNKNOWN = ''
    US_EAST_1 = 'us-east-1'
    US_EAST_2 = 'us-east-2'
    US_WEST_1 = 'us-west-1'
    US_WEST_2 = 'us-west-2'
    AF_SOUTH_1 = 'af-south-1'
    AP_EAST_1 = 'ap-east-1'
    AP_SOUTH_1 = 'ap-south-1'
    AP_NORTHEAST_1 = 'ap-northeast-1'
    AP_NORTHEAST_2 = 'ap-northeast-2'
    AP_NORTHEAST_3 = 'ap-northeast-3'
    AP_SOUTHEAST_1 = 'ap-southeast-1'
    AP_SOUTHEAST_2 = 'ap-southeast-2'
    CA_CENTRAL_1 = 'ca-central-1'
    CN_NORTH_1 = 'cn-north-1'
    CN_NORTHWEST_1 = 'cn-northwest-1'
    EU_CENTRAL_1 = 'eu-central-1'
    EU_NORTH_1 = 'eu-north-1'
    EU_SOUTH_1 = 'eu-south-1'
    EU_WEST_1 = 'eu-west-1'
    EU_WEST_2 = 'eu-west-2'
    EU_WEST_3 = 'eu-west-3'
    SA_EAST_1 = 'sa-east-1'
    ME_SOUTH_1 = 'me-south-1'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshiftUploadingMethodS3Staging:
    r"""The method how the data will be uploaded to the database."""
    
    access_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key_id') }})
    r"""This ID grants access to the above S3 staging bucket. Airbyte requires Read and Write permissions to the given bucket. See <a href=\\"https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys\\">AWS docs</a> on how to generate an access key ID and secret access key."""
    method: DestinationRedshiftUploadingMethodS3StagingMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    s3_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_name') }})
    r"""The name of the staging S3 bucket to use if utilising a COPY strategy. COPY is recommended for production workloads for better speed and scalability. See <a href=\\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html\\">AWS docs</a> for more details."""
    s3_bucket_region: DestinationRedshiftUploadingMethodS3StagingS3BucketRegionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_region') }})
    r"""The region of the S3 staging bucket to use if utilising a COPY strategy. See <a href=\\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html#:~:text=In-,Region,-%2C%20choose%20the%20AWS\\">AWS docs</a> for details."""
    secret_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_access_key') }})
    r"""The corresponding secret to the above access key id. See <a href=\\"https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys\\">AWS docs</a> on how to generate an access key ID and secret access key."""
    encryption: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption'), 'exclude': lambda f: f is None }})
    r"""How to encrypt the staging data"""
    file_buffer_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_buffer_count'), 'exclude': lambda f: f is None }})
    r"""Number of file buffers allocated for writing data. Increasing this number is beneficial for connections using Change Data Capture (CDC) and up to the number of streams within a connection. Increasing the number of file buffers past the maximum number of streams has deteriorating effects"""
    file_name_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name_pattern'), 'exclude': lambda f: f is None }})
    r"""The pattern allows you to set the file-name format for the S3 staging file(s)"""
    purge_staging_data: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purge_staging_data'), 'exclude': lambda f: f is None }})
    r"""Whether to delete the staging files from S3 after completing the sync. See <a href=\\"https://docs.airbyte.com/integrations/destinations/redshift/#:~:text=the%20root%20directory.-,Purge%20Staging%20Data,-Whether%20to%20delete\\"> docs</a> for details."""
    s3_bucket_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_path'), 'exclude': lambda f: f is None }})
    r"""The directory under the S3 bucket where data will be written. If not provided, then defaults to the root directory. See <a href=\\"https://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/faq.html#:~:text=be%20globally%20unique.-,For%20S3%20bucket%20paths,-%2C%20you%20can%20use\\">path's name recommendations</a> for more details."""
    
class DestinationRedshiftUploadingMethodStandardMethodEnum(str, Enum):
    STANDARD = 'Standard'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshiftUploadingMethodStandard:
    r"""The method how the data will be uploaded to the database."""
    
    method: DestinationRedshiftUploadingMethodStandardMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshift:
    r"""The values required to configure the destination."""
    
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Name of the database."""
    destination_type: DestinationRedshiftRedshiftEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Host Endpoint of the Redshift Cluster (must include the cluster-id, region and end with .redshift.amazonaws.com)"""
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Password associated with the username."""
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    r"""Port of the database."""
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    r"""The default schema tables are written to if the source does not specify a namespace. Unless specifically configured, the usual value for this field is \\"public\\"."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username to use to access the database."""
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3)."""
    tunnel_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    uploading_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uploading_method'), 'exclude': lambda f: f is None }})
    r"""The method how the data will be uploaded to the database."""
    