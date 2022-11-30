from typing import List

from cement import Controller, ex

from banyan.api import BanyanApiClient
from banyan.model.api_key import ApiKey, ApiKeyInfo

class ApiKeyController(Controller):
    class Meta:
        label = 'api_key'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage API keys'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client.api_keys

    @ex(help='list api_keys')
    def list(self):
        api_keys: List[ApiKeyInfo] = self._client.list()
        results = []
        headers = ['API Key Name', 'ID', 'Scope', 'Description']
        for res in api_keys:
            new_res = [res.name, res.id, res.scope, res.description]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')


    @ex(help='show details of an api_key',
        arguments=[
            (['api_key_name'],
            {
                'metavar': 'connector_name_or_id',
                'help': 'Name or ID of api_key to display.'
            })
        ])
    def get(self):
        info: ApiKeyInfo = self._client[self.app.pargs.api_key_name]
        api_key_json = ApiKeyInfo.Schema().dump(info)
        self.app.render(api_key_json, handler='json', indent=2, sort_keys=True)


    @ex(help='delete a given api_key record',
        arguments=[
            (['api_key_name'],
            {
                'metavar': 'connector_name_or_id',
                'help': 'Name or ID of api_key to display.'
            })
        ])
    def delete(self):
        info = self._client.delete(self.app.pargs.api_key_name)
        self.app.render(info, handler='json', indent=2, sort_keys=True)


    @ex(help='create a new api_key',
        arguments=[
            (['name'],
            {
                'help': 'name of api key'
            }),
            (['description'],
            {
                'help': 'description of api key'
            }),
            (['scope'],
            {
                'help': 'level of privilege - satellite, access_tier, Admin, ServiceAuthor, PolicyAuthor, EventWriter, ReadOnly'
            })                     
        ])
    def create(self):
        n_api = ApiKey(
            name = self.app.pargs.name,
            description = self.app.pargs.description,
            scope = self.app.pargs.scope
        )
        info = self._client.create(n_api)
        self.app.render(info, handler='json', indent=2, sort_keys=True)
        