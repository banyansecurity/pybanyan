from typing import List

from cement import Controller, ex

from banyan.api import NetagentAPI, ShieldAPI
from banyan.controllers.base import Base
from banyan.model.netagent import Netagent


class NetagentController(Controller):
    class Meta:
        label = 'netagent'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage netagents (AccessTiers and HostAgents)'

    @property
    def _client(self) -> NetagentAPI:
        return self.app.client.netagents

    @ex(help='list netagents',
        arguments=[
            (['--all'],
             {
                 'action': 'store_true',
                 'dest': 'show_all',
                 'help': 'Display all agents, including terminated agents. The default is to show only '
                         'active, reporting agents.',
             }),
        ])
    def list(self):
        agents: List[Netagent] = self._client.list()
        clusters: ShieldAPI = self.app.client.shields
        results = list()
        headers = ['Hostname', 'Shield', 'Type', 'Public IP', 'Status', 'Last Activity']
        for agent in agents:
            shield_name = agent.cluster_name or clusters.find(str(agent.cluster_id)).name
            if agent.status == 'Reporting' or self.app.pargs.show_all:
                last_activity = agent.last_activity_at.strftime(Base.TABLE_DATE_FORMAT) if \
                    agent.last_activity_at else 'None'
                new_row = [agent.hostname, shield_name, agent.host_type,
                           agent.public_ip_addr, agent.status,
                           last_activity]
                results.append(new_row)
        results.sort(key=lambda x: x[0])
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='show detailed information about a netagent',
        arguments=[
            (['hostname'],
             {
                 'help': 'Hostname of the agent.'
             }),
        ])
    def get(self):
        hostname = self.app.pargs.hostname
        agent = self._client.find(hostname)
        agent_json = Netagent.Schema().dump(agent)
        # colorized_json = highlight(policy_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(agent_json, handler='json', indent=2, sort_keys=True)
