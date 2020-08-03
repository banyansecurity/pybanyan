from cement import Controller, ex


class NetagentController(Controller):
    class Meta:
        label = 'netagent'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage netagents (AccessTiers and HostAgents)'

    # @property
    # def _client(self) -> RoleAPI:
    #     return self.app.client.roles

    @ex(help='list netagents')
    def list(self):
        pass
