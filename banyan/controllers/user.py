from cement import Controller, ex


class UserController(Controller):
    class Meta:
        label = 'user'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage user accounts'

    # @property
    # def _client(self) -> RoleAPI:
    #     return self.app.client.roles

    @ex(help='list users')
    def list(self):
        pass
