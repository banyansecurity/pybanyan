from typing import List

from cement import Controller, ex

from banyan.api import PolicyAPI, AttachmentAPI
from banyan.controllers.base import Base
from banyan.model.policy import PolicyInfo, Policy


class PolicyController(Controller):
    class Meta:
        label = 'policy'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage authorization policies for users and workloads'

    @property
    def _client(self) -> PolicyAPI:
        return self.app.client.policies

    @ex(help='list policies')
    def list(self):
        policies: List[PolicyInfo] = self._client.list()
        results = list()
        headers = ['Name', 'ID', 'Created', 'Last Updated']
        for policy in policies:
            new_row = [policy.policy_name, policy.policy_id,
                       policy.created_at.strftime(Base.TABLE_DATE_FORMAT),
                       policy.last_updated_at.strftime(Base.TABLE_DATE_FORMAT)]
            results.append(new_row)
        results.sort(key=lambda x: x[0])
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='show the definition of a policy',
        arguments=[
            (['policy_name'],
             {
                 'metavar': 'policy_name_or_id',
                 'help': 'Name or ID of the policy to display.'
             }),
        ])
    def get(self):
        info: PolicyInfo = self._client[self.app.pargs.policy_name]
        policy_json = Policy.Schema().dump(info.policy)
        # colorized_json = highlight(policy_json, lexers.JsonLexer(), formatters.Terminal256Formatter(style="default"))
        self.app.render(policy_json, handler='json', indent=2, sort_keys=True)

    @ex(help='create a new policy from a JSON specification',
        arguments=[
            (['policy_spec'],
             {
                 'help': 'JSON blob describing the new policy to be created, or a filename '
                         'containing JSON prefixed by "@" (example: @service.json).'
             }),
        ])
    def create(self):
        policy_spec = Base.get_json_input(self.app.pargs.policy_spec)
        policy = Policy.Schema().load(policy_spec)
        policy_info = self._client.create(policy)
        self.app.render(PolicyInfo.Schema().dump(policy_info), handler='json', indent=2, sort_keys=True)

    @ex(help='update an existing policy',
        arguments=[
            (['policy_spec'],
             {
                 'help': 'JSON blob describing the policy to be updated, or a filename '
                         'containing JSON prefixed by "@" (example: @service.json).'
             }),
        ])
    def update(self):
        policy_spec = Base.get_json_input(self.app.pargs.policy_spec)
        policy = Policy.Schema().load(policy_spec)
        policy_info = self._client.update(policy)
        self.app.render(PolicyInfo.Schema().dump(policy_info), handler='json', indent=2, sort_keys=True)

    @ex(help='delete a policy',
        arguments=[
            (['policy_name'],
             {
                 'metavar': 'policy_name_or_id',
                 'help': 'Name or ID of the policy to delete.'
             }),
        ])
    def delete(self):
        policy: PolicyInfo = self._client[self.app.pargs.policy_name]
        self.app.print(self._client.delete(policy))

    @ex(help='show services attached to a policy',
        arguments=[
            (['policy_name'],
             {
                 'metavar': 'policy_name_or_id',
                 'help': 'Name or ID of the policy to delete.'
             }),
        ])
    def list_attachments(self):
        policy: PolicyInfo = self._client[self.app.pargs.policy_name]
        attach_api: AttachmentAPI = self.app.client.attachments
        attachments = attach_api.list()
        results = list()
        headers = ['Object Name', 'Object ID', 'Type', 'Attached At', 'Attached By']
        for a in attachments:
            if a.policy_id == policy.id:
                new_row = [a.attached_to_name, a.attached_to_id, a.attached_to_type,
                           a.attached_at.strftime(Base.TABLE_DATE_FORMAT), a.attached_by]
                results.append(new_row)
        results.sort(key=lambda x: x[0])
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='attach a policy to a service',
        arguments=[
            (['policy_name'],
             {
                 'metavar': 'policy_name_or_id',
                 'help': 'Name or ID of the policy to attach to the service.',
             }),
            (['service_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service to attach a policy to.',
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
    def attach_to_service(self):
        info = self._client.attach(self.app.pargs.policy_name, self.app.pargs.service_name, self.app.pargs.enforcing)
        mode = 'ENFORCING' if info.enabled else 'PERMISSIVE'
        self.app.print(f'Policy {info.policy_id} attached to service {info.service_id} in {mode} mode.')

    @ex(help='detach the policy from a service',
        arguments=[
            (['policy_name'],
             {
                 'metavar': 'policy_name_or_id',
                 'help': 'Name or ID of the policy to attach to the service.',
             }),
            (['service_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service to attach a policy to.',
             }),
        ])
    def detach_from_service(self):
        self.app.print(self._client.detach(self.app.pargs.policy_name, self.app.pargs.service_name))
