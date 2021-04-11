from typing import List

from cement import Controller, ex

from banyan.api.d_resource import DiscoveredResourceAPI
from banyan.controllers.base import Base
from banyan.model.d_resource import DiscoveredResource, DiscoveredResourceInfo

class DiscoveredResourceController(Controller):
    class Meta:
        label = 'd_resource'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage discovered resources'

    @property
    def _client(self) -> DiscoveredResourceAPI:
        return self.app.client.discovered_resources

    @ex(help='list discovered_resources',
        arguments=[
            (['--tag-name'], 
            {
                'help': 'Banyan UDID of the discovered resource to display.'
            }),
        ])
    def list(self):
        d_resources: List[DiscoveredResourceInfo] = self._client.list(params={'include_tags': 'true', 'tag_name': self.app.pargs.tag_name})
        results = list()
        headers = ['Name', 'ID', 'Cloud', 'Region', 'Type', 'Private IP', '# Tags']
        for res in d_resources:
            new_res = [res.name, res.resource_udid, res.cloud_provider, res.region,
                    res.resource_type, res.private_ip, len(res.tags)]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='show details & tags of a discovered_resource', 
        arguments=[
            (['--resource_udid'], 
            {
                'help': 'Banyan UDID of the discovered resource to display.'
            }),
        ])
    def get(self):
        d_resource: DiscoveredResourceInfo = self._client[self.app.pargs.resource_udid]
        tags = d_resource.tags
        headers = ['Name', 'Value']
        self.app.render(tags, handler='tabulate', headers=headers, tablefmt='simple')

    @ex(help='create a new discovered_resource',
        arguments=[
            (['resources_json'], 
            {
                'help': 'JSON blob describing the new discovered resource(s) to be created, or a filename '
                         'containing JSON prefixed by "@" (example: @res.json).'
            }),
        ])
    def create(self):
        d_resources = Base.get_json_input(self.app.pargs.resources_json)
        info = self._client.create(d_resources)
        print(info)

    @ex(help='sync discovered_resources with AWS',
        arguments=[
            (['--resource_types'],
            {
                'help': 'Only supports EC2'
            }),
            (['--tag_name'],
            {
                'help': 'Filter resources by AWS Tag'
            }),
        ])
    def sync_aws(self):
        try:
            from banyan.ext.aws.ec2 import Ec2Controller
        except Exception as ex:
            raise NotImplementedError("AWS SDK not configured correctly > %s" % ex.args[0])

        ec2 = Ec2Controller()
        ec2.list()


    @ex(help='add a discovered_resource to a Banyan Service',
        arguments=[
            (['--cloud-provider'], {
                'help': ''
            }),
            (['--filter'], {
                'help': ''
            })
        ])
    def publish(self):
        return
