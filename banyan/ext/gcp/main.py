from typing import List, Dict, ClassVar, Type, Optional, Union
from dataclasses import dataclass, field
import os

try:
    import googleapiclient.discovery
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise

@dataclass
class GcpResourceModel:
    account: str
    project: str
    zone: str
    type: str
    id: str
    name: str = ''
    public_dns_name: str = ''
    public_ip: str = ''
    private_dns_name: str = ''
    private_ip: str = ''
    ports: str = ''
    labels: Dict = field(default_factory=dict)  # in GCP, tags used for networking

    PROVIDER = 'GCP'


class GcpController:
    def __init__(self, project: str = None, zone: str = None, label_name: str = None):
        try:
            gcp_creds = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
            self._cloud_client = googleapiclient.discovery.build('cloudresourcemanager', 'v1')
        except Exception as ex:
            print('GoogleApiClientError > %s' % ex.args[0])
            raise
        self._project_list = self._cloud_client.projects().list().execute()
        self._account = self._project_list.get('projects')[0].get('parent').get('id')
        self._project = project
        self._zone = zone
        self._label_name = label_name    

    def list_vm(self):
        resource_type = 'vm'
        compute_client = googleapiclient.discovery.build('compute', 'v1')

        instances: List[GcpResourceModel] = list()

        # get VMs by Project
        for project_obj in list(self._project_list.get('projects')):
            project_id = project_obj.get('projectId')
            project_name = project_obj.get('name')
            if self._project and self._project != project_name:
                continue

            # all zones
            aggr_obj = compute_client.instances().aggregatedList(project=project_id).execute()

            zone_list = list()
            for item_key in aggr_obj.get('items'):
                item_val = aggr_obj.get('items').get(item_key)
                if item_val.get('instances'):
                    zone_list.append(item_key.replace('zones/', ''))

            for zone in zone_list:
                if self._zone and self._zone != zone:
                    continue

                vm_list_obj = compute_client.instances().list(project=project_id, zone=zone, maxResults=100).execute()
                for vm in vm_list_obj.get('items'):
                    #print(vm)
                    vm_labels = vm.get('labels') or dict()
                    if self._label_name and not vm_labels.get(self._label_name):
                        continue

                    # check network interface for address
                    net_interface = vm.get('networkInterfaces')[0]
                    private_ip = net_interface.get('networkIP') 
                    public_ip = ''
                    if net_interface.get('accessConfigs'):
                        access_conf = net_interface.get('accessConfigs')[0]
                        if access_conf.get('type') == 'ONE_TO_ONE_NAT':
                            public_ip = access_conf.get('natIP')

                    res = GcpResourceModel(
                        account = self._account,
                        project = project_name,
                        zone = zone,
                        type = resource_type,
                        id = vm.get('id'),
                        name = vm.get('name'),
                        public_ip = public_ip,
                        private_ip = private_ip,
                        labels = vm_labels
                    )
                    print(res)

        return


if __name__ == '__main__':
    gcp = GcpController()
    my_vms = gcp.list_vm()
    print(my_vms)
