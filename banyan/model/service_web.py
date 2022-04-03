import json
from marshmallow_dataclass import dataclass
from banyan.model.service import *

@dataclass
class ServiceWebStandard:
    name: str = ""
    description: str = "ServiceWebStandard"
    # deployment model
    cluster: str = ""
    access_tier: str = ""
    connector: str = ""
    # connectivity
    domain: str = ""
    port: int = 443
    letsencrypt: bool = False
    # backend
    backend_domain: str = ""
    backend_port: int = None
    backend_tls: bool = False
    backend_tls_insecure: bool = False
    # TODO: cors, exemptions, custom_headers, service_accounts
    # in ui but ignore here - description_link, icon, show_in_catalog, backend_tls_client_cert

    # check obj
    def __post_init__(self):
        # basics
        if self.name == "" or self.domain == "" or self.backend_domain == "" or self.backend_port == 0:
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

    def service_obj(self) -> Service:
        tags = Tags(
            template = str(ServiceTemplate.WEB),
            user_facing = "true",
            protocol = "https",
            domain = self.domain,
            port = str(self.port),
            icon = "",
            service_app_type = str(ServiceAppType.WEB),
            description_link = ""
        )
        metadata = Metadata(
            name = self.name,
            friendly_name = None,
            description = self.description,
            cluster = self.cluster,
            tags = tags
        )
        frontend_address = FrontendAddress(
            port = str(self.port),
            cidr = None
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
            port = str(self.backend_port),
            tls = self.backend_tls,
            tls_insecure = self.backend_tls_insecure
        )
        backend = Backend(
            target = target,
            connector_name = self.connector
        )
        cert_settings = CertSettings(
            dns_names = [self.domain],
            letsencrypt = self.letsencrypt
        )
        oidc_settings = OIDCSettings(
            enabled = True,
            service_domain_name = "https://" + self.domain
        )
        exempted_paths = ExemptedPaths(
            enabled = False
        )
        http_settings = HttpSettings(
            enabled = True,
            oidc_settings = oidc_settings,
            exempted_paths = exempted_paths
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
