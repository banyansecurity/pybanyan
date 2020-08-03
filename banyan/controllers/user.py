from typing import List

from cement import Controller, ex

from banyan.api import UserAPI
from banyan.controllers.base import Base
from banyan.model.user_device import User


class UserController(Controller):
    class Meta:
        label = 'user'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage user accounts'

    @property
    def _client(self) -> UserAPI:
        return self.app.client.users

    @ex(help='list users')
    def list(self):
        users: List[User] = self._client.list()
        results = list()
        headers = ['Name', 'Email', 'Last Login', 'Login Count', 'Trust Score', 'Last TS Update']
        for user in users:
            new_row = [user.name, user.email, user.last_login.strftime(Base.TABLE_DATE_FORMAT),
                       user.login_count, user.trust_data.level,
                       user.trust_data.updated_at.strftime(Base.TABLE_DATE_FORMAT)]
            results.append(new_row)
        results.sort(key=lambda x: x[0])
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='show detailed information about a user',
        arguments=[
            (['email'],
             {
                 'help': 'Email address for the user.'
             }),
        ])
    def get(self):
        hostname = self.app.pargs.hostname
        agent = self._client.find(hostname)
        agent_json = Netagent.Schema().dump(agent)
        # colorized_json = highlight(policy_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(agent_json, handler='json', indent=2, sort_keys=True)

