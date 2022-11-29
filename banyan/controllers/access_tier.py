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
        return self.app.client.access_tiers

    @ex(help='list access tiers')
    def list(self):
        ats: List[AccessTierInfo] = self._client.list()
        results = []
        headers = ['Access Tier Name', 'ID', 'Cluster', 'Address']
        for res in ats:
            new_res = [res.name, res.id, res.cluster_name, res.address]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='show details of a access tier',
        arguments=[
            (['access_tier_name'],
            {
                'metavar': 'access_tier_name_or_id',
                'help': 'Name or ID of access tier to display.'
            })
        ])
    def get(self):
        info: AccessTierInfo = self._client[self.app.pargs.access_tier_name]
        at_json = AccessTierInfo.Schema().dump(info)
        self.app.render(at_json, handler='json', indent=2, sort_keys=True)


    @ex(help='delete a given access tier record',
        arguments=[
            (['access_tier_name'],
            {
                'metavar': 'access_tier_name_or_id',
                'help': 'Name or ID of access tier to delete.'
            })
        ])
    def delete(self):
        info = self._client.delete(self.app.pargs.access_tier_name)
        self.app.render(info, handler='json', indent=2, sort_keys=True)

    @ex(help='create a new access tier',
        arguments=[
            (['name'],
            {
                'help': 'name of access tier'
            }),
            (['cluster_name'],
            {
                'help': 'name of cluster'
            }),            
            (['address'],
            {
                'help': 'address of access tier'
            })                     
        ])
    def create(self):
        acc_tier = AccessTier(self.app.pargs.name, self.app.pargs.cluster_name, self.app.pargs.address)
        info = self._client.create(acc_tier)
        self.app.render(info, handler='json', indent=2, sort_keys=True)        