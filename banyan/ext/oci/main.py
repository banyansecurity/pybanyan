from typing import List, Dict, ClassVar, Type, Optional, Union
from dataclasses import dataclass, field
import os

try:
    import oci
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise

@dataclass
class OciResourceModel:
    tenancy: str

    compartment: str
    region: str

    type: str
    id: str
    name: str

    public_dns_name: str = ''
    public_ip: str = ''
    private_dns_name: str = ''
    private_ip: str = ''
    ports: str = ''
    tags: Dict = field(default_factory=dict)

    PROVIDER = 'OCI'


class OciController:
    def __init__(self, compartment: str = None, region: str = None, tag_name: str = None):
        try:
            self._config = oci.config.from_file()
            self._tenancy = self._config.get('tenancy')
            self._identity_client = oci.identity.IdentityClient(self._config)
        except Exception as ex:
            print('OCISDKError > %s' % ex.args[0])
            raise
        # all compartments from root, parent is in compartment_id
        resp = self._identity_client.list_compartments(compartment_id=self._tenancy, compartment_id_in_subtree=True)
        self._compartment_list = resp.data
        self._compartment = compartment
        self._region = region
        self._tag_name = tag_name

    
    def list_vm(self):
        resource_type = 'vm'
        compute_client = oci.core.ComputeClient(self._config)

        instances: List[OciResourceModel] = list()

        # get VMs by Compartment
        for compartment_obj in self._compartment_list:
            #print(compartment_obj)
            if self._compartment and self._compartment != compartment_obj.name:
                continue

            resp = compute_client.list_instances(compartment_id=compartment_obj.id)
            vm_list = resp.data

            for vm in vm_list:
                #print(vm)

                res = OciResourceModel(
                    tenancy = self._tenancy,
                    compartment = compartment_obj.name,
                    region = vm.region,
                    type = resource_type,
                    id =  vm.id,
                    name = vm.display_name                    
                )

                instances.append(res)

        return instances


if __name__ == '__main__':
    orl = OciController()
    my_vms = orl.list_vm()
    print(my_vms)