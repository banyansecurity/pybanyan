from typing import List
    
from cement import Controller, ex

from banyan.api import BanyanApiClient
from banyan.model.access_tier import AccessTier, AccessTierInfo

class AccessTierController(Controller):
    class Meta:
        label = 'access_tier'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage access tiers'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client

    @ex(help='list access tiers')
    def list(self):
        ats: List[AccessTierInfo] = self._client.access_tiers.list()
        results = []
        headers = ['Access Tier', 'Cluster', 'Address', 'Domains']
        for res in ats:
            new_res = [res.name, res.cluster_name, res.address, res.domains]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

