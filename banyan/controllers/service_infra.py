from typing import List

from cement import Controller, ex

from banyan.api.service_infra import ServiceInfraAPI
from banyan.controllers.base import Base
from banyan.model.service import ServiceInfo, Service
from banyan.model.service_infra import ServiceInfraSSH, ServiceInfraRDP, ServiceInfraK8S, ServiceInfraDatabase, ServiceInfraTCP

class ServiceInfraController(Controller):
    class Meta:
        label = 'service_infra'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage infrastructure services'

    @property
    def _client(self) -> ServiceInfraAPI:
        return self.app.client.services_infra

    @ex(help='list infrastructure services')
    def list(self):
        services: List[ServiceInfo] = self._client.list()
        results = list()
        headers = ['Name', 'ID', 'Type', 'Enabled', 'Created', 'Last Updated']
        for service in services:
            app_type = service.service_spec.metadata.tags.service_app_type
            new_row = [service.service_name, service.service_id, app_type, service.enabled,
                       service.created_at.strftime(Base.TABLE_DATE_FORMAT),
                       service.last_updated_at.strftime(Base.TABLE_DATE_FORMAT)]
            results.append(new_row)
        results.sort(key=lambda x: x[0])
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')


    @ex(help='show the definition of a infrastructure service',
        arguments=[
            (['service_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service to display.'
             }),
        ])
    def get(self):
        info: ServiceInfo = self._client[self.app.pargs.service_name]
        service_json = Service.Schema().dump(info.service_spec)
        # colorized_json = highlight(service_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(service_json, handler='json', indent=2, sort_keys=True)


    @ex(help='create a new infrastructure service from a JSON specification',
        arguments=[
            (['service_spec'],
             {
                 'help': 'JSON blob describing the new service to be created, or a filename '
                         'containing JSON prefixed by "@" (example: @service.json).'
             }),
        ])
    def create(self):
        spec = Base.get_json_input(self.app.pargs.service_spec)
        service: ServiceInfo = Service.Schema().load(spec)
        info = self._client.create(service)
        self.app.render(ServiceInfo.Schema().dump(info), handler='json', indent=2, sort_keys=True)


    @ex(help='update an existing infrastructure service from a JSON specification',
        arguments=[
            (['service_spec'],
             {
                 'help': 'JSON blob describing the service to be updated, or a filename '
                         'containing JSON prefixed by "@" (example: @service.json).'
             }),
        ])
    def update(self):
        spec = Base.get_json_input(self.app.pargs.service_spec)
        service: ServiceInfo = Service.Schema().load(spec)
        info = self._client.update(service)
        self.app.render(ServiceInfo.Schema().dump(info), handler='json', indent=2, sort_keys=True)

    @ex(help='delete an infrastructure service',
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

    @ex(help='enable an infrastructure service',
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

    @ex(help='disable an infrastructure service',
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

    @ex(help='attach a policy to an infrastructure service',
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
        self.app.print(f'Policy {result.policy_id} attached to service {self.app.pargs.service_name} in {mode} mode.')

    @ex(help='detach the active policy from an infrastructure service',
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


    @ex(help='quick create a new SSH infrastructure service',
        arguments=ServiceInfraSSH.arguments()
        )
    def quick_create_ssh(self):
        svc = ServiceInfraSSH()
        Base.assign_pargs_to_object(self.app.pargs, svc)
        Base.wait_for_input(True, 'Creating an infrastructure service: ' + str(svc))
        info = self._client.create(svc.service_obj())
        self.app.render(ServiceInfo.Schema().dump(info), handler='json', indent=2, sort_keys=True)


    @ex(help='quick create a new K8S infrastructure service',
        arguments=ServiceInfraK8S.arguments()
        )
    def quick_create_k8s(self):
        svc = ServiceInfraK8S()
        Base.assign_pargs_to_object(self.app.pargs, svc)
        Base.wait_for_input(True, 'Creating an infrastructure service: ' + str(svc))
        info = self._client.create(svc.service_obj())
        self.app.render(ServiceInfo.Schema().dump(info), handler='json', indent=2, sort_keys=True)


    @ex(help='quick create a new RDP infrastructure service',
        arguments=ServiceInfraRDP.arguments()
        )
    def quick_create_rdp(self):
        svc = ServiceInfraRDP()
        Base.assign_pargs_to_object(self.app.pargs, svc)
        Base.wait_for_input(True, 'Creating an infrastructure service: ' + str(svc))
        info = self._client.create(svc.service_obj())
        self.app.render(ServiceInfo.Schema().dump(info), handler='json', indent=2, sort_keys=True)

    @ex(help='quick create a new Database infrastructure service',
        arguments=ServiceInfraDatabase.arguments()
        )
    def quick_create_db(self):
        svc = ServiceInfraDatabase()
        Base.assign_pargs_to_object(self.app.pargs, svc)
        Base.wait_for_input(True, 'Creating an infrastructure service: ' + str(svc))
        info = self._client.create(svc.service_obj())
        self.app.render(ServiceInfo.Schema().dump(info), handler='json', indent=2, sort_keys=True)

    @ex(help='quick create a new Generic TCP infrastructure service',
        arguments=ServiceInfraTCP.arguments()
        )
    def quick_create_tcp(self):
        svc = ServiceInfraTCP()
        Base.assign_pargs_to_object(self.app.pargs, svc)
        Base.wait_for_input(True, 'Creating an infrastructure service: ' + str(svc))
        info = self._client.create(svc.service_obj())
        self.app.render(ServiceInfo.Schema().dump(info), handler='json', indent=2, sort_keys=True)
        