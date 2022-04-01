import json
from marshmallow_dataclass import dataclass
from banyan.model.service import *


@dataclass
class ServiceInfraBase:
    name: str = ""
    description: str = "ServiceInfraBase"
    # deployment model
    cluster: str = ""
    access_tier: str = ""
    connector: str = ""
    # connectivity
    domain: str = ""
    port: int = 8443
    # backend
    backend_domain: str = ""
    backend_port: int = None
    backend_http_connect: bool = False
    backend_dns_override_for_domain: str = ""
    # client
    client_user_override: bool = True
    client_listen_port: int = None
    # client proxy
    client_banyanproxy_mode: str = ""
    # client ssh
    client_ssh_auth: str = ""
    client_ssh_host_directive: str = ""
    client_ssh_write_config: bool = True
    # client k8s
    client_kube_cluster_name: str = ""
    client_kube_ca_key: str = ""
    # TODO: backend_allowed_hostnames, backend_allowed_cidrs, client_domains_to_proxy
    # TODO: ssh wildcard logic
    # in ui but ignore here - backend_target_delimiter, backend_domain_templating

    # check obj
    def __post_init__(self):
        # basics
        if self.name == "" or self.domain == "":
            raise Exception("Configuration Error! Need to specify name, domain, backend_domain, backend_port.")
        # deployment model
        if self.cluster == "":
            raise Exception("Configuration Error! Need to specify cluster.")
        if (self.connector == "" and self.access_tier == "") or (self.connector != "" and self.access_tier != ""):
            raise Exception("Configuration Error! Need to specify either access_tier or connector.")
        # deployment model = self-hosted access-tier
        if self.access_tier != "":
            self.connector = ""
        # deployment model = global-edge
        if self.connector != "":
            self.access_tier = "*"
        # backend connectivity
        if (self.backend_http_connect and self.backend_domain != "") or (not self.backend_http_connect and self.backend_domain == ""):
            raise Exception("Configuration Error! Need to specify either backend_http_connect or backend_domain.")

    def service_obj(self) -> Service:
        tags = Tags(
            template = ServiceTemplate.TCP,
            service_app_type = "", # child will override
            user_facing = True,
            protocol = "tcp",
            domain = self.domain,
            port = self.port,
            allow_user_override = self.client_user_override,
        )
        metadata = Metadata(
            name = self.name,
            friendly_name = self.name,
            description = self.description,
            cluster = self.cluster,
            tags = tags
        )
        frontend_address = FrontendAddress(
            port = self.port,
            cidr = ""
        )
        attributes = Attributes(
            tls_sni = [self.domain],
            frontend_addresses = [frontend_address],
            host_tag_selector = [
                { "com.banyanops.hosttag.site_name": self.access_tier }
            ]
        )
        target = BackendTarget(
            name = self.backend_domain,
            port = self.backend_port,
            tls = False,
        )
        backend = Backend(
            target = target,
            http_connect = self.backend_http_connect,
            connector_name = self.connector
        )
        cert_settings = CertSettings(
            dns_names = [self.domain],
        )
        http_settings = HttpSettings(
            enabled = False
        )
        spec = Spec(
            attributes = attributes,
            backend = backend,
            cert_settings = cert_settings,
            http_settings = http_settings
        )
        service = Service(
            kind = "BanyanService",
            apiVersion = "rbac.banyanops.com/v1",
            type = "origin",
            metadata = metadata, 
            spec = spec
        )
        return service


@dataclass
class ServiceInfraSSH(ServiceInfraBase):
    def __post_init__(self):
        if self.client_ssh_auth == "":
            self.client_ssh_auth = ServiceClientCertificateType.TRUSTCERT
        super().__post_init__()

    def service_obj(self) -> Service:
        svc = super().service_obj()
        # tags
        svc.metadata.tags.service_app_type = ServiceAppType.SSH
        svc.metadata.tags.ssh_service_type = self.client_ssh_auth
        svc.metadata.tags.ssh_host_directive = self.client_ssh_host_directive
        svc.metadata.tags.write_ssh_config = self.client_ssh_write_config
        # proxy mode
        svc.metadata.tags.ssh_chain_mode = self.backend_http_connect
        return svc

@dataclass
class ServiceInfraRDP(ServiceInfraBase):
    def __post_init__(self):
        super().__post_init__()

    def service_obj(self) -> Service:
        svc = super().service_obj()
        # tags
        svc.metadata.tags.service_app_type = ServiceAppType.RDP
        svc.metadata.tags.app_listen_port = self.client_listen_port
        # proxy mode
        svc.metadata.tags.banyanproxy_mode = ServiceClientProxyMode.RDPGATEWAY if self.backend_http_connect else ServiceClientProxyMode.TCP
        return svc

@dataclass
class ServiceInfraK8S(ServiceInfraBase):
    def __post_init__(self):
        self.backend_http_connect = True
        if self.client_kube_cluster_name == "" or self.client_kube_ca_key == "" or self.backend_dns_override_for_domain == "":
            raise Exception("Configuration Error! Need to specify client_kube_cluster_name, client_kube_ca_key, backend_dns_override_for_domain.")
        super().__post_init__()

    def service_obj(self) -> Service:
        svc = super().service_obj()
        # tags
        svc.metadata.tags.service_app_type = ServiceAppType.K8S
        svc.metadata.tags.app_listen_port = self.client_listen_port
        svc.metadata.tags.kube_cluster_name = self.client_kube_cluster_name
        svc.metadata.tags.kube_ca_key = self.client_kube_ca_key
        # proxy mode
        svc.metadata.tags.banyanproxy_mode = ServiceClientProxyMode.CHAIN
        # dns override
        svc.spec.backend.dns_overrides = { self.domain : self.backend_dns_override_for_domain }
        return svc

@dataclass
class ServiceInfraDatabase(ServiceInfraBase):
    def __post_init__(self):
        super().__post_init__()            

    def service_obj(self) -> Service:
        svc = super().service_obj()
        # tags
        svc.metadata.tags.service_app_type = ServiceAppType.DATABASE
        svc.metadata.tags.app_listen_port = self.client_listen_port
        # proxy mode
        svc.metadata.tags.banyanproxy_mode = ServiceClientProxyMode.CHAIN if self.backend_http_connect else ServiceClientProxyMode.TCP
        return svc

@dataclass
class ServiceInfraTCP(ServiceInfraBase):
    def __post_init__(self):
        super().__post_init__()            

    def service_obj(self) -> Service:
        svc = super().service_obj()
        # tags
        svc.metadata.tags.service_app_type = ServiceAppType.TCP
        svc.metadata.tags.app_listen_port = self.client_listen_port
        # proxy mode
        svc.metadata.tags.banyanproxy_mode = ServiceClientProxyMode.CHAIN if self.backend_http_connect else ServiceClientProxyMode.TCP
        return svc


if __name__ == '__main__':
    svc_ssh_at = ServiceInfraSSH(
        name = "test-ssh-at",
        cluster = "cluster1",
        access_tier = "foo",
        domain = "test-infra-ssh.example.com",
        backend_http_connect = True,
        client_ssh_host_directive = "10.10.1.0/24"
    )
    obj = svc_ssh_at.service_obj()
    print(json.dumps(Service.Schema().dump(obj), indent=2, sort_keys=True))

    svc_ssh_conn = ServiceInfraSSH(
        name = "test-ssh-conn",
        cluster = "global-edge",
        connector = "foo",
        domain = "test-ssh-conn" + ".orgname.banyanops.com",
        backend_domain = "10.10.1.1",
        backend_port = 22
    )
    obj = svc_ssh_conn.service_obj()
    print(json.dumps(Service.Schema().dump(obj), indent=2, sort_keys=True))

    svc_tcp_at = ServiceInfraTCP(
        name = "test-infra-tcp",
        cluster = "cluster1",
        access_tier = "foo",
        domain = "test-infra-tcp.example.com",
        backend_domain = "10.10.1.1",
        backend_port = 6006,
        client_listen_port = 9119
    )
    obj = svc_tcp_at.service_obj()
    print(json.dumps(Service.Schema().dump(obj), indent=2, sort_keys=True))

    svc_k8s_conn = ServiceInfraK8S(
        name = "test-k8s-conn",
        cluster = "global-edge",
        connector = "foo",
        domain = "test-k8s-conn" + ".orgname.banyanops.com",
        backend_dns_override_for_domain = "myoidcproxy.amazonaws.com",
        client_kube_cluster_name = "eks-hero",
        client_kube_ca_key = "AAAA1234"
    )
    obj = svc_k8s_conn.service_obj()
    print(json.dumps(Service.Schema().dump(obj), indent=2, sort_keys=True))

