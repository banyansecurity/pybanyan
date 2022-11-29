from typing import List
    
from cement import Controller, ex

from banyan.api import BanyanApiClient
from banyan.controllers.base import Base
from banyan.model.service_tunnel import ServiceTunnel, ServiceTunnelInfo

class ServiceTunnelController(Controller):
    class Meta:
        label = 'service_tunnel'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage service tunnels'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client.service_tunnels

    @ex(help='list service tunnels')
    def list(self):
        ats: List[ServiceTunnelInfo] = self._client.list()
        results = []
        headers = ['Name', 'ID', 'Created', 'Last Updated']
        for res in ats:
            new_res = [res.name, res.id, 
                       res.created_at.strftime(Base.TABLE_DATE_FORMAT),
                       res.updated_at.strftime(Base.TABLE_DATE_FORMAT)]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')
    

