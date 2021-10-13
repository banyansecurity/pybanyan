from typing import List, Dict, ClassVar, Type, Optional, Union
from dataclasses import dataclass, field
import os, json

try: 
    from azure.identity import DefaultAzureCredential
    from azure.mgmt.resource import ResourceManagementClient
    from azure.mgmt.compute import ComputeManagementClient
    from azure.mgmt.network import NetworkManagementClient
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise

try:
    from ..model import *
except:
    # trying to run "python main.py"
    import sys
    sys.path.append('..')
    from model import *

class AzureController:
    def __init__(self, filter_by_resource_group: str = None, filter_by_location: str = None, filter_by_tag_name: str = None):
        try:
            self._credential = DefaultAzureCredential()
            self._subscription = os.environ["AZURE_SUBSCRIPTION_ID"]
            resource_client = ResourceManagementClient(self._credential, self._subscription)
        except Exception as ex:
            print('AzureSDKError > %s' % ex.args[0])
            raise
        self._filter_by_resource_group = filter_by_resource_group
        self._filter_by_location = filter_by_location
        self._filter_by_tag_name = filter_by_tag_name

        self._provider = 'AZURE'
        self._account = IaasLevel('subscription', self._subscription, '')
        try:
            self._resource_group_list = resource_client.resource_groups.list()
        except Exception as ex:
            print('AzureControllerError > %s' % ex.args[0])
            raise


    def list_vm(self):
        res_type = 'vm'
        compute_client =  ComputeManagementClient(self._credential, self._subscription)
        network_client = NetworkManagementClient(self._credential, self._subscription)

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
                public_ip = public_ip,
                tags = vm_tags
            )

            res_parent = IaasLevel('resource_group', vm_rg, '')
            res_loc = IaasLocation('location', vm_loc, '')

            res = IaasResource(
                provider = self._provider,
                account = self._account,
                parent = res_parent,
                location = res_loc,
                instance = res_inst
            )

            instances.append(res)

        return instances


    def list_lb(self):
        res_type = 'lb'
        network_client = NetworkManagementClient(self._credential, self._subscription)

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
                ports = res_ports,
                tags = lb_tags
            )

            res_parent = IaasLevel('resource_group', lb_rg, '')
            res_loc = IaasLocation('location', lb_loc, '')

            res = IaasResource(
                provider = self._provider,
                account = self._account,
                parent = res_parent,
                location = res_loc,
                instance = res_inst
            )
            instances.append(res)

        return instances


if __name__ == '__main__':
    azr = AzureController('all')
    my_vms = azr.list_vm()
    print(my_vms)
    my_lbs = azr.list_lb()
    print(my_lbs)

