from typing import List, ClassVar, Type, Optional, Union
from dataclasses import dataclass
import os

try: 
    from azure.identity import DefaultAzureCredential
    from azure.mgmt.resource import ResourceManagementClient
    from azure.mgmt.compute import ComputeManagementClient
    from azure.mgmt.network import NetworkManagementClient
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise

@dataclass
class VmModel:
    class Meta:
        help = "Azure VM Model"
    
    location: str
    group: str
    id: str
    name: str
    public_ip: str
    private_ip: str
    tags: List
    cloud_provider: str = 'Azure'
    type: str = 'Microsoft.Compute/virtualMachines'

class VmController:
    class Meta:
        help = "Azure VM Controller"

    #TODO: support more filters - resource_group, location, etc
    def list(self, tag_name: str = None):
        try:
            credential = DefaultAzureCredential()
            subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
            resource_client = ResourceManagementClient(credential, subscription_id)
            compute_client =  ComputeManagementClient(credential, subscription_id)
            network_client = NetworkManagementClient(credential,subscription_id)
        except Exception as ex:
            print('AzureSDKError > %s' % ex.args[0])
            raise

        instances: List[VmModel] = list()
        vm_list = compute_client.virtual_machines.list_all()
        for vm in list(vm_list):
            if tag_name is not None and not vm.tags.get(tag_name):
                continue

            ni_reference = vm.network_profile.network_interfaces[0]
            ni_reference = ni_reference.id.split('/')
            ni_group = ni_reference[4]
            ni_name = ni_reference[8]

            net_interface = network_client.network_interfaces.get(ni_group, ni_name)
            pub_ip_reference = net_interface.ip_configurations[0].public_ip_address
            pub_ip_reference = pub_ip_reference.id.split('/')
            pub_ip_group = pub_ip_reference[4]
            pub_ip_name = pub_ip_reference[8]

            public_ip = network_client.public_ip_addresses.get(pub_ip_group, pub_ip_name)
            public_ip = public_ip.ip_address
            
            private_ip = net_interface.ip_configurations[0].private_ip_address

            res = VmModel(
                vm.location,
                ni_group,
                vm.id,
                vm.name,
                public_ip,
                private_ip,
                vm.tags
            )
            instances.append(res)

        return instances


if __name__ == '__main__':
    vmc = VmController()
    my_vms = vmc.list('Env')
    print(my_vms)

