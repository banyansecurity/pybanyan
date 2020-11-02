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

    # TODO: implement /security_events
    @ex(help='list events')
    def list(self):
        pass

    # TODO: implement /security_events_type_count
    @ex(help='show summary of events in database')
    def summary(self):
        pass
