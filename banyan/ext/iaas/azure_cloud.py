from typing import List
import os, json

from banyan.ext.iaas.base import IaasAccount, IaasResource, IaasInstance, IaasRegion, IaasConf, IaasController
 
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient


class AzureController(IaasController):
    def __init__(self, filter_by_resource_group: str, filter_by_location: str = None, filter_by_tag_name: str = None):
        self._provider = 'azure'
        _azure_subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
        _azure_tenant_id = os.getenv('AZURE_TENANT_ID')
        _azure_client_id = os.getenv('AZURE_CLIENT_ID')
        _azure_client_secret = os.getenv('AZURE_CLIENT_SECRET')
        if not _azure_subscription_id:
            _creds = IaasConf.get_creds(self._provider)
            _azure_subscription_id = _creds['azure_subscription_id']
            _azure_tenant_id = _creds['azure_tenant_id']
            _azure_client_id = _creds['azure_client_id']
            _azure_client_secret = _creds['azure_client_secret']

        try:
            os.environ['AZURE_SUBSCRIPTION_ID'] = _azure_subscription_id
            os.environ['AZURE_TENANT_ID'] = _azure_tenant_id
            os.environ['AZURE_CLIENT_ID'] = _azure_client_id
            os.environ['AZURE_CLIENT_SECRET'] = _azure_client_secret            
            self._credential = DefaultAzureCredential()     # needs env vars
            self._subscription_id = _azure_subscription_id  # for clients
            resource_client = ResourceManagementClient(self._credential, self._subscription_id)
        except Exception as ex:
            print('AzureSDKError > %s' % ex.args[0])
            raise
        self._filter_by_resource_group = filter_by_resource_group
        self._filter_by_location = filter_by_location
        self._filter_by_tag_name = filter_by_tag_name

        try:
            self._resource_group_list = resource_client.resource_groups.list()
        except Exception as ex:
            print('AzureControllerError > %s' % ex.args[0])
            raise


    def list_vm(self):
        res_type = 'vm'
        compute_client =  ComputeManagementClient(self._credential, self._subscription_id)
        network_client = NetworkManagementClient(self._credential, self._subscription_id)

        # VMs in all resource groups
        vm_list = compute_client.virtual_machines.list_all()

        instances: List[IaasResource] = list()
        for vm in list(vm_list):
            #print(json.dumps(vm.as_dict(), indent=4))
            vm_loc = vm.location
            vm_tags = vm.tags or dict()
            vm_reference = vm.id.split('/')
            vm_rg = vm_reference[4]
            ni_reference = vm.network_profile.network_interfaces[0].id.split('/')
            ni_name = ni_reference[8]

            # implement filtering
            if self._filter_by_resource_group != 'all' and self._filter_by_resource_group != vm_rg:
                continue
            if self._filter_by_location and self._filter_by_location != vm_loc:
                continue
            if self._filter_by_tag_name and not vm_tags.get(self._filter_by_tag_name):
                continue

            # check network interface for address
            net_interface = network_client.network_interfaces.get(vm_rg, ni_name)
            #print(json.dumps(net_interface.as_dict(), indent=4))
            # assume only 1 NIC
            ip_config = net_interface.ip_configurations[0]
            private_ip = ip_config.private_ip_address or ''
            public_ip = ''
            if ip_config.public_ip_address:
                pub_ip_reference = ip_config.public_ip_address.id.split('/')
                pub_ip_group = pub_ip_reference[4]
                pub_ip_name = pub_ip_reference[8]
                pub_ip = network_client.public_ip_addresses.get(pub_ip_group, pub_ip_name)
                #print(json.dumps(pub_ip.as_dict(), indent=4))
                public_ip = pub_ip.ip_address

            res_inst = IaasInstance(
                type = res_type,
                id = vm.id,
                name = vm.name,
                private_ip = private_ip,
                public_ip = public_ip
            )

            res_acct = IaasAccount('resource_group', vm_rg)
            res_regn = IaasRegion('location', vm_loc)

            res = IaasResource(
                provider = self._provider,
                account = res_acct,
                region = res_regn,
                instance = res_inst,
                tags = vm_tags
            )
            instances.append(res)

        return instances


    def list_lb(self):
        res_type = 'lb'
        network_client = NetworkManagementClient(self._credential, self._subscription_id)

        lb_list = network_client.load_balancers.list_all()

        instances: List[IaasResource] = list()
        for lb in list(lb_list):
            #print(json.dumps(lb.as_dict(), indent=4))
            lb_loc = lb.location
            lb_tags = lb.tags or dict()
            lb_reference = lb.id.split('/')
            lb_rg = lb_reference[4]

            # implement filtering
            if self._filter_by_resource_group != 'all' and self._filter_by_resource_group != lb_rg:
                continue            
            if self._filter_by_location and self._filter_by_location != lb_loc:
                continue
            if self._filter_by_tag_name and not lb_tags.get(self._filter_by_tag_name):
                continue

            ip_config = lb.frontend_ip_configurations[0]
            private_ip = ip_config.private_ip_address or ''
            public_ip = ''
            if ip_config.public_ip_address:
                pub_ip_reference = ip_config.public_ip_address.id.split('/')
                pub_ip_group = pub_ip_reference[4]
                pub_ip_name = pub_ip_reference[8]
                pub_ip = network_client.public_ip_addresses.get(pub_ip_group, pub_ip_name)
                #print(json.dumps(pub_ip.as_dict(), indent=4))
                public_ip = pub_ip.ip_address

            res_ports = list()
            for lb_rule in list(lb.load_balancing_rules):
                res_ports.append(f'{lb_rule.frontend_port}/{lb_rule.protocol}')

            res_inst = IaasInstance(
                type = res_type,
                id = lb.id,
                name = lb.name,
                public_ip = public_ip,
                private_ip = private_ip,
                ports = res_ports
            )

            res_acct = IaasAccount('resource_group', lb_rg)
            res_regn = IaasRegion('location', lb_loc)

            res = IaasResource(
                provider = self._provider,
                account = res_acct,
                region = res_regn,
                instance = res_inst,
                tags = lb_tags
            )
            instances.append(res)

        return instances


if __name__ == '__main__':
    azr = AzureController('all', None, 'banyan:discovery')
    my_vms = azr.list_vm()
    print(my_vms)
    my_lbs = azr.list_lb()
    print(my_lbs)

