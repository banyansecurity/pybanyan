import logging
from typing import List
from uuid import UUID

from cement import Controller, ex

from banyan.controllers.base import Base

from banyan.api import BanyanApiClient
from banyan.model.access_tier import AccessTier, AccessTierInfo

class AccessTierController(Controller):
    class Meta:
        label = "access_tier"
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage access tiers'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client

    @ex(help='list access_tiers')
    def list(self):
        access_tiers: List[AccessTierInfo] = self._client.access_tiers.list()
        results = []
        headers = ['Name', 'ID', 'Cluster', 'Address', 'Status', 'Tunnel - User', 'Tunnel - Sat']
        for res in access_tiers:
            new_res = [res.name, res.id, res.cluster_name, res.address, res.status,
                       res.tunnel_enduser is not None,
                       res.tunnel_satellite is not None]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')
    

    @ex(help='get details of an access_tier',
        arguments=[
            (['name'],
            {
                'help': 'get access_tier details by name.'
            }),
            (['--spec'],
            {
                'help': 'get spec JSON for use in updating'
            }),                       
        ])
    def get(self):
        params={'name': self.app.pargs.name}
        access_tiers: List[AccessTierInfo] = self._client.access_tiers.list(params=params)
        at_json = AccessTierInfo.Schema().dump(access_tiers[0])
        if (self.app.pargs.spec):
            at_json = AccessTier.Schema().dump(AccessTier.Schema().load(at_json))
        self.app.render(at_json, handler='json', indent=2, sort_keys=True)

    @ex(help='create a new access_tier',
        arguments=[
            (['access_tier_json'], 
            {
                'help': 'JSON blob describing the new access_tier to be created, or a filename '
                         'containing JSON prefixed by "@" (example: @res.json).'
            }),
        ])
    def create(self):
        new_at_json = Base.get_json_input(self.app.pargs.access_tier_json)
        access_tier: AccessTierInfo = self._client.access_tiers.create(new_at_json)
        at_json = AccessTier.Schema().dump(access_tier)
        self.app.render(at_json, handler='json', indent=2, sort_keys=True)


    @ex(help='update tunnel configs for a given access_tier',
        arguments=[
            (['name'],
            {
                'help': 'Access tier name to update.'
            }),
            (['--enduser_cidrs'],
            {
                'help': 'Filename containing EndUser tunnel CIDR range '
                        'prefixed by "@" (example: @cidrs.txt).'
            }),                       
        ])
    def update_config(self):
        params={'name': self.app.pargs.name}
        access_tiers: List[AccessTierInfo] = self._client.access_tiers.list(params=params)
        my_at_info: AccessTierInfo = access_tiers[0]
        my_at: AccessTier = AccessTier.Schema().load(AccessTierInfo.Schema().dump(my_at_info))
        
        # enduser CIDRs
        if (self.app.pargs.enduser_cidrs):
            if my_at.tunnel_enduser is None:
                print('--> No EndUser tunnel to update')
                return

            cidrs = []
            with open(self.app.pargs.enduser_cidrs[1:]) as tmp_file:
                cidrs = [line.rstrip('\n') for line in tmp_file]
            print('--> Updating EndUser tunnel CIDR range from:\n%s' % "\n".join(my_at.tunnel_enduser.cidrs))
            print('--> Updating EndUser tunnel CIDR range to:\n%s' % "\n".join(cidrs[:10]))

            my_at.tunnel_enduser.cidrs = cidrs
            my_at_json = AccessTier.Schema().dump(my_at)

            access_tier: AccessTierInfo = self._client.access_tiers.update(my_at_info.id, my_at_json)
            at_json = AccessTier.Schema().dump(access_tier)
            self.app.render(at_json, handler='json', indent=2, sort_keys=True)


    @ex(help='delete a given access_tier', 
        arguments=[
            (['id'],
            {
                'help': 'ID (not name) of access_tier to delete.'
            }),            
        ])
    def delete(self):
        id: UUID = self.app.pargs.id
        info = self._client.access_tiers.delete(id)
        self.app.render(info, handler='json')