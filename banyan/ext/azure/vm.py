from typing import List, ClassVar, Type, Optional, Union
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
    subscription: str   # Azure Subscription is within an Account 
    resource_group: str          # Azure Resource Group
    location: str
    id: str
    name: str = ''
    public_dns_name: str = ''
    public_ip: str = ''
    private_dns_name: str = ''
    private_ip: str = ''
    ports: str = ''
    tags: List = field(default_factory=list)

    PROVIDER = 'AZURE'

class AzureController:
    def __init__(self, location: str = None, tag_name: str = None):
        try:
            self._credential = DefaultAzureCredential()
            self._subscription = os.environ["AZURE_SUBSCRIPTION_ID"]
            self._resource_client = ResourceManagementClient(self._credential, self._subscription)
        except Exception as ex:
            print('AzureSDKError > %s' % ex.args[0])
            raise
        self._resource_client.resource_groups.list()
        self._location = location
        self._tag_name = tag_name


    def list_vm(self):
        compute_client =  ComputeManagementClient(self._credential, self._subscription)
        network_client = NetworkManagementClient(self._credential, self._subscription)

        vm_list = list()
        if self._location:
            vm_list = compute_client.virtual_machines.list_by_location(self._location)
        else:
            vm_list = compute_client.virtual_machines.list_all()

        instances: List[AzureResourceModel] = list()
        for vm in list(vm_list):
            print(json.dumps(vm.as_dict(), indent=4))
            vm_reference = vm.id.split('/')
            vm_rg = vm_reference[4]
            ni_reference = vm.network_profile.network_interfaces[0].id.split('/')
            ni_name = ni_reference[8]

            net_interface = network_client.network_interfaces.get(vm_rg, ni_name)
            print(json.dumps(net_interface.as_dict(), indent=4))
            
            private_ip = net_interface.ip_configurations[0].private_ip_address

            res = AzureResourceModel(
                subscription = self._subscription,
                resource_group = vm_rg,
                location = vm.location,
                id = vm.id,
                name = vm.name,
                private_ip = private_ip,
                tags = vm.tags
            )

            if self._tag_name and vm.tags and not vm.tags.get(self._tag_name):
                continue

            instances.append(res)

        return instances


if __name__ == '__main__':
    azr = AzureController()
    my_vms = azr.list_vm()
    print(my_vms)

