from datetime import datetime
from typing import List
import os

from cement import Controller, ex

from banyan.api import BanyanApiClient
from banyan.model.service import ServiceInfo


class ExportController(Controller):
    class Meta:
        label = 'export'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'export all objects from an organization'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client

    @ex(help='export all objects from an organization',
        arguments=[
            (['--path'],
             {
                 'help': 'Directory to place the object JSON files.',
                 'default': os.getcwd()
             }),
        ]
        )
    def all(self):
        self.roles()
        self.policies()
        self.services()

    @ex(help='export roles from an organization',
        arguments=[
            (['--path'],
             {
                 'help': 'Directory to place the object JSON files.',
                 'default': os.getcwd()
             }),
        ]
        )
    def roles(self):
        role_path = self._mkdir('roles')
        self.app.print(f' * Exporting roles to {role_path}')
        all_roles = self._client.roles.list()
        for role in all_roles:
            with open(self._mkfile(role_path, f'{role.name}.role.json'), 'w') as f:
                f.write(role.role.Schema().dumps(role.role))

    @ex(help='export policies from an organization',
        arguments=[
            (['--path'],
             {
                 'help': 'Directory to place the object JSON files.',
                 'default': os.getcwd()
             }),
        ]
        )
    def policies(self):
        policy_path = self._mkdir('policies')
        self.app.print(f' * Exporting policies to {policy_path}')
        all_policies = self._client.policies.list()
        for policy in all_policies:
            with open(self._mkfile(policy_path, f'{policy.name}.policy.json'), 'w') as f:
                f.write(policy.policy.Schema().dumps(policy.policy))

    @ex(help='export services from an organization',
        arguments=[
            (['--path'],
             {
                 'help': 'Directory to place the object JSON files.',
                 'default': os.getcwd()
             }),
        ]
        )
    def services(self):
        service_path = self._mkdir('services')
        self.app.print(f' * Exporting services to {service_path}')
        all_services = self._client.services.list()
        for service in all_services:
            with open(self._mkfile(service_path, f'{service.name}.service.json'), 'w') as f:
                f.write(service.service.Schema().dumps(service.service))

    def _mkdir(self, subdir: str) -> str:
        path = os.path.join(self.app.pargs.path, subdir)
        os.makedirs(path, exist_ok=True)
        return os.path.abspath(path)

    def _mkfile(self, path: str, fname: str) -> str:
        fname = fname.replace(' ', '_')
        return os.path.join(path, fname)
