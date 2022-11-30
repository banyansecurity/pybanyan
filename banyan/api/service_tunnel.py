from banyan.api.base import ApiBase
from banyan.model.service_tunnel import ServiceTunnel, ServiceTunnelInfo

class ServiceTunnelAPI(ApiBase):
    class Meta:
        data_class = ServiceTunnel
        info_class = ServiceTunnelInfo
        supports_paging = True
        list_uri = '/v2/service_tunnel'
        insert_uri = '/v2/service_tunnel'
        delete_uri = '/v2/service_tunnel/ID'
        obj_name = 'service_tunnel'
