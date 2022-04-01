from marshmallow_dataclass import dataclass
from banyan.model.service import *

@dataclass
class ServiceWebStandard:
    name: str
    description: str
    
    cluster: str
    access_tier: str
    connector: str
    
    domain: str
    backend_domain: str
    backend_port: int
    
    # solid defaults
    port: int = 443
    letsencrypt: bool = False
    backend_tls: bool = False
    backend_tls_insecure: bool = False

    # todo - cors, exemptions, custom_headers, service_accounts
    # in ui but ignore here - description_link, icon, show_in_catalog, backend_tls_client_cert

    def create_service_obj(self) -> Service:
        # global edge deployment model if connector is set
        access_tier_selector = "com.banyanops.hosttag.site_name"
        access_tier_value = self.access_tier
        if self.connector:
            access_tier_value = "*"

        tags = Tags(
            template = ServiceTemplate.WEB,
            service_app_type = ServiceAppType.WEB,
            user_facing = True,
            protocol = "HTTPS",
            domain = self.domain,
            port = self.port
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
                {access_tier_selector: access_tier_value}
            ]
        )
        target = BackendTarget(
            name = self.backend_domain,
            port = self.backend_port,
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
        http_settings = HttpSettings(
            enabled = True,
            oidc_settings = oidc_settings
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


if __name__ == '__main__':
    svc_web = ServiceWebStandard(
        name = "test",
        description = "test",
        cluster = "cl1",
        access_tier = "",
        connector = "myconn",
        domain = "test.example.com",
        backend_domain = "10.10.1.1",
        backend_port = 8080
    )
    svc_obj = svc_web.create_service_obj()
    print(svc_obj)
