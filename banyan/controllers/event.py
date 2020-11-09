from datetime import datetime
from typing import List

from cement import Controller, ex

from banyan.api.event_v2 import EventV2API
from banyan.model.event_v2 import EventV2, EventV2Type, EventV2Subtype


class EventV2Controller(Controller):
    class Meta:
        label = 'event'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'report on security events'

    @property
    def _client(self) -> EventV2API:
        return self.app.client.events

    @ex(help='list events',
        arguments=[
            (['--type'],
             {
                 'help': 'Filters events of one event type.',
                 'choices': EventV2Type.choices(),
             }),
            (['--subtype'],
             {
                 'help': 'Filters events of one subtype (conditionally depends on type).',
                 'choices': EventV2Subtype.choices(),
             }),
            (['--action'],
             {
                 'help': 'Filters events by one of the possible event action values (e.g. "grant", "deny").',
             }),
            (['--email'],
             {
                 'help': 'Filters events associated with a single user, based on their email address.',
             }),
            (['--device-id'],
             {
                 'help': 'Filters events associated with a single device, based on its device ID.',
             }),
            (['--serial-number'],
             {
                 'help': 'Filters events associated with a single device, based on its serial number.',
             }),
            (['--container-id'],
             {
                 'help': 'Filters events associated with a single workload, based on its container ID.',
             }),
            (['--service-name'],
             {
                 'help': 'Filters events associated with a single service, based on its service name.',
             }),
            (['--event-id'],
             {
                 'help': 'Retrieve a single event based on its event ID.',
             }),
            (['--before'],
             {
                 'help': 'Filters events that occurred before a specific time.',
                 'type': datetime.fromisoformat,
             }),
            (['--after'],
             {
                 'help': 'Filters events that occurred after a specific time.',
                 'type': datetime.fromisoformat,
             }),
            (['--order'],
             {
                 'help': 'Sets the order for returned events based on created_at timestamp. Supported values '
                         'ASC, DESC. Default is DESC.',
                 'choices': ('ASC', 'DESC')
             }),
        ]
        )
    def list(self):
        events: List[EventV2] = self._client.list(before_dt=self.app.pargs.before, after_dt=self.app.pargs.after,
                                                  order=self.app.pargs.order, event_type=self.app.pargs.type,
                                                  subtype=self.app.pargs.subtype,
                                                  action=self.app.pargs.action, email_address=self.app.pargs.email,
                                                  device_id=self.app.pargs.device_id,
                                                  device_serial=self.app.pargs.serial_number,
                                                  container_id=self.app.pargs.container_id,
                                                  service_name=self.app.pargs.service_name,
                                                  event_id=self.app.pargs.event_id)
        event_json = EventV2.Schema().dump(events, many=True)
        self.app.render(event_json, handler='json', indent=2, sort_keys=True)
