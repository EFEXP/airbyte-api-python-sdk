"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationMongodbAuthTypeLoginPasswordAuthorizationEnum(str, Enum):
    LOGIN_PASSWORD = 'login/password'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbAuthTypeLoginPassword:
    r"""Login/Password."""
    
    authorization: DestinationMongodbAuthTypeLoginPasswordAuthorizationEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization') }})
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Password associated with the username."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username to use to access the database."""
    
class DestinationMongodbAuthTypeNoneAuthorizationEnum(str, Enum):
    NONE = 'none'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbAuthTypeNone:
    r"""None."""
    
    authorization: DestinationMongodbAuthTypeNoneAuthorizationEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization') }})
    
class DestinationMongodbMongodbEnum(str, Enum):
    MONGODB = 'mongodb'

class DestinationMongodbInstanceTypeMongoDBAtlasInstanceEnum(str, Enum):
    ATLAS = 'atlas'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbInstanceTypeMongoDBAtlas:
    r"""MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    
    cluster_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cluster_url') }})
    r"""URL of a cluster to connect to."""
    instance: DestinationMongodbInstanceTypeMongoDBAtlasInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    
class DestinationMongodbInstanceTypeReplicaSetInstanceEnum(str, Enum):
    REPLICA = 'replica'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbInstanceTypeReplicaSet:
    r"""MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    
    instance: DestinationMongodbInstanceTypeReplicaSetInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    server_addresses: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('server_addresses') }})
    r"""The members of a replica set. Please specify `host`:`port` of each member seperated by comma."""
    replica_set: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replica_set'), 'exclude': lambda f: f is None }})
    r"""A replica set name."""
    
class DestinationMongodbInstanceTypeStandaloneMongoDbInstanceInstanceEnum(str, Enum):
    STANDALONE = 'standalone'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbInstanceTypeStandaloneMongoDbInstance:
    r"""MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The Host of a Mongo database to be replicated."""
    instance: DestinationMongodbInstanceTypeStandaloneMongoDbInstanceInstanceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance') }})
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    r"""The Port of a Mongo database to be replicated."""
    
class DestinationMongodbTunnelMethodPasswordAuthenticationTunnelMethodEnum(str, Enum):
    r"""Connect through a jump server tunnel host using username and password authentication"""
    SSH_PASSWORD_AUTH = 'SSH_PASSWORD_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbTunnelMethodPasswordAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_method: DestinationMongodbTunnelMethodPasswordAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    
class DestinationMongodbTunnelMethodSSHKeyAuthenticationTunnelMethodEnum(str, Enum):
    r"""Connect through a jump server tunnel host using username and ssh key"""
    SSH_KEY_AUTH = 'SSH_KEY_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbTunnelMethodSSHKeyAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_method: DestinationMongodbTunnelMethodSSHKeyAuthenticationTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port') }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    
class DestinationMongodbTunnelMethodNoTunnelTunnelMethodEnum(str, Enum):
    r"""No ssh tunnel needed to connect to database"""
    NO_TUNNEL = 'NO_TUNNEL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbTunnelMethodNoTunnel:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    
    tunnel_method: DestinationMongodbTunnelMethodNoTunnelTunnelMethodEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodb:
    r"""The values required to configure the destination."""
    
    auth_type: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    r"""Authorization type."""
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Name of the database."""
    destination_type: DestinationMongodbMongodbEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    instance_type: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance_type'), 'exclude': lambda f: f is None }})
    r"""MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    tunnel_method: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    