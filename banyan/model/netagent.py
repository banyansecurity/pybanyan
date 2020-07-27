from dataclasses import field
from typing import List, Dict, Optional, ClassVar, Type
from marshmallow import validate, fields, pre_load, Schema
from marshmallow_dataclass import dataclass
# from dataclasses_serialization.json import JSONStrSerializerMixin, JSONSerializerMixin
# from banyan.model.custom_types import Iso8601Date
from semver import VersionInfo
from ipaddress import IPv4Interface
from datetime import datetime
from uuid import UUID


@dataclass
class Netagent:
    TERMINATED = "Terminated"
    REPORTING = "Reporting"
    TAG_HOSTNAME = "com.banyanops.hosttag.hname"
    TAG_SITE_NAME = "com.banyanops.hosttag.site_name"
    TAG_DOMAIN_NAMES = "com.banyanops.hosttag.site_domain_names"
    TAG_FQDN = "com.banyanops.hosttag.site_address"
    hostname: str = field(metadata={"data_key": "Hostname"})
    version: VersionInfo = field(metadata={"marshmallow_field": fields.String(data_key="Version")})
    visibility: bool = field(metadata={"data_key": "Visibility"})
    cidrs_txt: str = field(metadata={"data_key": "CIDRs"})
    uname_txt: str = field(metadata={"data_key": "Uname"})
    site_name: str = field(metadata={"data_key": "SiteName"})
    status: str = field(metadata={"validate": validate.OneOf([TERMINATED, REPORTING]), "data_key": "Status"})
    cluster_name: Optional[str] = field(metadata={"data_key": "ClusterName"})
    cluster_id: Optional[UUID] = field(metadata={"data_key": "ClusterID"})
    last_activity_at: Optional[datetime] = field(metadata={"format": "iso", "data_key": "LastActivityAt"})
    ip_addresses: List[str] = field(default_factory=list, metadata={"data_key": "IPs"})
    host_tags: Dict[str, str] = field(default_factory=dict, metadata={"data_key": "HostTags"})
    Schema: ClassVar[Type[Schema]] = Schema

    @pre_load
    def remove_empty_dates(self, data, many, **kwargs):
        if "LastActivityAt" in data and data["LastActivityAt"] == "":
            del data["LastActivityAt"]
        return data

    @property
    def name(self) -> str:
        return self.host_tags.get(Netagent.TAG_SITE_NAME)

    @property
    def domain_names(self) -> List[str]:
        return self.host_tags.get(Netagent.TAG_DOMAIN_NAMES).split(',')

    @property
    def fqdn(self):
        return self.host_tags.get(Netagent.TAG_FQDN)

    @property
    def host_data(self) -> Dict[str, str]:
        data = dict()
        for pair in self.uname_txt.split(','):
            k, *v = pair.strip().split(' ')
            data[k] = ' '.join(v)
        return data

    @property
    def cidr_map(self) -> Dict[IPv4Interface, int]:
        assert(self.cidrs_txt[0] == '[' and self.cidrs_txt[-1] == ']')
        tokens = self.cidrs_txt[1:-1].split(' ')
        cidrs = dict()
        while tokens:
            net_str = IPv4Interface(tokens[0])
            assert(tokens[1] == '--dport')
            port = int(tokens[2])
            tokens = tokens[3:]
            cidrs[net_str] = port
        return cidrs
