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
                'help': 'Filter discovered resource by Tag Name.'
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
            (['resource_udid'],
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
            (['resource_type'],
            {
                'help': 'Type of AWS Resource - EC2 | RDS | LB | ALL.'
            }),
            (['--tag_name'],
            {
                'help': 'Only sync resources with specific tag name'
            }),
            (['--tag_value'],
            {
                'help': 'Only sync resources with specific tag values ("*" is allowed).'
            })

        ])
    def sync_aws(self):
        try:
            from banyan.ext.aws.ec2 import Ec2Controller
        except Exception as ex:
            raise NotImplementedError("AWS SDK not configured correctly > %s" % ex.args[0])

        ec2 = Ec2Controller()
        ec2.list()
        #TODO: Call create in a loop
        return


    @ex(help='use discovered_resource to create a new service',
        arguments=[
            (['service_name'],
            {
                'help': 'Name of service to create.'
            }),       
            (['service_type'],
            {
                'help': 'Type of service to create - WEB | SSH | RDS | GENERIC_TCP.'
            }),
            (['resource_udid'],
            {
                'help': 'Banyan UDID of the discovered resource to use.'
            }),         
            (['--backend_port'],
            {
                'help': 'Specify if backend port is non-standard.'
            }),
            (['--backend_tls'],
            {
                'default': False,
                'help': 'Specify if backend requires TLS.'
            })            
        ])
    def publish(self):
        #TODO: get resource, logic to create service
        return

    @ex(help='add a discovered_resource to an existing service whitelist',
        arguments=[
            (['service_name'],
            {
                'help': 'Name of service whose whitelist should be updated.'
            }),          
            (['tag_name'],
            {
                'help': 'Name of Tag of the discovered resources to use.'
            }),
            (['tag_value'],
            {
                'help': 'Value of Tag of the discovered resources to use ("*" is allowed).'
            })
        ])
    def whitelist(self):
        #TODO: get resource(s), check service if it has whitelist
        return