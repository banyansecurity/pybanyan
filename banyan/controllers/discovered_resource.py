from typing import List
from uuid import UUID

import copy
from time import sleep

from cement import Controller, ex

from banyan.controllers.base import Base

from banyan.api import BanyanApiClient
from banyan.model.discovered_resource import DiscoveredResource, DiscoveredResourceInfo
from banyan.model.service import ServiceInfo, Service, SimpleWebService, AllowPattern
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
        headers = ['Name', 'ID', 'Cloud', 'Region', 'Type', 'Private IP', '# Tags', 'Status']
        for res in d_resources:
            new_res = [res.name, res.resource_udid, res.cloud_provider, res.region,
                    res.resource_type, res.private_ip, len(res.tags), res.status]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')


    @ex(help='show details & tags of a discovered_resource', 
        arguments=[
            (['resource_uuid'],
            {
                'help': 'Get discovered resource by Banyan UUID.'
            }),            
        ])
    def get(self):
        id: UUID = self.app.pargs.resource_uuid
        d_resource: DiscoveredResourceInfo = self._client.discovered_resources.get(id)
        dr_json = DiscoveredResource.Schema().dump(d_resource)
        self.app.render(dr_json, handler='json', indent=2, sort_keys=True)


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
        d_resource: DiscoveredResourceInfo = self._client.discovered_resources.create(d_resource)
        dr_json = DiscoveredResource.Schema().dump(d_resource)
        self.app.render(dr_json, handler='json', indent=2, sort_keys=True)


    @ex(help='update status for a given discovered_resource record', 
        arguments=[
            (['resource_uuid'],
            {
                'help': 'Banyan UUID of discovered resource to update.'
            }),
            (['status'],
            {
                'help': 'Status - Discovered | Ignored | Published'
            }),                       
        ])
    def update(self):
        id: UUID = self.app.pargs.resource_uuid
        status: str = self.app.pargs.status
        d_resource: DiscoveredResourceInfo = self._client.discovered_resources.update_status(id, status)
        dr_json = DiscoveredResource.Schema().dump(d_resource)
        self.app.render(dr_json, handler='json', indent=2, sort_keys=True)


    @ex(help='delete a given discovered_resource record', 
        arguments=[
            (['resource_uuid'],
            {
                'help': 'Banyan UUID of discovered resource to delete.'
            }),            
        ])
    def delete(self):
        id: UUID = self.app.pargs.resource_uuid
        info = self._client.discovered_resources.delete(id)
        self.app.print(info)

    @ex(help='sync discovered_resources with AWS IaaS',
        arguments=[
            (['resource_type'],
            {
                'help': 'Type of AWS Resource - EC2 | RDS | LB | ALL.'
            }),
            (['tag_name'],
            {
                'help': 'Only sync resources with specific tag name'
            }),
            (['--tag_value'],
            {
                'default': "*",
                'help': 'Only sync resources with a specific tag value.'
            })

        ])
    def sync_aws(self):
        try:
            from banyan.ext.aws.ec2 import Ec2Controller, Ec2Model
        except Exception as ex:
            raise NotImplementedError("AWS SDK not configured correctly > %s" % ex.args[0])

        Base.wait_for_input('Getting list of AWS Resources')
        ec2 = Ec2Controller()
        instances = ec2.list(self.app.pargs.tag_name, [self.app.pargs.tag_value])
        results = list()
        for instance in instances:
            allvars = vars(copy.copy(instance))
            allvars['tags'] = len(allvars['tags'])
            results.append(allvars)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        Base.wait_for_input('Syncing into Discovered Resource')
        for instance in instances:
            res_tags = []
            for tag in instance.tags:
                res_tag = {
                    'name': tag['Key'],
                    'value': tag['Value']
                }
                res_tags.append(res_tag)

            res = DiscoveredResource(
                instance.cloud_provider,
                instance.region,
                instance.id,
                instance.name,
                instance.type,
                instance.public_ip,
                instance.private_ip,
                res_tags
            )
            self.app.render(DiscoveredResource.Schema().dump(res), handler='json')
            info = self._client.discovered_resources.create(res)
            print('\n-->', info)
            sleep(0.05)

        print('\n--> Sync with AWS successful.')


    @ex(help='sync discovered_resources with Azure IaaS',
        arguments=[
            (['resource_type'],
            {
                'help': 'Type of Azure Resource - VM | ALL.'
            }),
            (['tag_name'],
            {
                'help': 'Only sync resources with specific tag name'
            })
        ])
    def sync_azure(self):
        try:
            from banyan.ext.azure.vm import VmController, VmModel
        except Exception as ex:
            raise NotImplementedError("Azure SDK not configured correctly > %s" % ex.args[0])

        Base.wait_for_input('Getting list of Azure Resources')
        vm = VmController()
        instances = vm.list(self.app.pargs.tag_name)
        results = list()
        for instance in instances:
            allvars = vars(copy.copy(instance))
            allvars['tags'] = len(allvars['tags'])
            results.append(allvars)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        Base.wait_for_input('Syncing into Discovered Resource')
        for instance in instances:
            res_tags = []
            for key in instance.tags:
                res_tag = {
                    'name': key,
                    'value': instance.tags[key]
                }
                res_tags.append(res_tag)            
            res = DiscoveredResource(
                instance.cloud_provider,
                instance.location,
                instance.id,
                instance.name,
                instance.type,
                instance.public_ip,
                instance.private_ip,
                res_tags
            )
            self.app.render(DiscoveredResource.Schema().dump(res), handler='json')
            info = self._client.discovered_resources.create(res)
            print('\n-->', info)
            sleep(0.05)

        print('\n--> Sync with Azure successful.')


    @ex(help='sync discovered_resources with VMWare vSphere',
        arguments=[
            (['resource_type'],
            {
                'help': 'Type of VMWare Resource - VM | ALL.'
            }),
            (['tag_name'],
            {
                'help': 'Only sync resources with specific category:tag'
            })
        ])
    def sync_vmware(self):
        try:
            from banyan.ext.vmware.vm import VmController, VmModel
        except Exception as ex:
            raise NotImplementedError("VMware SDK not configured correctly > %s" % ex.args[0])

        Base.wait_for_input('Getting list of VMware Resources')
        vm = VmController()
        instances = vm.list()
        results = list()
        for instance in instances:
            allvars = vars(copy.copy(instance))
            allvars['tags'] = len(allvars['tags'])
            results.append(allvars)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        Base.wait_for_input('Syncing into Discovered Resource')
        for instance in instances:
            res_tags = []
            for key in instance.tags:
                res_tag = {
                    'name': key,
                    'value': instance.tags[key]
                }
                res_tags.append(res_tag)            
            res = DiscoveredResource(
                instance.cloud_provider,
                instance.datacenter,
                instance.id,
                instance.name,
                instance.type,
                instance.public_ip,
                instance.private_ip,
                res_tags
            )
            self.app.render(DiscoveredResource.Schema().dump(res), handler='json')
            info = self._client.discovered_resources.create(res)
            print('\n-->', info)
            sleep(0.05)

        print('\n--> Sync with VMware successful.')


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
            (['resource_uuid'],
            {
                'help': 'Banyan UUID of the discovered resource to use.'
            }),                           
            (['--backend_port'],
            {
                'default': 80,
                'help': 'Specify if backend port is non-standard.'
            }),
            (['--backend_tls'],
            {
                'default': False,
                'help': 'Specify if backend requires TLS.'
            })            
        ])
    def publish(self):
        Base.wait_for_input('Getting Discovered Resource')
        id: UUID = self.app.pargs.resource_uuid
        d_resource: DiscoveredResourceInfo = self._client.discovered_resources.get(id)

        if d_resource:
            dr_json = DiscoveredResource.Schema().dump(d_resource)
            self.app.render(dr_json, handler='json', indent=2, sort_keys=True)
        else:
            raise RuntimeError('No discovered_resource found')

        pol_web = SimpleWebPolicy('USER',
                                  'policy-%s' % self.app.pargs.service_name,
                                  'pybanyan publish flow'
        )
        print('\n--> Policy to create:')
        print(pol_web)

        Base.wait_for_input('Creating policy')
        policy_info = self._client.policies.create_simple_web(pol_web)
        self.app.render(PolicyInfo.Schema().dump(policy_info), handler='json', indent=2, sort_keys=True)

        svc_web = SimpleWebService(self.app.pargs.service_type,
                                  'WEB_USER',
                                  self.app.pargs.service_name,
                                  'pybanyan publish flow',
                                  self.app.pargs.service_domain,
                                  443,
                                  d_resource.private_ip,
                                  self.app.pargs.backend_port,
                                  self.app.pargs.backend_tls
        )
        print('\n--> Service to create:')
        print(svc_web)

        Base.wait_for_input('Creating service')
        service_info = self._client.services.create_simple_web(svc_web)
        self.app.render(ServiceInfo.Schema().dump(service_info), handler='json', indent=2, sort_keys=True)

        Base.wait_for_input('Getting services and policies')
        self._client.services.list()
        self._client.policies.list()

        Base.wait_for_input('Attaching policy to service')
        result = self._client.policies.attach(policy_info, service_info, True)
        mode = 'ENFORCING' if result.enabled else 'PERMISSIVE'
        self.app.print(f'Policy {result.policy_id} attached to service {result.service_id} in {mode} mode.')

        print('\n--> Publish flow successful.')


    @ex(help='add discovered_resources by tag to an existing service',
        arguments=[
            (['service_name'],
            {
                'help': 'Name of service whose whitelist should be updated.'
            }),          
            (['tag_name'],
            {
                'help': 'Name of Tag of the discovered resources.'
            }),
            (['--tag_value'],
            {
                'help': 'Value of Tag of the discovered resources.'
            })
        ])
    def whitelist(self):
        Base.wait_for_input('Getting Discovered Resources')
        params = {
            'include_tags': 'true',
            'tag_name': self.app.pargs.tag_name,
            'tag_value': self.app.pargs.tag_value
        }
        d_resources: List[DiscoveredResourceInfo] = self._client.discovered_resources.list(params=params)
        if len(d_resources) == 0:
            raise RuntimeError('No discovered_resource found')        

        print('\n--> Discovered resources to whitelist:')
        results = list()
        headers = ['Name', 'ID', 'Cloud', 'Region', 'Type', 'Private IP', 'Public IP', '# Tags']
        for res in d_resources:
            new_res = [res.name, res.resource_udid, res.cloud_provider, res.region,
                    res.resource_type, res.private_ip, res.public_ip, len(res.tags)]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')

        Base.wait_for_input('Getting services')
        self._client.services.list()
        service_info: ServiceInfo = self._client.services[self.app.pargs.service_name]
        if not service_info.service.spec.backend.http_connect:
            raise RuntimeError('Service does not support whitelist by IP address')

        print('\n--> Service to update whitelist to:')
        svc = service_info.service
        service_json = Service.Schema().dump(svc)
        self.app.render(service_json, handler='json', indent=2, sort_keys=True)

        print('\n--> New whitelist:')
        allow = AllowPattern()
        for d_resource in d_resources:
            allow.cidrs.append('%s/32' % d_resource.private_ip)
        print(allow)
        svc.spec.backend.allow_patterns = [allow]

        Base.wait_for_input('Updating service')
        service_info = self._client.services.update(svc)
        self.app.render(ServiceInfo.Schema().dump(service_info), handler='json', indent=2, sort_keys=True)

        print('\n--> Whitelist flow successful.')
