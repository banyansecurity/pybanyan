from typing import List

from cement import Controller, ex

from banyan.api.service import ServiceAPI
from banyan.controllers.base import Base
from banyan.model.service import ServiceInfo, Service
from banyan.lib.service import DEFAULT_TIMEOUT, DEFAULT_DNS_SERVER, ServiceTest
from banyan.lib.cloud import has_cloud


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
        service: ServiceInfo = Service.Schema().load(spec)
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
        service: ServiceInfo = Service.Schema().load(spec)
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

    @ex(help='run sanity checks on a service',
        hide=not has_cloud,
        arguments=[
            (['service_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service to attach a policy to.',
             }),
            (['--timeout'],
             {
                 'type': float,
                 'help': 'Length of time to wait for backend service to respond, in seconds. '
                         f'(default: {DEFAULT_TIMEOUT})',
                 'default': DEFAULT_TIMEOUT
             }),
            (['--external-dns'],
             {
                 'help': 'Public DNS server to query for service resolution. '
                         f'(default: {DEFAULT_DNS_SERVER})',
                 'default': DEFAULT_DNS_SERVER
             }),
            (['--wildcard'],
             {
                 'help': 'Hostname to substitute for wildcard in service spec (e.g. *.bnndemos.com).'
             })
        ])
    def test(self):
        info = self._client[self.app.pargs.service_name]
        harness = ServiceTest(info.service, self.app.client,
                              self.app.pargs.timeout, self.app.pargs.external_dns,
                              self.app.pargs.wildcard)
        harness.run()

    @ex(help='create an Okta Bookmark Application from a web service',
        arguments=[
            (['service_name'],
            {
                'help': 'name of service to add to Okta.'
            }),
            (['group_name'],
            {
                'help': 'Okta group to assign application access.'
            }),            
        ])
    def bookmark_okta(self):
        try:
            from banyan.ext.idp.okta import OktaApplicationController
        except Exception as ex:
            raise NotImplementedError("Okta SDK not configured correctly > %s" % ex.args[0])

        self._client.list()
        service_info: ServiceInfo = self._client[self.app.pargs.service_name]
        if not service_info.service.spec.http_settings.oidc_settings.enabled:
            raise RuntimeError('Service needs to be of type WEB')

        Base.wait_for_input(True, 'Get service to add to Okta:')
        svc = service_info.service
        service_json = Service.Schema().dump(svc)
        self.app.render(service_json, handler='json', indent=2, sort_keys=True)

        Base.wait_for_input(True, 'Adding to Okta and assigning group.')
        okta = OktaApplicationController()
        okta_app = okta.create_bookmark(svc.name, svc.spec.http_settings.oidc_settings.service_domain_name)
        print(okta_app)
        okta_assignment = okta.assign(okta_app.id, self.app.pargs.group_name)
        print(okta_assignment)

        print('\n--> Bookmark to Okta successful.')


    @ex(help='create an Azure AD Linked Sign-on from a web service',
    arguments=[
        (['service_name'],
        {
            'help': 'name of service to add to Azure AD.'
        }),
        (['group_name'],
        {
            'help': 'Azure AD group to assign application access.'
        }),            
    ])
    def bookmark_aad(self):
        try:
            from banyan.ext.idp.azure_ad import AzureADApplicationController
        except Exception as ex:
            raise NotImplementedError("Azure AD Microsoft Graph SDK not configured correctly > %s" % ex.args[0]) 

        self._client.list()
        service_info: ServiceInfo = self._client[self.app.pargs.service_name]
        if not service_info.service.spec.http_settings.oidc_settings.enabled:
            raise RuntimeError('Service needs to be of type WEB')

        Base.wait_for_input(True, 'Get service to add to AzureAD:')
        svc = service_info.service
        service_json = Service.Schema().dump(svc)
        self.app.render(service_json, handler='json', indent=2, sort_keys=True)

        Base.wait_for_input(True, 'Adding to Azure AD and assigning group.')
        aad = AzureADApplicationController()
        aad_app = aad.create_bookmark(svc.name, svc.spec.http_settings.oidc_settings.service_domain_name)
        print(aad_app)

        print('\n--> Bookmark to Azure AD successful.')
        
