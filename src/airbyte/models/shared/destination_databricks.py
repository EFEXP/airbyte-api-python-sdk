"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationDatabricksDataSourceAzureBlobStorageDataSourceTypeEnum(str, Enum):
    AZURE_BLOB_STORAGE = 'AZURE_BLOB_STORAGE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationDatabricksDataSourceAzureBlobStorage:
    r"""Storage on which the delta lake is built."""
    
    azure_blob_storage_account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_name') }})
    r"""The account's name of the Azure Blob Storage."""
    azure_blob_storage_container_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_container_name') }})
    r"""The name of the Azure blob storage container."""
    azure_blob_storage_sas_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_sas_token') }})
    r"""Shared access signature (SAS) token to grant limited access to objects in your storage account."""
    data_source_type: DestinationDatabricksDataSourceAzureBlobStorageDataSourceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_source_type') }})
    azure_blob_storage_endpoint_domain_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_endpoint_domain_name'), 'exclude': lambda f: f is None }})
    r"""This is Azure Blob Storage endpoint domain name. Leave default value (or leave it empty if run container from command line) to use Microsoft native from example."""
    
class DestinationDatabricksDataSourceAmazonS3DataSourceTypeEnum(str, Enum):
    S3_STORAGE = 'S3_STORAGE'

class DestinationDatabricksDataSourceAmazonS3S3BucketRegionEnum(str, Enum):
    r"""The region of the S3 staging bucket to use if utilising a copy strategy."""
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
    US_GOV_EAST_1 = 'us-gov-east-1'
    US_GOV_WEST_1 = 'us-gov-west-1'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationDatabricksDataSourceAmazonS3:
    r"""Storage on which the delta lake is built."""
    
    data_source_type: DestinationDatabricksDataSourceAmazonS3DataSourceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_source_type') }})
    s3_access_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_access_key_id') }})
    r"""The Access Key Id granting allow one to access the above S3 staging bucket. Airbyte requires Read and Write permissions to the given bucket."""
    s3_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_name') }})
    r"""The name of the S3 bucket to use for intermittent staging of the data."""
    s3_bucket_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_path') }})
    r"""The directory under the S3 bucket where data will be written."""
    s3_bucket_region: DestinationDatabricksDataSourceAmazonS3S3BucketRegionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_region') }})
    r"""The region of the S3 staging bucket to use if utilising a copy strategy."""
    s3_secret_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_secret_access_key') }})
    r"""The corresponding secret to the above access key id."""
    file_name_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name_pattern'), 'exclude': lambda f: f is None }})
    r"""The pattern allows you to set the file-name format for the S3 staging file(s)"""
    
class DestinationDatabricksDataSourceRecommendedManagedTablesDataSourceTypeEnum(str, Enum):
    MANAGED_TABLES_STORAGE = 'MANAGED_TABLES_STORAGE'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationDatabricksDataSourceRecommendedManagedTables:
    r"""Storage on which the delta lake is built."""
    
    data_source_type: DestinationDatabricksDataSourceRecommendedManagedTablesDataSourceTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_source_type') }})
    
class DestinationDatabricksDatabricksEnum(str, Enum):
    DATABRICKS = 'databricks'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationDatabricks:
    r"""The values required to configure the destination."""
    
    accept_terms: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accept_terms') }})
    r"""You must agree to the Databricks JDBC Driver <a href=\\"https://databricks.com/jdbc-odbc-driver-license\\">Terms & Conditions</a> to use this connector."""
    data_source: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_source') }})
    r"""Storage on which the delta lake is built."""
    databricks_http_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_http_path') }})
    r"""Databricks Cluster HTTP Path."""
    databricks_personal_access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_personal_access_token') }})
    r"""Databricks Personal Access Token for making authenticated requests."""
    databricks_server_hostname: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_server_hostname') }})
    r"""Databricks Cluster Server Hostname."""
    destination_type: DestinationDatabricksDatabricksEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    database: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database'), 'exclude': lambda f: f is None }})
    r"""The name of the catalog. If not specified otherwise, the \\"hive_metastore\\" will be used."""
    databricks_port: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('databricks_port'), 'exclude': lambda f: f is None }})
    r"""Databricks Cluster Port."""
    purge_staging_data: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purge_staging_data'), 'exclude': lambda f: f is None }})
    r"""Default to 'true'. Switch it to 'false' for debugging purpose."""
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""The default schema tables are written. If not specified otherwise, the \\"default\\" will be used."""
    