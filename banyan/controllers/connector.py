from typing import List
    
from cement import Controller, ex

from banyan.api import BanyanApiClient
from banyan.model.connector import Connector, ConnectorInfo

class ConnectorController(Controller):
    class Meta:
        label = 'connector'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage Connectors'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client

    @ex(help='list connectors')
    def list(self):
        conns: List[ConnectorInfo] = self._client.connectors.list()
        results = []
        headers = ['Connector', 'Status', 'Version', 'Host']
        for res in conns:
            new_res = [res.name, res.status, res.connector_version, res.host_info['name']]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')
