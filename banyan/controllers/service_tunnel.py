from typing import List
    
from cement import Controller, ex

from banyan.api import ServiceTunnelAPI
from banyan.controllers.base import Base
from banyan.model.service_tunnel import ServiceTunnel, ServiceTunnelInfo

class ServiceTunnelController(Controller):
    class Meta:
        label = 'service_tunnel'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage service tunnels'

    @property
    def _client(self) -> ServiceTunnelAPI:
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
    

    @ex(help='show the definition of a service tunnel',
        arguments=[
            (['service_tunnel_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service tunnel to display.'
             }),
        ])
    def get(self):
        info: ServiceTunnelInfo = self._client[self.app.pargs.service_tunnel_name]
        service_json = ServiceTunnel.Schema().dump(info.service)
        # colorized_json = highlight(service_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(service_json, handler='json', indent=2, sort_keys=True)


    @ex(help='delete a given service tunnel',
        arguments=[
            (['service_tunnel_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service tunnel to delete.'
             }),
        ])
    def delete(self):
        info = self._client.delete(self.app.pargs.service_tunnel_name)
        self.app.render(info, handler='json', indent=2, sort_keys=True)