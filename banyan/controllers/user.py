from typing import List

from cement import Controller, ex

from banyan.api import UserAPI
from banyan.controllers.base import Base
from banyan.model.user_device import User, TrustDataV1, TrustScore


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
        email = self.app.pargs.email
        user = self._client.find(email)
        user_json = User.Schema().dump(user)
        # colorized_json = highlight(policy_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(user_json, handler='json', indent=2, sort_keys=True)

    @ex(help='show details about the user\'s trust score calculation',
        arguments=[
            (['email'],
             {
                 'help': 'Email address for the user.'
             }),
        ])
    def get_trust(self):
        email = self.app.pargs.email
        user = self._client.find(email)
        trust = self._client.get_trustscores(user)
        trust_json = TrustScore.Schema().dump(trust, many=True)
        # colorized_json = highlight(policy_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(trust_json, handler='json', indent=2, sort_keys=True)

    @ex(help='set the maximum trust level for a user',
        arguments=[
            (['email'],
             {
                 'help': 'Email address for the user.'
             }),
            (['--trust-level'],
             {
                 'choices': TrustDataV1.TRUST_VALUES,
                 'required': True,
                 'help': f'Maximum trust level for this device. Must be one of: {TrustDataV1.TRUST_VALUES}.'
             }
             ),
            (['--reason'],
             {
                 'required': True,
                 'help': 'Explanation to be displayed in console and to the end user.'
             }),
            (['--ext-source'],
             {
                 'required': True,
                 'help': 'Name of the external data source (e.g. CarbonBlack, CrowdStrike, etc).'
             }),
        ])
    def set_max_trust(self):
        serial_number = self.app.pargs.serial_number
        device = self._client.find(serial_number)
        trust = self._client.set_max_trustlevel(device, self.app.pargs.trust_level,
                                                self.app.pargs.reason, self.app.pargs.ext_source)
        trust_json = TrustScore.Schema().dump(trust)
        self.app.render(trust_json, handler='json', indent=2, sort_keys=True)

    # TODO: implement /user/verify
    @ex(help='force verify a user')
    def verify(self):
        pass

    # TODO: implement /forgot_password
    @ex(help='send password reminder email')
    def forgot_password(self):
        pass

    # TODO: implement /reset_password
    @ex(help='send password reset email')
    def reset_password(self):
        pass

    # TODO: implement /refresh_token
    @ex(help='generate API refresh token for a user')
    def refresh_token(self):
        pass

    # TODO: implement /revoke_token
    @ex(help='revoke a user\'s refresh token')
    def revoke_token(self):
        pass
