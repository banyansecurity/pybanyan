from typing import List
    
from cement import Controller, ex

from banyan.controllers.base import Base

from banyan.api import BanyanApiClient
from banyan.model.connector import Connector, ConnectorInfo, Spec, PeerAccessTier, Metadata

class ConnectorController(Controller):
    class Meta:
        label = 'connector'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage connectors'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client.connectors

    @ex(help='list connectors')
    def list(self):
        conns: List[ConnectorInfo] = self._client.list()
        results = []
        headers = ['Connector Name', 'ID', 'Status', 'Version', 'Host']
        for res in conns:
            new_res = [res.name, res.id, res.status, res.connector_version, Base.trunc(res.host_info, 24, True)]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')


    @ex(help='show details of a connector',
        arguments=[
            (['connector_name'],
            {
                'metavar': 'connector_name_or_id',
                'help': 'Name or ID of connector to display.'
            })
        ])
    def get(self):
        info: ConnectorInfo = self._client[self.app.pargs.connector_name]
        conn_json = ConnectorInfo.Schema().dump(info)
        self.app.render(conn_json, handler='json', indent=2, sort_keys=True)


    @ex(help='delete a given connector record',
        arguments=[
            (['connector_name'],
            {
                'metavar': 'connector_name_or_id',
                'help': 'Name or ID of connector to delete.'
            })
        ])
    def delete(self):
        info = self._client.delete(self.app.pargs.connector_name)
        self.app.render(info, handler='json', indent=2, sort_keys=True)


    @ex(help='create a new connector',
        arguments=[
            (['name'],
            {
                'help': 'name of connector'
            }),
            (['api_key_id'],
            {
                'help': 'UUID of API key used to register the connector'
            })                     
        ])
    def create(self):
        metadata = Metadata(self.app.pargs.name, self.app.pargs.name)
        peer_at = PeerAccessTier('global-edge', ['*'])
        spec = Spec(self.app.pargs.api_key_id, 25, [], [peer_at])
        conn = Connector('', '', '', metadata, spec)
        info = self._client.create(conn)
        self.app.render(info, handler='json', indent=2, sort_keys=True)

