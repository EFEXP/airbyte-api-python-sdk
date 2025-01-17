"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceOracleConnectionDataSystemIDSIDConnectionTypeEnum(str, Enum):
    SID = 'sid'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleConnectionDataSystemIDSID:
    r"""Use SID (Oracle System Identifier)"""
    
    sid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sid') }})
    connection_type: Optional[SourceOracleConnectionDataSystemIDSIDConnectionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connection_type'), 'exclude': lambda f: f is None }})
    
class SourceOracleConnectionDataServiceNameConnectionTypeEnum(str, Enum):
    SERVICE_NAME = 'service_name'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleConnectionDataServiceName:
    r"""Use service name"""
    
    service_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_name') }})
    connection_type: Optional[SourceOracleConnectionDataServiceNameConnectionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connection_type'), 'exclude': lambda f: f is None }})
    
class SourceOracleEncryptionTLSEncryptedVerifyCertificateEncryptionMethodEnum(str, Enum):
    ENCRYPTED_VERIFY_CERTIFICATE = 'encrypted_verify_certificate'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleEncryptionTLSEncryptedVerifyCertificate:
    r"""Verify and use the certificate provided by the server."""
    
    encryption_method: SourceOracleEncryptionTLSEncryptedVerifyCertificateEncryptionMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_method') }})
    ssl_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_certificate') }})
    r"""Privacy Enhanced Mail (PEM) files are concatenated certificate containers frequently used in certificate installations."""
    
class SourceOracleEncryptionNativeNetworkEncryptionNNEEncryptionAlgorithmEnum(str, Enum):
    r"""This parameter defines what encryption algorithm is used."""
    AES256 = 'AES256'
    RC4_56 = 'RC4_56'
    THREE_DES168 = '3DES168'

class SourceOracleEncryptionNativeNetworkEncryptionNNEEncryptionMethodEnum(str, Enum):
    CLIENT_NNE = 'client_nne'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleEncryptionNativeNetworkEncryptionNNE:
    r"""The native network encryption gives you the ability to encrypt database connections, without the configuration overhead of TCP/IP and SSL/TLS and without the need to open and listen on different ports."""
    
    encryption_method: SourceOracleEncryptionNativeNetworkEncryptionNNEEncryptionMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_method') }})
    encryption_algorithm: Optional[SourceOracleEncryptionNativeNetworkEncryptionNNEEncryptionAlgorithmEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_algorithm'), 'exclude': lambda f: f is None }})
    r"""This parameter defines what encryption algorithm is used."""
    
class SourceOracleOracleEnum(str, Enum):
    ORACLE = 'oracle'

class SourceOracleTunnelMethodPasswordAuthenticationTunnelMethodEnum(str, Enum):
    r"""Connect through a jump server tunnel host using username and password authentication"""
    SSH_PASSWORD_AUTH = 'SSH_PASSWORD_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleTunnelMethodPasswordAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_method: SourceOracleTunnelMethodPasswordAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    
class SourceOracleTunnelMethodSSHKeyAuthenticationTunnelMethodEnum(str, Enum):
    r"""Connect through a jump server tunnel host using username and ssh key"""
    SSH_KEY_AUTH = 'SSH_KEY_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleTunnelMethodSSHKeyAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_method: SourceOracleTunnelMethodSSHKeyAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    
class SourceOracleTunnelMethodNoTunnelTunnelMethodEnum(str, Enum):
    r"""No ssh tunnel needed to connect to database"""
    NO_TUNNEL = 'NO_TUNNEL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracleTunnelMethodNoTunnel:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    tunnel_method: SourceOracleTunnelMethodNoTunnelTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOracle:
    r"""The values required to configure the source."""
    
    encryption: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption') }})
    r"""The encryption method with is used when communicating with the database."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Hostname of the database."""
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    r"""Port of the database.
    Oracle Corporations recommends the following port numbers:
    1521 - Default listening port for client connections to the listener. 
    2484 - Recommended and officially registered listening port for client connections to the listener using TCP/IP with SSL
    """
    source_type: SourceOracleOracleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""The username which is used to access the database."""
    connection_data: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connection_data'), 'exclude': lambda f: f is None }})
    r"""Connect data that will be used for DB connection"""
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3)."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""The password associated with the username."""
    schemas: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemas'), 'exclude': lambda f: f is None }})
    r"""The list of schemas to sync from. Defaults to user. Case sensitive."""
    tunnel_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    