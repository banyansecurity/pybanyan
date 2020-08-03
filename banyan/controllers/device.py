from cement import Controller, ex


class DeviceController(Controller):
    class Meta:
        label = 'device'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage devices'

    # @property
    # def _client(self) -> RoleAPI:
    #     return self.app.client.roles

    @ex(help='list devices')
    def list(self):
        pass
