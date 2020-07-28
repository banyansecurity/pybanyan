from typing import List

from cement import Controller, ex

from banyan.api import PolicyAPI
from banyan.model.policy import PolicyInfo


class PolicyController(Controller):
    class Meta:
        label = 'policy'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage authorization policies for users and workloads'

    @property
    def _client(self) -> PolicyAPI:
        return self.app.client.policies

    @ex(help='create a new policy')
    def create(self):
        pass

    @ex(help='delete a policy')
    def delete(self):
        pass

    @ex(help='list policies')
    def list(self):
        policies: List[PolicyInfo] = self._client.list()
        results = list()
        headers = ['Name', 'ID', 'Created', 'Last Updated']
        for policy in policies:
            new_row = [policy.name, policy.id,
                       policy.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                       policy.last_updated_at.strftime("%Y-%m-%d %H:%M:%S")]
            results.append(new_row)
        results.sort(key=lambda x: x[0])
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='update an existing policy')
    def update(self):
        pass

    @ex(help='enable a policy')
    def enable(self):
        pass

    @ex(help='disable a policy')
    def disable(self):
        pass

    @ex(help='show services attached to a policy')
    def list_attached(self):
        pass