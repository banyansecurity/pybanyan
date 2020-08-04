from typing import List

from cement import Controller, ex

from banyan.api.shield import ShieldAPI
from banyan.controllers.base import Base
from banyan.core.exc import BanyanError
from banyan.model.netagent import Netagent
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

    @ex(help='show detailed information about a shield',
        arguments=[
            (['shield_name'],
             {
                 'metavar': 'shield_name_or_id',
                 'help': 'Name or ID of the shield.'
             }),
        ])
    def get(self):
        shield_name = self.app.pargs.shield_name
        shield = self._client.find(shield_name)
        shield_json = Shield.Schema().dump(shield)
        # colorized_json = highlight(policy_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(shield_json, handler='json', indent=2, sort_keys=True)

    @ex(help='list netagents connected to a shield',
        arguments=[
            (['shield_name'],
             {
                 'metavar': 'shield_name_or_id',
                 'help': 'Name or ID of the shield.'
             }),
        ])
    def list_netagents(self):
        shield_name = self.app.pargs.shield_name
        shield = self._client.find(shield_name)
        agents: List[Netagent] = self._client.config.netagent_map[str(shield.id)]
        results = list()
        headers = ['Site Name', 'Hostname', 'Public IP', 'Status', 'Last Activity']
        for agent in agents:
            new_row = [agent.name, agent.hostname, agent.public_ip_addr, agent.status,
                       agent.last_activity_at.strftime(Base.TABLE_DATE_FORMAT) if agent.last_activity_at else 'None']
            results.append(new_row)
        results.sort(key=lambda x: x[0] + x[1])
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    # TODO: implement for /shield_activity?num=1000&ShieldName=<name>
    @ex(help='show activity (stats, links, events) recorded by a shield')
    def list_activity(self):
        pass

    # TODO: implement /register_shield
    @ex(help='register a shield with the system')
    def create(self):
        pass

    # TODO: implement /delete_shield_cluster
    @ex(help='delete a shield')
    def delete(self):
        pass

    # TODO: implement /shield_events?StartTime=&EndTime=
    @ex(help='show security events recorded by a shield')
    def list_events(self):
        pass
