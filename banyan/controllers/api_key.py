from typing import List
    
from cement import Controller, ex

from banyan.api import BanyanApiClient
from banyan.model.api_key import ApiKey, ApiKeyInfo

class ApiKeyController(Controller):
    class Meta:
        label = 'api_key'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage API Keys'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client

    @ex(help='list api_keys')
    def list(self):
        api_keys: List[ApiKeyInfo] = self._client.api_keys.list()
        results = []
        headers = ['Name', 'ID', 'Scope', 'Description']
        for res in api_keys:
            new_res = [res.name, res.id, res.scope, res.description]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')
               
