from datetime import datetime
from typing import List

from cement import Controller, ex

from banyan.api.audit import AuditAPI
from banyan.model.audit import AuditEvent, AuditAction, AuditEventType


class AuditController(Controller):
    class Meta:
        label = 'audit'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'retrieve audit logs'

    @property
    def _client(self) -> AuditAPI:
        return self.app.client.audit

    @ex(help='list events',
        arguments=[
            (['--type'],
             {
                 'help': 'Filters by admin activity type.',
                 'choices': AuditEventType.choices(),
             }),
            (['--action'],
             {
                 'help': 'Filters events by one of the possible event action values.',
                 'choices': AuditAction.choices(),
             }),
            (['--admin-email'],
             {
                 'help': 'Filters by Admin email address.',
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
        ]
        )
    def list(self):
        events: List[AuditEvent] = self._client.list(before_dt=self.app.pargs.before, after_dt=self.app.pargs.after,
                                                     event_type=self.app.pargs.type, action=self.app.pargs.action,
                                                     admin_email=self.app.pargs.admin_email)
        event_json = AuditEvent.Schema().dump(events, many=True)
        self.app.render(event_json, handler='json', indent=2, sort_keys=True)
