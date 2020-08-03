from typing import List

from cement import Controller, ex

from banyan.api.service import ServiceAPI
from banyan.controllers.base import Base
from banyan.model.service import ServiceInfo, Service


class ServiceController(Controller):
    class Meta:
        label = 'service'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage web and TCP services and workloads'

    @property
    def _client(self) -> ServiceAPI:
        return self.app.client.services

    @ex(help='list registered services')
    def list(self):
        services: List[ServiceInfo] = self._client.list()
        results = list()
        headers = ['Name', 'ID', 'Type', 'Enabled', 'Created', 'Last Updated']
        for service in services:
            app_type = service.service.metadata.tags.service_app_type
            new_row = [service.service_name, service.service_id, app_type, service.enabled,
                       service.created_at.strftime(Base.TABLE_DATE_FORMAT),
                       service.last_updated_at.strftime(Base.TABLE_DATE_FORMAT)]
            results.append(new_row)
        results.sort(key=lambda x: x[0])
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='show the definition of a registered service',
        arguments=[
            (['service_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service to display.'
             }),
        ])
    def get(self):
        info: ServiceInfo = self._client[self.app.pargs.service_name]
        service_json = Service.Schema().dump(info.service)
        # colorized_json = highlight(service_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(service_json, handler='json', indent=2, sort_keys=True)

    @ex(help='create a new service from a JSON specification',
        arguments=[
            (['service_spec'],
             {
                 'help': 'JSON blob describing the new service to be created, or a filename '
                         'containing JSON prefixed by "@" (example: @service.json).'
             }),
        ])
    def create(self):
        spec = Base.get_json_input(self.app.pargs.service_spec)
        service = Service.Schema().load(spec)
        info = self._client.create(service)
        self.app.render(ServiceInfo.Schema().dump(info), handler='json', indent=2, sort_keys=True)

    @ex(help='update an existing service from a JSON specification',
        arguments=[
            (['service_spec'],
             {
                 'help': 'JSON blob describing the service to be updated, or a filename '
                         'containing JSON prefixed by "@" (example: @service.json).'
             }),
        ])
    def update(self):
        spec = Base.get_json_input(self.app.pargs.service_spec)
        service = Service.Schema().load(spec)
        info = self._client.update(service)
        self.app.render(ServiceInfo.Schema().dump(info), handler='json', indent=2, sort_keys=True)

    @ex(help='delete a service',
        arguments=[
            (['service_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service to delete.'
             }),
        ])
    def delete(self):
        service: ServiceInfo = self._client[self.app.pargs.service_name]
        self.app.print(self._client.delete(service))

    @ex(help='enable a service',
        arguments=[
            (['service_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service to enable.'
             }),
        ])
    def enable(self):
        service: ServiceInfo = self._client[self.app.pargs.service_name]
        self.app.print(self._client.enable(service))

    @ex(help='disable a service',
        arguments=[
            (['service_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service to disable.'
             }),
        ])
    def disable(self):
        service: ServiceInfo = self._client[self.app.pargs.service_name]
        self.app.print(self._client.disable(service))

    @ex(help='attach a policy to a service',
        arguments=[
            (['service_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service to attach a policy to.',
             }),
            (['policy_name'],
             {
                 'metavar': 'policy_name_or_id',
                 'help': 'Name or ID of the policy to attach to the service.',
             }),
            (['--permissive'],
             {
                 'action': 'store_false',
                 'dest': 'enforcing',
                 'help': 'Set the policy to permissive mode (allow all traffic and log any unauthorized access).',
             }),
            (['--enforcing'], {
                'action': 'store_true',
                'dest': 'enforcing',
                'default': True,
                'help': 'Set the policy to enforcing mode (deny unauthorized access).',
            }),
        ])
    def attach_policy(self):
        result = self._client.attach(self.app.pargs.service_name, self.app.pargs.policy_name, self.app.pargs.enforcing)
        mode = 'ENFORCING' if result.enabled else 'PERMISSIVE'
        self.app.print(f'Policy {result.policy_id} attached to service {result.service_id} in {mode} mode.')

    @ex(help='detach the active policy from a service',
        arguments=[
            (['service_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service to attach a policy to.',
             }),
            (['policy_name'],
             {
                 'metavar': 'policy_name_or_id',
                 'help': 'Name or ID of the policy to attach to the service.',
             }),
        ])
    def detach_policy(self):
        self.app.print(self._client.detach(self.app.pargs.service_name, self.app.pargs.policy_name))

    @ex(help='run sanity checks on a service')
    def test(self):
        pass
