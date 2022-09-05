import logging
from typing import List
from uuid import UUID

from cement import Controller, ex

from banyan.controllers.base import Base

from banyan.api import BanyanApiClient
from banyan.model.connector import Connector, ConnectorInfo

class ConnectorController(Controller):
    class Meta:
        label = "connector"
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage connectors (for Global Edge deployments)'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client

    @ex(help='list connectors')
    def list(self):
        access_tiers: List[ConnectorInfo] = self._client.connectors.list()
        results = []
        headers = ['Name', 'ID', 'Status', 'CIDRs', 'Domains']
        for res in access_tiers:
            new_res = [res.name, res.id, res.status, res.cidrs, res.domains]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='get details of a connector',
        arguments=[
            (['name'],
            {
                'help': 'get connector details by name.'
            }),
            (['--spec'],
            {
                'help': 'get spec JSON for use in updating'
            }),                       
        ])
    def get(self):
        params={'name': self.app.pargs.name}
        connectors: List[ConnectorInfo] = self._client.connectors.list(params=params)
        conn_json = ConnectorInfo.Schema().dump(connectors[0])
        print(connectors[0])
        if (self.app.pargs.spec):
            conn_json = Connector.Schema().dump(connectors[0].connector)
        self.app.render(conn_json, handler='json', indent=2, sort_keys=True)