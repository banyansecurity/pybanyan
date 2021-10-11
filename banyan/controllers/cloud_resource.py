import logging
from typing import List
from uuid import UUID

import copy
from time import sleep

from cement import Controller, ex

from banyan.controllers.base import Base

from banyan.api import BanyanApiClient
from banyan.model.cloud_resource import CloudResource, CloudResourceInfo
from banyan.model.service import ServiceInfo, Service, SimpleWebService, AllowPattern
from banyan.model.policy import PolicyInfo, SimpleWebPolicy


class CloudResourceController(Controller):
    class Meta:
        label = 'cloud_resource'
        stacked_type = 'nested'
        stacked_on = 'base'
        help = 'manage cloud resources discovered from IaaS'

    @property
    def _client(self) -> BanyanApiClient:
        return self.app.client

    def trunc(self, value, num_chars) -> str:
        if not value:
            return ''
        elif len(value) < num_chars+3:
            return value
        else:
            return '...' + str(value)[-num_chars:]

    @ex(help='list cloud_resources',
        arguments=[
            (['--tag_name'], 
            {
                'help': 'Filter discovered resource by Tag Name.'
            }),
        ])
    def list(self):
        params={'include_tags': 'true', 'tag_name': self.app.pargs.tag_name}
        d_resources: List[CloudResourceInfo] = self._client.cloud_resources.list(params=params)
        results = list()
        headers = ['Name', 'ID', 'Cloud', 'Account', 'Region', 'Type', 'Private Address', 'Public Address', '# Tags', 'Status']
        for res in d_resources:
            new_res = [res.name, res.resource_udid, res.cloud_provider, self.trunc(res.account,6), 
                       res.region, res.resource_type, 
                       self.trunc(res.private_ip or res.private_dns_name, 24), 
                       self.trunc(res.public_ip or res.public_dns_name, 24), 
                       len(res.tags), res.status]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')


    @ex(help='show details & tags of a cloud_resource', 
        arguments=[
            (['resource_uuid'],
            {
                'help': 'Get discovered resource by Banyan UUID.'
            }),            
        ])
    def get(self):
        id: UUID = self.app.pargs.resource_uuid
        d_resource: CloudResourceInfo = self._client.cloud_resources.get(id)
        dr_json = CloudResourceInfo.Schema().dump(d_resource)
        self.app.render(dr_json, handler='json', indent=2, sort_keys=True)


    @ex(help='create a new cloud_resource',
        arguments=[
            (['resources_json'], 
            {
                'help': 'JSON blob describing the new discovered resource(s) to be created, or a filename '
                         'containing JSON prefixed by "@" (example: @res.json).'
            }),
        ])
    def create(self):
        d_resource = Base.get_json_input(self.app.pargs.resources_json)
        d_resource: CloudResourceInfo = self._client.cloud_resources.create(d_resource)
        dr_json = CloudResource.Schema().dump(d_resource)
        self.app.render(dr_json, handler='json', indent=2, sort_keys=True)


    @ex(hide=True, help='update status for a given cloud_resource record', 
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
    def update_status(self):
        id: UUID = self.app.pargs.resource_uuid
        status: str = self.app.pargs.status
        d_resource: CloudResourceInfo = self._client.cloud_resources.update_status(id, status)
        dr_json = CloudResource.Schema().dump(d_resource)
        self.app.render(dr_json, handler='json', indent=2, sort_keys=True)


    @ex(help='delete a given cloud_resource record', 
        arguments=[
            (['resource_uuid'],
            {
                'help': 'Banyan UUID of discovered resource to delete.'
            }),            
        ])
    def delete(self):
        id: UUID = self.app.pargs.resource_uuid
        info = self._client.cloud_resources.delete(id)
        self.app.render(info, handler='json')


    @ex(help='show cloud_resources associated with services', 
        arguments=[
            (['--resource_uuid'],
            {
                'help': 'Banyan UUID of discovered resource to list associations for.'
            }),            
        ])
    def list_associations(self):
        assocs = self._client.cloud_resources.associations(self.app.pargs.resource_uuid)
        results = list()
        headers = ['ID', 'Resource ID', 'Resource Name', 'Resource Type', 'Service ID', 'Service Name', 'Resource Status']
        for res in assocs:
            new_res = [res.id, self.trunc(res.resource_udid,9), res.resource_name, res.resource_type, 
                       res.service_id, res.service_name, res.resource_status]
            results.append(new_res)
        self.app.render(results, handler='tabulate', headers=headers, tablefmt='simple')


    @ex(hide=True, help='associate cloud_resource with service', 
        arguments=[
            (['resource_uuid'],
            {
                'help': 'Banyan UUID of discovered resource to associate.'
            }),
            (['service_name'],
             {
                 'metavar': 'service_name_or_id',
                 'help': 'Name or ID of the service to associate a discovered resource with.',
             }),                   
        ])
    def associate_with_service(self):
        info = self._client.cloud_resources.associate(self.app.pargs.resource_uuid, self.app.pargs.service_name)
        self.app.render(info, handler='json')


    @ex(hide=True, help='dissociate cloud_resource from service', 
        arguments=[
            (['association_uuid'],
            {
                'help': 'Association UUID of discovered resource and service.'
            }),            
        ])
    def dissociate_from_service(self):
        info = self._client.cloud_resources.dissociate(self.app.pargs.association_uuid)
        self.app.render(info, handler='json')


    @ex(help='test AWS configuration')
    def test_aws(self):
        try:
            from banyan.ext.aws.main import AwsResourceModel, AwsController
        except Exception as ex:
            raise NotImplementedError("AWS SDK not configured correctly > %s" % ex.args[0])

        aws = AwsController()
        instances: List[AwsResourceModel] = aws.list_ec2()
        if len(instances):
            print('--> AWS configuration test passed. Found %d resources.' % len(instances))
        else:
            print('--> AWS configuration test failed. Check your AWS credentials and SDK configuration.')


    @ex(help='sync cloud_resources with AWS IaaS',
        arguments=[
            (['resource_type'],
            {
                'help': 'Type of AWS resource - ec2 | rds | elb | all'
            }),
            (['--region_name'],
            {
                'help': 'Region where AWS resources run - us-east-1, us-west-2, etc. If not specified, use default region.'
            }),            
            (['--tag_name'],
            {
                'help': 'Only sync resources with specific tag name. If not specified, sync all resources.'
            })
        ])
    def sync_aws(self):
        try:
            from banyan.ext.aws.main import AwsResourceModel, AwsController
        except Exception as ex:
            raise NotImplementedError("AWS SDK not configured correctly > %s" % ex.args[0])

        instances: List[AwsResourceModel] = list()
        rt = self.app.pargs.resource_type.lower()
        aws = AwsController(self.app.pargs.region_name, self.app.pargs.tag_name)
        if rt == 'ec2' or rt == 'all':
            Base.wait_for_input('Getting list of AWS EC2 Resources')
            instances += aws.list_ec2()
        if rt == 'rds' or rt == 'all':
            Base.wait_for_input('Getting list of AWS RDS Resources')
            instances += aws.list_rds()
        if rt == 'elb' or rt == 'all':
            Base.wait_for_input('Getting list of AWS ELB Resources')
            instances += aws.list_elb() 

        results = list()
        for instance in instances:
            allvars = vars(copy.copy(instance))
            allvars['tags'] = len(allvars['tags'])
            results.append(allvars)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        Base.wait_for_input('Filtering for new AWS Resources')
        #TODO: List only AWS resources in specified Region (need API update)
        d_resources: List[CloudResourceInfo] = self._client.cloud_resources.list()
        added_instances = Base.rows_added(instances, 'id', d_resources, 'resource_id')

        new_results = list()
        for instance in added_instances:
            allvars = vars(copy.copy(instance))
            allvars['tags'] = len(allvars['tags'])
            new_results.append(allvars)
        self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')

        if len(new_results) == 0:
            print('--> No new AWS resources to sync')
            return

        Base.wait_for_input('Syncing into Discovered Resource')
        for instance in added_instances:
            res_tags = []
            for tag in instance.tags:
                res_tag = {
                    'name': tag['Key'],
                    'value': tag['Value']
                }
                res_tags.append(res_tag)

            res = CloudResource(
                cloud_provider = AwsResourceModel.PROVIDER,
                account = instance.account,
                region = instance.region,
                resource_id = instance.id,
                resource_name = instance.name,
                resource_type = instance.type,
                public_dns_name = instance.public_dns_name,
                public_ip = instance.public_ip,
                private_dns_name = instance.private_dns_name,
                private_ip = instance.private_ip,
                ports = instance.ports,
                status = 'discovered',
                tags = res_tags
            )
            self.app.render(CloudResource.Schema().dump(res), handler='json')
            info = self._client.cloud_resources.create(res)
            print('\n-->', info)
            sleep(0.05)

        print('\n--> Sync with AWS successful.')


    @ex(help='test Azure configuration')
    def test_azure(self):
        try:
            from banyan.ext.azure.main import AzureController, AzureResourceModel
        except Exception as ex:
            raise NotImplementedError("Azure SDK not configured correctly > %s" % ex.args[0])

        azr = AzureController()
        instances: List[AzureResourceModel] = azr.list_vm()
        if len(instances):
            print('--> Azure configuration test passed. Found %d resources.' % len(instances))
        else:
            print('--> Azure configuration test failed. Check your Azure credentials and SDK configuration.')


    @ex(help='sync cloud_resources with Azure IaaS',
        arguments=[
            (['resource_type'],
            {
                'help': 'Type of Azure Resource - vm | lb | all.'
            }),
            (['--resource_group'],
            {
                'help': 'Azure Resource Group where resources run. If not specified, use all  resource groups.'
            }),            
            (['--location'],
            {
                'help': 'Location where Azure resources run - centralus, eastus, etc. If not specified, use all locations.'
            }),            
            (['--tag_name'],
            {
                'help': 'Only sync resources with specific tag name. If not specified, sync all resources.'
            })
        ])
    def sync_azure(self):
        try:
            from banyan.ext.azure.main import AzureController, AzureResourceModel
        except Exception as ex:
            raise NotImplementedError("Azure SDK not configured correctly > %s" % ex.args[0])

        instances: List[AzureResourceModel] = list()
        rt = self.app.pargs.resource_type.lower()
        azr = AzureController(self.app.pargs.resource_group, self.app.pargs.location, self.app.pargs.tag_name)
        if rt == 'vm' or rt == 'all':
            Base.wait_for_input('Getting list of Azure VM Resources')
            instances += azr.list_vm()
        if rt == 'lb' or rt == 'all':
            Base.wait_for_input('Getting list of Azure LB Resources')
            instances += azr.list_lb()

        results = list()
        for instance in instances:
            allvars = vars(copy.copy(instance))
            allvars.pop('id')    # too long to display
            allvars['tags'] = len(allvars['tags'])
            results.append(allvars)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        Base.wait_for_input('Filtering for new Azure Resources')
        #TODO: List only Azure resources in specified Location (need API update)
        d_resources: List[CloudResourceInfo] = self._client.cloud_resources.list()
        added_instances = Base.rows_added(instances, 'id', d_resources, 'resource_id')

        new_results = list()
        for instance in added_instances:
            allvars = vars(copy.copy(instance))
            allvars.pop('id')    # too long to display
            allvars['tags'] = len(allvars['tags'])
            new_results.append(allvars)
        self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')

        if len(new_results) == 0:
            print('--> No new Azure resources to sync')
            return

        Base.wait_for_input('Syncing into Discovered Resource')
        for instance in instances:
            res_tags = []
            for key in instance.tags:
                res_tag = {
                    'name': key,
                    'value': instance.tags[key]
                }
                res_tags.append(res_tag)            
            
            res = CloudResource(
                cloud_provider = AzureResourceModel.PROVIDER,
                account = f'{instance.resource_group}-{instance.subscription}',
                region = instance.location,
                resource_id = instance.id,
                resource_name = instance.name,
                resource_type = instance.type,
                public_dns_name = instance.public_dns_name,
                public_ip = instance.public_ip,
                private_dns_name = instance.private_dns_name,
                private_ip = instance.private_ip,
                ports = instance.ports,
                status = 'discovered',
                tags = res_tags
            )
            self.app.render(CloudResource.Schema().dump(res), handler='json')
            info = self._client.cloud_resources.create(res)
            print('\n-->', info)
            sleep(0.05)

        print('\n--> Sync with Azure successful.')


    @ex(help='test VMware vSphere configuration')
    def test_vmware(self):
        try:
            from banyan.ext.vmware.main import VmwareController, VmwareResourceModel
        except Exception as ex:
            raise NotImplementedError("VMware SDK not configured correctly > %s" % ex.args[0])

        vmw = VmwareController()
        instances: List[VmwareResourceModel] = vmw.list_vm()
        if len(instances):
            print('--> VMWare vSphere configuration test passed. Found %d resources.' % len(instances))
        else:
            print('--> VMWare vSphere configuration test failed. Check your VMWare vSphere credentials and SDK configuration.')


    @ex(help='sync cloud_resources with VMWare vSphere',
        arguments=[
            (['resource_type'],
            {
                'help': 'Type of VMWare Resource - vm | all.'
            }),
            (['--datacenter'],
            {
                'help': 'Datacenter where vSphere resources run. If not specified, use all datacenters.'
            }),              
            (['--tag_name'],
            {
                'help': 'Only sync resources with specific category:tag'
            })
        ])
    def sync_vmware(self):
        try:
            from banyan.ext.vmware.main import VmwareController, VmwareResourceModel
        except Exception as ex:
            raise NotImplementedError("VMware SDK not configured correctly > %s" % ex.args[0])

        Base.wait_for_input('Getting list of VMware Resources')
        vmw = VmwareController(self.app.pargs.datacenter)
        instances: List[VmwareResourceModel] = vmw.list_vm()
        results = list()
        for instance in instances:
            allvars = vars(copy.copy(instance))
            allvars['tags'] = len(allvars['tags'])
            results.append(allvars)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        Base.wait_for_input('Filtering for new VMware Resources')
        #TODO: List only VMware resources in specified Datacenter (need API update)
        d_resources: List[CloudResourceInfo] = self._client.cloud_resources.list()
        added_instances = Base.rows_added(instances, 'id', d_resources, 'resource_id')

        new_results = list()
        for instance in added_instances:
            allvars = vars(copy.copy(instance))
            allvars['tags'] = len(allvars['tags'])
            new_results.append(allvars)
        self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')

        Base.wait_for_input('Syncing into Discovered Resource')
        for instance in instances:
            res_tags = []
            for key in instance.tags:
                res_tag = {
                    'name': key,
                    'value': instance.tags[key]
                }
                res_tags.append(res_tag)            
            res = CloudResource(
                cloud_provider = VmwareResourceModel.PROVIDER,
                account = VmwareResourceModel.ACCOUNT,
                region = instance.datacenter,
                resource_name = instance.id,
                resource_type = instance.type,
                resource_id = instance.id,
                resource_name = instance.name,
                resource_type = instance.type,
                public_dns_name = instance.public_dns_name,
                public_ip = instance.public_ip,
                private_dns_name = instance.private_dns_name,
                private_ip = instance.private_ip,
                ports = instance.ports,
                status = 'discovered',
                tags = res_tags
            )
            self.app.render(CloudResource.Schema().dump(res), handler='json')
            info = self._client.cloud_resources.create(res)
            print('\n-->', info)
            sleep(0.05)

        print('\n--> Sync with VMware successful.')


    @ex(help='use cloud_resource to create a new service',
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
        d_resource: CloudResourceInfo = self._client.cloud_resources.get(id)

        if d_resource:
            dr_json = CloudResource.Schema().dump(d_resource)
            self.app.render(dr_json, handler='json', indent=2, sort_keys=True)
        else:
            raise RuntimeError('No cloud_resource found')

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


    @ex(help='add cloud_resources by tag to an existing service',
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
        d_resources: List[CloudResourceInfo] = self._client.cloud_resources.list(params=params)
        if len(d_resources) == 0:
            raise RuntimeError('No cloud_resource found')        

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
