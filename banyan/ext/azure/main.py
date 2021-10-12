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

@dataclass
class AzureResourceModel:
    subscription: str            # Azure Subscription is within an Account 
    
    resource_group: str          # Azure Resource Group is within a Subscription
    location: str
    
    type: str
    id: str
    name: str = ''

    public_dns_name: str = ''
    public_ip: str = ''
    private_dns_name: str = ''
    private_ip: str = ''
    ports: str = ''
    tags: Dict = field(default_factory=dict)

    PROVIDER = 'AZURE'

class AzureController:
    def __init__(self, resource_group: str = None, location: str = None, tag_name: str = None):
        try:
            self._credential = DefaultAzureCredential()
            self._subscription = os.environ["AZURE_SUBSCRIPTION_ID"]
            self._resource_client = ResourceManagementClient(self._credential, self._subscription)
        except Exception as ex:
            print('AzureSDKError > %s' % ex.args[0])
            raise
        self._resource_group_list = self._resource_client.resource_groups.list()
        self._resource_group = resource_group
        self._location = location
        self._tag_name = tag_name


    def list_vm(self):
        resource_type = 'vm'
        compute_client =  ComputeManagementClient(self._credential, self._subscription)
        network_client = NetworkManagementClient(self._credential, self._subscription)

        # VMs in all resource groups
        vm_list = compute_client.virtual_machines.list_all()

        instances: List[AzureResourceModel] = list()
        for vm in list(vm_list):
            #print(json.dumps(vm.as_dict(), indent=4))
            vm_loc = vm.location
            vm_tags = vm.tags or dict()
            vm_reference = vm.id.split('/')
            vm_rg = vm_reference[4]
            ni_reference = vm.network_profile.network_interfaces[0].id.split('/')
            ni_name = ni_reference[8]

            # implement filtering
            if self._resource_group and self._resource_group != vm_rg:
                continue
            if self._location and self._location != vm_loc:
                continue
            if self._tag_name and not vm_tags.get(self._tag_name):
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

            res = AzureResourceModel(
                subscription = self._subscription,
                resource_group = vm_rg,
                location = vm_loc,
                type = resource_type,
                id = vm.id,
                name = vm.name,
                public_ip = public_ip,
                private_ip = private_ip,
                tags = vm_tags
            )

            instances.append(res)

        return instances

    def list_lb(self):
        resource_type = 'lb'
        network_client = NetworkManagementClient(self._credential, self._subscription)

        lb_list = network_client.load_balancers.list_all()

        instances: List[AzureResourceModel] = list()
        for lb in list(lb_list):
            #print(json.dumps(lb.as_dict(), indent=4))
            lb_loc = lb.location
            lb_tags = lb.tags or dict()
            lb_reference = lb.id.split('/')
            lb_rg = lb_reference[4]

            # implement filtering
            if self._location and self._location != lb_loc:
                continue
            if self._resource_group and self._resource_group != lb_rg:
                continue
            if self._tag_name and not lb_tags.get(self._tag_name):
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

            res = AzureResourceModel(
                subscription = self._subscription,
                resource_group = lb_rg,
                location = lb_loc,
                type = resource_type,
                id = lb.id,
                name = lb.name,
                public_ip = public_ip,
                private_ip = private_ip,
                tags = lb_tags
            )

            valid_ports = []
            lb_rules = lb.load_balancing_rules
            for lb_rule in list(lb_rules):
                valid_ports.append(f'{lb_rule.frontend_port}/{lb_rule.protocol}')
            res.ports = ','.join(valid_ports)

            instances.append(res)

        return instances


if __name__ == '__main__':
    azr = AzureController(None,'eastus2','banyan:discovery')
    my_vms = azr.list_vm()
    print(my_vms)
    my_lbs = azr.list_lb()
    print(my_lbs)

