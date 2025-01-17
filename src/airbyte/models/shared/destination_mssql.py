"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationMssqlMssqlEnum(str, Enum):
    MSSQL = 'mssql'

class DestinationMssqlSslMethodEncryptedVerifyCertificateSslMethodEnum(str, Enum):
    ENCRYPTED_VERIFY_CERTIFICATE = 'encrypted_verify_certificate'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssqlSslMethodEncryptedVerifyCertificate:
    r"""Verify and use the certificate provided by the server."""
    
    ssl_method: DestinationMssqlSslMethodEncryptedVerifyCertificateSslMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method') }})
    host_name_in_certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostNameInCertificate'), 'exclude': lambda f: f is None }})
    r"""Specifies the host name of the server. The value of this property must match the subject property of the certificate."""
    
class DestinationMssqlSslMethodEncryptedTrustServerCertificateSslMethodEnum(str, Enum):
    ENCRYPTED_TRUST_SERVER_CERTIFICATE = 'encrypted_trust_server_certificate'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssqlSslMethodEncryptedTrustServerCertificate:
    r"""Use the certificate provided by the server without verification. (For testing purposes only!)"""
    
    ssl_method: DestinationMssqlSslMethodEncryptedTrustServerCertificateSslMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method') }})
    
class DestinationMssqlTunnelMethodPasswordAuthenticationTunnelMethodEnum(str, Enum):
    r"""Connect through a jump server tunnel host using username and password authentication"""
    SSH_PASSWORD_AUTH = 'SSH_PASSWORD_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssqlTunnelMethodPasswordAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_method: DestinationMssqlTunnelMethodPasswordAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    
class DestinationMssqlTunnelMethodSSHKeyAuthenticationTunnelMethodEnum(str, Enum):
    r"""Connect through a jump server tunnel host using username and ssh key"""
    SSH_KEY_AUTH = 'SSH_KEY_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssqlTunnelMethodSSHKeyAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_method: DestinationMssqlTunnelMethodSSHKeyAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    
class DestinationMssqlTunnelMethodNoTunnelTunnelMethodEnum(str, Enum):
    r"""No ssh tunnel needed to connect to database"""
    NO_TUNNEL = 'NO_TUNNEL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssqlTunnelMethodNoTunnel:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    tunnel_method: DestinationMssqlTunnelMethodNoTunnelTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMssql:
    r"""The values required to configure the destination."""
    
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""The name of the MSSQL database."""
    destination_type: DestinationMssqlMssqlEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The host name of the MSSQL database."""
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    r"""The port of the MSSQL database."""
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    r"""The default schema tables are written to if the source does not specify a namespace. The usual value for this field is \\"public\\"."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""The username which is used to access the database."""
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3)."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""The password associated with this username."""
    ssl_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method'), 'exclude': lambda f: f is None }})
    r"""The encryption method which is used to communicate with the database."""
    tunnel_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    