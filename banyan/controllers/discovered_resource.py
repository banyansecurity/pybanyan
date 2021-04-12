from typing import List
import copy
from time import sleep

from cement import Controller, ex

from banyan.controllers.base import Base

from banyan.api import BanyanApiClient
from banyan.model.discovered_resource import DiscoveredResource, DiscoveredResourceInfo
from banyan.model.service import ServiceInfo, SimpleWebService
from banyan.model.policy import PolicyInfo, SimpleWebPolicy


class DiscoveredResourceController(Controller):
    class Meta:
        label = 'discovered_resource'
        aliases = ['dr']
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage discovered resources'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client

    @ex(help='list discovered_resources',
        arguments=[
            (['--tag_name'], 
            {
                'help': 'Filter discovered resource by Tag Name.'
            }),
        ])
    def list(self):
        d_resources: List[DiscoveredResourceInfo] = self._client.discovered_resources.list(params={'include_tags': 'true', 'tag_name': self.app.pargs.tag_name})
        results = list()
        headers = ['Name', 'ID', 'Cloud', 'Region', 'Type', 'Private IP', 'Public IP', '# Tags']
        for res in d_resources:
            new_res = [res.name, res.resource_udid, res.cloud_provider, res.region,
                    res.resource_type, res.private_ip, res.public_ip, len(res.tags)]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')


    #TODO-API: argument should be UDID not tag_name
    @ex(help='show details & tags of a discovered_resource', 
        arguments=[
            (['tag_name'],
            {
                'help': 'Filter discovered resource by Tag Name.'
            }),
            (['--tag_value'],
            {
                'help': 'Filter discovered resource by Tag Value.',
                'default': ''
            }),
            (['--resource_uuid'],
            {
                'help': 'Filter discovered resource by Banyan UUID.'
            }),            
        ])
    def get(self):
        params = {
            'include_tags': 'true', 
            'tag_name': self.app.pargs.tag_name,
            'tag_value': self.app.pargs.tag_value
        }
        d_resources: List[DiscoveredResourceInfo] = self._client.discovered_resources.list(params=params)
        d_resource: DiscoveredResourceInfo = None
        if len(d_resources):
            d_resource = d_resources[0]
            print(vars(d_resource))
        else:
            print('No discovered_resource found.')


    @ex(help='create a new discovered_resource',
        arguments=[
            (['resources_json'], 
            {
                'help': 'JSON blob describing the new discovered resource(s) to be created, or a filename '
                         'containing JSON prefixed by "@" (example: @res.json).'
            }),
        ])
    def create(self):
        d_resource = Base.get_json_input(self.app.pargs.resources_json)
        info = self._client.discovered_resources.create(d_resource)
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
            from banyan.ext.aws.ec2 import Ec2Controller, Ec2Model
        except Exception as ex:
            raise NotImplementedError("AWS SDK not configured correctly > %s" % ex.args[0])

        ec2 = Ec2Controller()
        instances = ec2.list()

        print('\n--> List of AWS Resources')
        results = list()
        for instance in instances:
            allvars = vars(copy.copy(instance))
            allvars['tags'] = len(allvars['tags'])
            results.append(allvars)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        for instance in instances:
            res_tags = []
            for tag in instance.tags:
                res_tag = {
                    'name': tag['Key'],
                    'value': tag['Value']
                }
                res_tags.append(res_tag)

            res = DiscoveredResource(instance.cloud_provider,
                                     instance.region,
                                     instance.resource_id,
                                     instance.resource_name,
                                     instance.resource_type,
                                     instance.public_ip,
                                     instance.private_ip,
                                     res_tags
                                     )
            print('\n--> Syncing Discovered Resource')
            self.app.render(DiscoveredResource.Schema().dump(res), handler='json')
            info = self._client.discovered_resources.create(res)
            print('\n-->', info)
            sleep(0.05)

    #TODO-API: argument should be UDID not tag_name
    @ex(help='use discovered_resource to create a new service',
        arguments=[
            (['service_name'],
            {
                'help': 'Name of service to create.'
            }),
            (['service_domain'],
            {
                'help': 'Domain name of service, ex: corp.org.com (no https://).'
            }),                  
            (['service_type'],
            {
                'help': 'Type of service - WEB | SSH | RDS | GENERIC_TCP.'
            }),
            (['tag_name'],
            {
                'help': 'Tag name of discovered resource.'
            }),
            (['--tag_value'],
            {
                'help': 'Tag value of discovered resource.',
                'default': ''
            }),
            (['--resource_uuid'],
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
        params = {
            'include_tags': 'true', 
            'tag_name': self.app.pargs.tag_name,
            'tag_value': self.app.pargs.tag_value
        }
        d_resources: List[DiscoveredResourceInfo] = self._client.discovered_resources.list(params=params)
        d_resource: DiscoveredResourceInfo = None
        if len(d_resources):
            d_resource = d_resources[0]
            print('\n--> Discovered resource to publish:')
            print(d_resource)
        else:
            raise RuntimeError('No discovered_resource found')

        svc_web = SimpleWebService(self.app.pargs.service_type,
                                  'WEB_USER',
                                  self.app.pargs.service_name,
                                  'pybanyan publish flow',
                                  self.app.pargs.service_domain,
                                  443,
                                  d_resource.private_ip,
                                  80,
                                  self.app.pargs.backend_tls
        )
        print('\n--> Service to create:')
        print(svc_web)

        print('\n--> Creating service:')
        service_info = self._client.services.create_simple_web(svc_web)
        self.app.render(ServiceInfo.Schema().dump(service_info), handler='json', indent=2, sort_keys=True)

        pol_web = SimpleWebPolicy('USER',
                                  'policy-%s' % self.app.pargs.service_name,
                                  'pybanyan publish flow'
        )
        print('\n--> Service to create:')
        print(pol_web)

        print('\n--> Creating policy')
        policy_info = self._client.policies.create_simple_web(pol_web)
        self.app.render(PolicyInfo.Schema().dump(policy_info), handler='json', indent=2, sort_keys=True)

        print('\n--> Getting all policies and services for cache.')
        self._client.services.list()
        self._client.policies.list()

        print('\n--> Attaching policy to service:')
        result = self._client.policies.attach(policy_info, service_info, True)
        mode = 'ENFORCING' if result.enabled else 'PERMISSIVE'
        self.app.print(f'Policy {result.policy_id} attached to service {result.service_id} in {mode} mode.')

        print('\n--> Publish flow successful.')


    @ex(help='add a discovered_resource to an existing service',
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