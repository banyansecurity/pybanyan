from cement import Controller, ex


class AdminController(Controller):
    class Meta:
        label = 'admin'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage administrator accounts'

    # @property
    # def _client(self) -> RoleAPI:
    #     return self.app.client.roles

    @ex(help='list administrators')
    def list(self):
        pass
