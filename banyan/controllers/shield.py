from typing import List

from cement import Controller, ex

from banyan.api.shield import ShieldAPI
from banyan.core.exc import BanyanError
from banyan.model.shield import Shield


class ShieldController(Controller):
    class Meta:
        label = 'shield'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage Banyan Shield clusters'

    @property
    def _client(self) -> ShieldAPI:
        return self.app.client.shields

    @ex(help='list shields')
    def list(self):
        shields: List[Shield] = self._client.list()
        results = list()
        headers = ['Name', 'ID', 'Address', 'SCEP Enabled', 'OTK Enabled', 'Status']
        for shield in shields:
            new_row = [shield.name, shield.id,
                       shield.public_addr, shield.scep_enabled, shield.otk_enabled, self._client.status(str(shield.id))]
            results.append(new_row)
        results.sort(key=lambda x: x[0])
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='get one-time key for netagent registration',
        arguments=[
            (['shield_name'],
             {
                 'metavar': 'shield_name_or_id',
                 'help': 'Name or ID of the shield.'
             }),
        ])
    def get_otk(self):
        shield_name = self.app.pargs.shield_name
        shield = self._client.find(shield_name)
        if self._client.status(shield_name) == 'INACTIVE':
            raise BanyanError(f'Shield {shield_name} status is INACTIVE')
        if not shield.otk_enabled:
            raise BanyanError(f'Shield {shield_name} is not enabled for OTK')
        self.app.print(str(shield.one_time_key))
