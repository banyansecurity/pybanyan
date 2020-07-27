from cement import Controller, App, ex
from cement.core.config import ConfigInterface
from banyan.api import BanyanApiClient
from typing import List, Dict
from banyan.model.service import ServiceInfo, Service
import sys
# from banyan.model.custom_types import JSONType
import json
from banyan.api.services import ServiceAPI


class ServiceController(Controller):
    class Meta:
        label = 'service'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage web and TCP services and workloads'

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    @property
    def _client(self) -> ServiceAPI:
        return self.app.client.services

    # noinspection PyMethodMayBeStatic
    def _get_json_input(self, arg: str):
        if arg[0] == '@':
            arg = open(arg[1:]).read()
        elif arg == '-':
            arg = sys.stdin.read()
        else:
            arg = arg.encode('utf-8')
        return json.loads(arg)

    @ex(help='create a new service from a JSON specification',
        arguments=[
            (['service_spec'],
             {
                 'help': 'JSON blob describing a new service to be registered with Banyan, or a filename '
                         'containing JSON prefixed by "@" (example: @service.json).'
             }),
        ])
    def create(self):
        service_spec = self._get_json_input(self.app.pargs.service_spec)
        service = Service.from_json(service_spec)
        service_info = self._client.insert(service)
        self.app.render(service_info.as_json(), handler='json')

    @ex(help='update an existing service from a JSON specification',
        arguments=[
            (['service_spec'],
             {
                 'help': 'JSON blob describing a new service to be registered with Banyan, or a filename '
                         'containing JSON prefixed by "@" (example: @service.json).'
             }),
        ])
    def update(self):
        service_spec = self._get_json_input(self.app.pargs.service_spec)
        service = Service.from_json(service_spec)
        service_info = self._client.update(service)
        self.app.render(service_info.as_json(), handler='json')

    @ex(help='delete a service',
        arguments=[
            (['service_name'],
             {}),
        ])
    def delete(self):
        service_name = self.app.pargs.service_name
        service = self._client[service_name]
        self.app.print(self._client.delete(service))

    @ex(help='list registered services')
    def list(self):
        services: List[ServiceInfo] = self._client.list()
        results = list()
        json_results = list()
        headers = ['Name', 'ID', 'Type', 'Created', 'Last Updated']
        for service in services:
            new_row = [service.name, service.service_id, service.service.metadata.tags.service_app_type,
                       service.created_at, service.last_updated_at]
            results.append(new_row)
            json_results.append(service.Schema().dump(service))

        results.sort(key=lambda x: x[0])

        self.app.render(results, headers=headers, handler='tabulate', tablefmt='simple')
        # self.app.render(json_results, handler='json')

        # app: App = self.app
        # conf: ConfigInterface = app.config
        # if app.Meta.output_handler == 'json':
        #     self.app.render({'api_url': conf.get('banyan', 'api_url'),
        #                      'refresh_token': conf.get('banyan', 'refresh_token')}, handler='json')
        # elif app.Meta.output_handler == 'tabulate':
        #     self.app.render([[conf.get('banyan', 'api_url'), conf.get('banyan', 'refresh_token')]],
        #                     headers=['API Url', 'Refresh Token'], handler='tabulate', tablefmt='simple')

    @ex(help='enable a service',
        arguments=[
            (['service_name'],
             {}),
        ])
    def enable(self):
        service_name = self.app.pargs.service_name
        service = self._client[service_name]
        self.app.print(self._client.enable(service))

    @ex(help='disable a service',
        arguments=[
            (['service_name'],
             {}),
        ])
    def disable(self):
        service_name = self.app.pargs.service_name
        service = self._client[service_name]
        self.app.print(self._client.disable(service))

    @ex(help='attach a policy to a service',
        arguments=[
            (['service_name'],
             {}),
            (['--policy-name'],
             {}),
            (['--policy-id'],
             {})
        ])
    def attach(self):
        print(self.app.pargs.policy_name)
        pass

    @ex(help='detach the policy from a service',
        arguments=[
            (['service_name'], {})
        ])
    def detach(self):
        service_name = self.app.pargs.service_name
        pass

    @ex(help='run sanity checks on a service')
    def test(self):
        pass
