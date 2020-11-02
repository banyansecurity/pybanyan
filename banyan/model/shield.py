from dataclasses import field
from datetime import datetime
from ipaddress import IPv4Address
from typing import List, Dict, ClassVar, Type
from uuid import UUID

import OpenSSL.crypto
from marshmallow import fields, Schema, EXCLUDE
from marshmallow_dataclass import dataclass
from semver import VersionInfo

from banyan.model import Resource, VersionField
from banyan.model.netagent import Netagent


@dataclass
class Shield(Resource):
    class Meta:
        unknown = EXCLUDE

    org_id: UUID = field(metadata={"data_key": "OrgID"})
    shield_id: UUID = field(metadata={"data_key": "UUID"})
    shield_name: str = field(metadata={"data_key": "ShieldName"})
    group_type: str = field(metadata={"data_key": "GroupType"})
    cluster_mgr_type: str = field(metadata={"data_key": "ClusterMgrType"})
    cluster_mgr_ip: IPv4Address = field(metadata={"marshmallow_field": fields.String(data_key="ClusterMgrIP")})
    version: VersionInfo = field(metadata={"marshmallow_field": VersionField(data_key="ShieldVersion")})
    auto_upgrade: bool = field(metadata={"data_key": "AutoUpgrade"})
    one_time_key: UUID = field(metadata={"data_key": "OneTimeKey"})
    otk_expire_dt: datetime = field(metadata={"data_key": "OTKExpiryTime"})
    scep_enabled: bool = field(metadata={"data_key": "SCEPEnabled"})
    public_addr: str = field(metadata={"data_key": "PublicAddr"})
    ca_cert_str: str = field(metadata={"data_key": "CACert"})
    otk_enabled: bool = field(metadata={"data_key": "OTKEnabled"})
    ssh_ca_public_key: str = field(metadata={"data_key": "SSHCAPublicKey"})
    Schema: ClassVar[Type[Schema]] = Schema

    def load_cacert(self) -> OpenSSL.crypto.X509:
        cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, self.ca_cert_str.encode('utf-8'))
        return cert

    @property
    def name(self) -> str:
        return self.shield_name

    @property
    def id(self) -> str:
        return str(self.shield_id)


@dataclass
class ShieldLastActivity:
    class Meta:
        unknown = EXCLUDE

    last_activity_time: datetime = field(metadata={"data_key": "InsertTime"})
    status: str = field(metadata={"data_key": "Status"})
    uuid: UUID = field(metadata={"data_key": "UUID"})
    Schema: ClassVar[Type[Schema]] = Schema


@dataclass
class ShieldConfig:
    class Meta:
        unknown = EXCLUDE

    shields: List[Shield] = field(default_factory=list, metadata={"data_key": "Configs"})
    last_activity_map: Dict[str, ShieldLastActivity] = field(default_factory=dict,
                                                             metadata={"data_key": "ShieldLastActivitiesMap"})
    netagent_map: Dict[str, List[Netagent]] = field(default_factory=dict,
                                                    metadata={"data_key": "NetagentHostInfoMap"})
    Schema: ClassVar[Type[Schema]] = Schema
