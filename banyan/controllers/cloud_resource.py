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
        value = str(value)
        if len(value) < num_chars + 3:
            return value
        else:
            return '...' + value[-num_chars:]

    @ex(help='list cloud_resources',
        arguments=[
            (['--cloud'], 
            {
                'help': 'filter by provider - AWS | AZURE | GCP | OCI | ...'
            }),
            (['--account'], 
            {
                'help': 'filter by account'
            }),
            (['--region'], 
            {
                'help': 'filter by region/location/zone'
            }),
            (['--resource_type'], 
            {
                'help': 'filter by type - ec2 | vm | rds | ...'
            })
        ])
    def list(self):
        params={'cloud_provider': self.app.pargs.cloud, 'account': self.app.pargs.account, 'region': self.app.pargs.region, 'resource_type': self.app.pargs.resource_type}
        synced_resources: List[CloudResourceInfo] = self._client.cloud_resources.list(params=params)
        results = list()
        headers = ['Name', 'ID', 'Cloud', 'Account', 'Region', 'Type', 'Private Address', 'Public Address', '# Tags', 'Status']
        for res in synced_resources:
            new_res = [res.name[:20], res.resource_udid, res.cloud_provider, self.trunc(res.account,6), 
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
                'help': 'get discovered resource by Banyan UUID.'
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


    @ex(hide=True, help='delete all cloud_resource records')
    def delete_all(self):
        synced_resources: List[CloudResourceInfo] = self._client.cloud_resources.list()
        for d_resource in synced_resources:
            info = self._client.cloud_resources.delete(d_resource.id)
            self.app.render(info, handler='json')
            sleep(0.05)

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
            (['region'],
            {
                'help': 'region where AWS EC2 resources exist - us-east-1, us-west-2, etc.'
            })    
        ])
    def test_aws(self):
        try:
            from banyan.ext.iaas.aws import AwsController
        except Exception as ex:
            raise NotImplementedError("AWS SDK not configured correctly > %s" % ex.args[0])

        aws = AwsController(self.app.pargs.region)
        instances: List[IaasResource] = aws.list_ec2()
        if len(instances):
            print('--> AWS configuration test passed. Found %d resources.' % len(instances))
        else:
            print('--> AWS configuration test failed. Check your AWS credentials and SDK configuration.')


    @ex(help='sync cloud_resources with AWS IaaS',
        arguments=[
            (['resource_type'],
            {
                'help': 'type of AWS resource - ec2 | rds | elb. You can say "all" but be careful!'
            }),
            (['region'],
            {
                'help': 'region where AWS resources run - us-east-1, us-west-2, etc. You can say "all" but be careful!'
            }),            
            (['--tag_name'],
            {
                'help': 'only sync resources with specific tag name. If not specified, sync all resources.'
            }),
            (['--wait_for_input', '-w'],
            {
                'action': 'store_true',
                'help': 'wait for user input before proceeding to next step'
            })
        ])
    def sync_aws(self):
        try:
            from banyan.ext.iaas.aws import AwsController
        except Exception as ex:
            raise NotImplementedError("AWS SDK not configured correctly > %s" % ex.args[0])

        rt = self.app.pargs.resource_type.lower()
        wait = self.app.pargs.wait_for_input

        instances: List[IaasResource] = list()
        aws = AwsController(self.app.pargs.region, self.app.pargs.tag_name)
        if rt == 'ec2' or rt == 'all':
            Base.wait_for_input(wait, 'Getting list of AWS EC2 resources')
            instances += aws.list_ec2()
        if rt == 'rds' or rt == 'all':
            Base.wait_for_input(wait, 'Getting list of AWS RDS resources')
            instances += aws.list_rds()
        if rt == 'elb' or rt == 'all':
            Base.wait_for_input(wait, 'Getting list of AWS ELB resources')
            instances += aws.list_elb() 

        results = Base.tabulate_iaas_resources(instances)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')
        if len(results) == 0:
            print('--> No AWS resources to sync')
            return

        Base.wait_for_input(wait, 'Filtering for new AWS resources')
        params={'cloud_provider': aws.provider, 'resource_type': rt, 'region': self.app.pargs.region}
        synced_resources: List[CloudResourceInfo] = self._client.cloud_resources.list(params=Base.sanitize_alls(params))
        added_instances = Base.added_iaas_resources(instances, synced_resources)

        new_results = Base.tabulate_iaas_resources(added_instances)
        self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')
        if len(new_results) == 0:
            print('--> No new AWS resources to sync')
            return

        Base.wait_for_input(wait, 'Syncing into Banyan Cloud Resource inventory')
        for instance in added_instances:
            res = Base.convert_iaas_resource(instance)
            self._client.cloud_resources.create(res)
            print('\n--> Added AWS resource id(name): %s(%s)' % (res.resource_id, res.resource_name))
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
                'help': 'type of Azure resource - vm | lbl. You can say "all" but be careful!'
            }),
            (['resource_group'],
            {
                'help': 'Azure Resource Group where resources run. You can say "all" but be careful!'
            }),            
            (['--location'],
            {
                'help': 'location where Azure resources run - centralus, eastus, etc. If not specified, all locations are used.'
            }),            
            (['--tag_name'],
            {
                'help': 'only sync resources with specific tag name. If not specified, sync all resources.'
            }),
            (['--wait_for_input', '-w'],
            {
                'action': 'store_true',
                'help': 'wait for user input before proceeding to next step'
            })
        ])
    def sync_azure(self):
        try:
            from banyan.ext.iaas.azure_cloud import AzureController
        except Exception as ex:
            raise NotImplementedError("Azure SDK not configured correctly > %s" % ex.args[0])

        rt = self.app.pargs.resource_type.lower()     
        wait = self.app.pargs.wait_for_input

        instances: List[IaasResource] = list()
        azr = AzureController(self.app.pargs.resource_group, self.app.pargs.location, self.app.pargs.tag_name)
        if rt == 'vm' or rt == 'all':
            Base.wait_for_input(wait, 'Getting list of Azure VM resources')
            instances += azr.list_vm()
        if rt == 'lb' or rt == 'all':
            Base.wait_for_input(wait, 'Getting list of Azure LB resources')
            instances += azr.list_lb()

        results = Base.tabulate_iaas_resources(instances, ['id'])
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')
        if len(results) == 0:
            print('--> No Azure resources to sync')
            return

        Base.wait_for_input(wait, 'Filtering for new Azure resources')
        params={'cloud_provider': azr.provider, 'resource_type': rt, 'account': self.app.pargs.resource_group, 'region': self.app.pargs.location}
        synced_resources: List[CloudResourceInfo] = self._client.cloud_resources.list(params=Base.sanitize_alls(params))
        added_instances = Base.added_iaas_resources(instances, synced_resources)

        new_results = Base.tabulate_iaas_resources(added_instances, ['id'])
        self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')
        if len(new_results) == 0:
            print('--> No new Azure resources to sync')
            return

        Base.wait_for_input(wait, 'Syncing into Banyan Cloud Resource inventory')
        for instance in added_instances:
            res = Base.convert_iaas_resource(instance)
            self._client.cloud_resources.create(res)
            print('\n--> Added Azure resource id(name): %s(%s)' % (res.resource_id, res.resource_name))
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
                'help': 'type of GCP resource - vm | all.'
            }),
            (['project'],
            {
                'help': 'Project ID where GCP resources run. You can say "all" but be careful!'
            }),
            (['--zone'],
            {
                'help': 'zone where GCP resources run - us-east4-b, us-west1-a, etc. If not specified, all zones are used.'
            }),                      
            (['--tag_name'],
            {
                'help': 'only sync resources with specific category:tag'
            }),
            (['--wait_for_input', '-w'],
            {
                'action': 'store_true',
                'help': 'wait for user input before proceeding to next step'
            })
        ])
    def sync_gcp(self):
        try:
            from banyan.ext.iaas.gcp import GcpController
        except Exception as ex:
            raise NotImplementedError("GCP Client Libraries for Python not configured correctly > %s" % ex.args[0])

        rt = self.app.pargs.resource_type.lower()
        wait = self.app.pargs.wait_for_input

        instances: List[IaasResource] = list()
        gcp = GcpController(self.app.pargs.project, self.app.pargs.zone, self.app.pargs.tag_name)
        if rt == 'vm' or rt == 'all':
            Base.wait_for_input(wait, 'Getting list of GCP VM resources')
            instances += gcp.list_vm()

        results = Base.tabulate_iaas_resources(instances)
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')
        if len(results) == 0:
            print('--> No GCP resources to sync')
            return

        Base.wait_for_input(wait, 'Filtering for new GCP resources')
        params={'cloud_provider': gcp.provider, 'resource_type': rt, 'account': self.app.pargs.project, 'region': self.app.pargs.zone}
        synced_resources: List[CloudResourceInfo] = self._client.cloud_resources.list(params=Base.sanitize_alls(params))
        added_instances = Base.added_iaas_resources(instances, synced_resources)

        new_results = Base.tabulate_iaas_resources(added_instances)
        self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')
        if len(new_results) == 0:
            print('--> No new GCP resources to sync')
            return

        Base.wait_for_input(wait, 'Syncing into Banyan Cloud Resource inventory')
        for instance in added_instances:
            res = Base.convert_iaas_resource(instance)
            self._client.cloud_resources.create(res)
            print('\n--> Added GCP resource id(name): %s(%s)' % (res.resource_id, res.resource_name))
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
                'help': 'type of OCI resource - vm | all.'
            }),
            (['compartment'],
            {
                'help': 'Compartment NAME where OCI resources run. You can say "all" but be careful!'
            }), 
            (['--region'],
            {
                'help': 'region where OCI resources run - phx, iad, sjc, etc. If not specified, all regions are used.'
            }),                         
            (['--tag_name'],
            {
                'help': 'only sync resources with specific category:tag'
            }),
            (['--wait_for_input', '-w'],
            {
                'action': 'store_true',
                'help': 'wait for user input before proceeding to next step'
            })            
        ])
    def sync_oci(self):
        try:
            from banyan.ext.iaas.oracle_cloud import OciController
        except Exception as ex:
            raise NotImplementedError("OCI Python SDK not configured correctly > %s" % ex.args[0])

        wait = self.app.pargs.wait_for_input
        rt = self.app.pargs.resource_type.lower()

        instances: List[IaasResource] = list()
        orl = OciController(self.app.pargs.compartment)
        if rt == 'vm' or rt == 'all':
            Base.wait_for_input(wait, 'Getting list of OCI VM resources')
            instances += orl.list_vm()

        results = Base.tabulate_iaas_resources(instances, ['id', 'account'])
        self.app.render(results, handler='tabulate', headers='keys', tablefmt='simple')
        if len(results) == 0:
            print('--> No OCI resources to sync')
            return

        Base.wait_for_input(wait, 'Filtering for new OCI resources')
        params={'cloud_provider': orl.provider, 'resource_type': rt, 'account': self.app.pargs.compartment, 'region': self.app.pargs.region}
        synced_resources: List[CloudResourceInfo] = self._client.cloud_resources.list(params=Base.sanitize_alls(params))
        added_instances = Base.added_iaas_resources(instances, synced_resources)

        new_results = Base.tabulate_iaas_resources(added_instances, ['id', 'account'])
        self.app.render(new_results, handler='tabulate', headers='keys', tablefmt='simple')
        if len(new_results) == 0:
            print('--> No new OCI resources to sync')
            return

        Base.wait_for_input(wait, 'Syncing into Banyan Cloud Resource inventory')
        for instance in added_instances:
            res = Base.convert_iaas_resource(instance)
            self._client.cloud_resources.create(res)
            print('\n--> Added Azure resource id(name): %s(%s)' % (res.resource_id, res.resource_name))
            sleep(0.05)

        print('\n--> Sync with Oracle Cloud successful.')

