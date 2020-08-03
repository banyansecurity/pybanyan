from cement import Controller, ex


class EventV1Controller(Controller):
    class Meta:
        label = 'event'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'report on security and audit events'

    # @property
    # def _client(self) -> RoleAPI:
    #     return self.app.client.roles

    @ex(help='list events')
    def list(self):
        pass
