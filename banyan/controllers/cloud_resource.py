import logging
from typing import List
from uuid import UUID

import copy
from time import sleep

from cement import Controller, ex

from banyan.controllers.base import Base

from banyan.api import BanyanApiClient
from banyan.model.cloud_resource import CloudResource, CloudResourceInfo
from banyan.ext.iaas.base import IaasResource


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
                       len(res.tags or []), res.status]
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


    @ex(help='test AWS configuration by getting EC2 resources',
        arguments=[
            (['region_name'],
            {
                'help': 'Region where AWS EC2 resources exist - us-east-1, us-west-2, etc.'
            })    
        ])
    def test_aws(self):
        try:
            from banyan.ext.iaas.aws import AwsController
        except Exception as ex:
            raise NotImplementedError("AWS SDK not configured correctly > %s" % ex.args[0])

        aws = AwsController(self.app.pargs.region_name)
        instances: List[IaasResource] = aws.list_ec2()
        if len(instances):
            print('--> AWS configuration test passed. Found %d resources.' % len(instances))
        else:
            print('--> AWS configuration test failed. Check your AWS credentials and SDK configuration.')


    @ex(help='sync cloud_resources with AWS IaaS',
        arguments=[
            (['resource_type'],
            {
                'help': 'Type of AWS resource - ec2 | rds | elb. You can say "all" but be careful!'
            }),
            (['region_name'],
            {
                'help': 'Region where AWS resources run - us-east-1, us-west-2, etc. You can say "all" but be careful!'
            }),            
            (['--tag_name'],
            {
                'help': 'Only sync resources with specific tag name. If not specified, sync all resources.'
            })
        ])
    def sync_aws(self):
        try:
            from banyan.ext.iaas.aws import AwsController
        except Exception as ex:
            raise NotImplementedError("AWS SDK not configured correctly > %s" % ex.args[0])

        instances: List[IaasResource] = list()
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

        results = Base.tabulate_iaas_resources(instances)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        if len(results) == 0:
            print('--> No AWS resources to sync')
            return

        Base.wait_for_input('Filtering for new AWS Resources')
        #TODO: List only AWS resources in specified Region (need API update)
        d_resources: List[CloudResourceInfo] = self._client.cloud_resources.list()
        added_instances = Base.added_iaas_resources(instances, d_resources)

        new_results = Base.tabulate_iaas_resources(added_instances)
        self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')

        if len(new_results) == 0:
            print('--> No new AWS resources to sync')
            return

        Base.wait_for_input('Syncing into Discovered Resource')
        for instance in added_instances:
            res = Base.convert_iaas_resource(instance)
            self.app.render(CloudResource.Schema().dump(res), handler='json')
            info = self._client.cloud_resources.create(res)
            print('\n-->', info)
            sleep(0.05)

        print('\n--> Sync with AWS successful.')


    @ex(help='test Azure configuration',
        arguments=[
            (['resource_group'],
            {
                'help': 'Azure Resource Group where some VMs run. You can say "all" but be careful!'
            })
        ])    
    def test_azure(self):
        try:
            from banyan.ext.iaas.azure_cloud import AzureController
        except Exception as ex:
            raise NotImplementedError("Azure SDK not configured correctly > %s" % ex.args[0])

        azr = AzureController(self.app.pargs.resource_group)
        instances: List[IaasResource] = azr.list_vm()
        if len(instances):
            print('--> Azure configuration test passed. Found %d resources.' % len(instances))
        else:
            print('--> Azure configuration test failed. Check your Azure credentials and SDK configuration.')


    @ex(help='sync cloud_resources with Azure IaaS',
        arguments=[
            (['resource_type'],
            {
                'help': 'Type of Azure Resource - vm | lbl. You can say "all" but be careful!'
            }),
            (['resource_group'],
            {
                'help': 'Azure Resource Group where resources run. You can say "all" but be careful!'
            }),            
            (['--location'],
            {
                'help': 'Location where Azure resources run - centralus, eastus, etc. If not specified, all locations are used.'
            }),            
            (['--tag_name'],
            {
                'help': 'Only sync resources with specific tag name. If not specified, sync all resources.'
            })
        ])
    def sync_azure(self):
        try:
            from banyan.ext.iaas.azure_cloud import AzureController
        except Exception as ex:
            raise NotImplementedError("Azure SDK not configured correctly > %s" % ex.args[0])

        instances: List[IaasResource] = list()
        rt = self.app.pargs.resource_type.lower()
        azr = AzureController(self.app.pargs.resource_group, self.app.pargs.location, self.app.pargs.tag_name)
        if rt == 'vm' or rt == 'all':
            Base.wait_for_input('Getting list of Azure VM Resources')
            instances += azr.list_vm()
        if rt == 'lb' or rt == 'all':
            Base.wait_for_input('Getting list of Azure LB Resources')
            instances += azr.list_lb()

        results = Base.tabulate_iaas_resources(instances, ['id'])
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        Base.wait_for_input('Filtering for new Azure Resources')
        #TODO: List only Azure resources in specified Resource Group (need API update)
        d_resources: List[CloudResourceInfo] = self._client.cloud_resources.list()
        added_instances = Base.added_iaas_resources(instances, d_resources)

        new_results = Base.tabulate_iaas_resources(added_instances, ['id'])
        self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')

        if len(new_results) == 0:
            print('--> No new Azure resources to sync')
            return

        Base.wait_for_input('Syncing into Discovered Resource')
        for instance in added_instances:
            res = Base.convert_iaas_resource(instance)
            self.app.render(CloudResource.Schema().dump(res), handler='json')
            info = self._client.cloud_resources.create(res)
            print('\n-->', info)
            sleep(0.05)

        print('\n--> Sync with Azure successful.')


    @ex(help='test Google Cloud configuration',
        arguments=[
            (['project'],
            {
                'help': 'Project ID where GCP resources run. You can say "all" but be careful!'
            })
        ])    
    def test_gcp(self):
        try:
            from banyan.ext.iaas.gcp import GcpController
        except Exception as ex:
            raise NotImplementedError("GCP Client Libraries for Python not configured correctly > %s" % ex.args[0])

        gcp = GcpController(self.app.pargs.project)
        instances: List[IaasResource] = gcp.list_vm()
        if len(instances):
            print('--> Google Cloud configuration test passed. Found %d resources.' % len(instances))
        else:
            print('--> Google Cloud configuration test failed. Check your Google Cloud credentials and Client Libraries for Python configuration.')


    @ex(help='sync cloud_resources with Google Cloud',
        arguments=[
            (['resource_type'],
            {
                'help': 'Type of VMWare Resource - vm | all.'
            }),
            (['project'],
            {
                'help': 'Project ID where GCP resources run. You can say "all" but be careful!'
            }),              
            (['--tag_name'],
            {
                'help': 'Only sync resources with specific category:tag'
            })
        ])
    def sync_gcp(self):
        try:
            from banyan.ext.iaas.gcp import GcpController
        except Exception as ex:
            raise NotImplementedError("GCP Client Libraries for Python not configured correctly > %s" % ex.args[0])

        Base.wait_for_input('Getting list of GCP Resources')
        gcp = GcpController(self.app.pargs.project)
        instances: List[IaasResource] = gcp.list_vm()

        results = Base.tabulate_iaas_resources(instances)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        Base.wait_for_input('Filtering for new GCP Resources')
        #TODO: List only GCP resources in specified Project (need API update)
        d_resources: List[CloudResourceInfo] = self._client.cloud_resources.list()
        added_instances = Base.added_iaas_resources(instances, d_resources)

        new_results = Base.tabulate_iaas_resources(added_instances)
        self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')

        if len(new_results) == 0:
            print('--> No new GCP resources to sync')
            return

        Base.wait_for_input('Syncing into Discovered Resource')
        for instance in added_instances:
            res = Base.convert_iaas_resource(instance)
            self.app.render(CloudResource.Schema().dump(res), handler='json')
            info = self._client.cloud_resources.create(res)
            print('\n-->', info)
            sleep(0.05)

        print('\n--> Sync with Google Cloud successful.')


    @ex(help='test Oracle Cloud configuration',
        arguments=[
            (['compartment'],
            {
                'help': 'Compartment NAME where OCI resources run. You can say "all" but be careful!'
            })
        ])    
    def test_oci(self):
        try:
            from banyan.ext.iaas.oracle_cloud import OciController
        except Exception as ex:
            raise NotImplementedError("OCI Python SDK not configured correctly > %s" % ex.args[0])

        vmw = OciController(self.app.pargs.compartment)
        instances: List[IaasResource] = vmw.list_vm()
        if len(instances):
            print('--> Oracle Cloud configuration test passed. Found %d resources.' % len(instances))
        else:
            print('--> Oracle Cloud configuration test failed. Check your OCI credentials and SDK configuration.')


    @ex(help='sync cloud_resources with Oracle Cloud',
        arguments=[
            (['resource_type'],
            {
                'help': 'Type of VMWare Resource - vm | all.'
            }),
            (['compartment'],
            {
                'help': 'Compartment NAME where OCI resources run. You can say "all" but be careful!'
            }),              
            (['--tag_name'],
            {
                'help': 'Only sync resources with specific category:tag'
            })
        ])
    def sync_oci(self):
        try:
            from banyan.ext.iaas.oracle_cloud import OciController
        except Exception as ex:
            raise NotImplementedError("OCI Python SDK not configured correctly > %s" % ex.args[0])

        Base.wait_for_input('Getting list of OCI Resources')
        orl = OciController(self.app.pargs.compartment)
        instances: List[IaasResource] = orl.list_vm()

        results = Base.tabulate_iaas_resources(instances, ['id', 'account'])
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')

        Base.wait_for_input('Filtering for new OCI Resources')
        #TODO: List only OCI resources in specified Compartment (need API update)
        d_resources: List[CloudResourceInfo] = self._client.cloud_resources.list()
        added_instances = Base.added_iaas_resources(instances, d_resources)

        new_results = Base.tabulate_iaas_resources(added_instances, ['id', 'account'])
        self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')

        if len(new_results) == 0:
            print('--> No new VMware resources to sync')
            return

        Base.wait_for_input('Syncing into Discovered Resource')
        for instance in added_instances:
            res = Base.convert_iaas_resource(instance)
            self.app.render(CloudResource.Schema().dump(res), handler='json')
            info = self._client.cloud_resources.create(res)
            print('\n-->', info)
            sleep(0.05)

        print('\n--> Sync with Oracle Cloud successful.')

