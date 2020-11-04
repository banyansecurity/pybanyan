from dataclasses import field
from datetime import datetime
from ipaddress import IPv4Interface
from typing import List, Dict, Optional, ClassVar, Type
from uuid import UUID

from marshmallow import validate, pre_load, Schema, EXCLUDE
from marshmallow_dataclass import dataclass
from semver import VersionInfo

from banyan.model import Resource, BanyanEnum, VersionField


class NetagentStatus(BanyanEnum):
    TERMINATED = "Terminated"
    REPORTING = "Reporting"


@dataclass
class Netagent(Resource):
    class Meta:
        unknown = EXCLUDE

    TAG_HOSTNAME = "com.banyanops.hosttag.hname"
    TAG_TYPE = "com.banyanops.hosttag.type"
    TAG_SITE_NAME = "com.banyanops.hosttag.site_name"
    TAG_DOMAIN_NAMES = "com.banyanops.hosttag.site_domain_names"
    TAG_FQDN = "com.banyanops.hosttag.site_address"

    hostname: str = field(metadata={"data_key": "Hostname"})
    version: VersionInfo = field(metadata={"marshmallow_field": VersionField(data_key="Version")})
    visibility: bool = field(metadata={"data_key": "Visibility"})
    cidrs_txt: str = field(metadata={"data_key": "CIDRs"})
    uname_txt: str = field(metadata={"data_key": "Uname"})
    site_name: str = field(metadata={"data_key": "SiteName"})
    status: str = field(metadata={"validate": validate.OneOf(NetagentStatus.choices()),
                                  "data_key": "Status"})
    cluster_name: Optional[str] = field(metadata={"data_key": "ClusterName"})
    cluster_id: Optional[UUID] = field(metadata={"data_key": "ClusterID"})
    last_activity_at: Optional[datetime] = field(metadata={"format": "iso", "data_key": "LastActivityAt"})
    ip_addresses: List[str] = field(default_factory=list, metadata={"data_key": "IPs"})
    host_tags: Dict[str, str] = field(default_factory=dict, metadata={"data_key": "HostTags"})
    Schema: ClassVar[Type[Schema]] = Schema

    # noinspection PyUnusedLocal
    @pre_load
    def _remove_empty_dates(self, data, many, **kwargs):
        if "LastActivityAt" in data and data["LastActivityAt"] == "":
            del data["LastActivityAt"]
        return data

    @property
    def name(self) -> str:
        return self.hostname

    @property
    def id(self) -> str:
        return self.hostname

    @property
    def domain_names(self) -> List[str]:
        names = self.host_tags.get(Netagent.TAG_DOMAIN_NAMES).split(',')
        return [x.strip() for x in names]

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

    @property
    def public_ip_addr(self) -> str:
        for ip in self.ip_addresses:
            nic = IPv4Interface(ip)
            if nic.is_global:
                return ip
        return ''

    @property
    def is_access_tier(self):
        host_type = self.host_tags.get(Netagent.TAG_TYPE)
        return host_type == 'access_tier'

    @property
    def host_type(self):
        return self.host_tags.get(Netagent.TAG_TYPE)
