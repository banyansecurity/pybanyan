from typing import List, Dict, ClassVar, Type, Optional, Union
from dataclasses import dataclass, field
import os

try:
    import googleapiclient.discovery
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
    

class GcpController:
    def __init__(self, filter_by_project: str, filter_by_zone: str = None, filter_by_label_name: str = None):
        try:
            gcp_creds = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
            self._cloud_client = googleapiclient.discovery.build('cloudresourcemanager', 'v1')
        except Exception as ex:
            print('GoogleApiClientError > %s' % ex.args[0])
            raise
        self._filter_by_project = filter_by_project
        self._filter_by_zone = filter_by_zone
        self._filter_by_label_name = filter_by_label_name    

        self._provider = 'GCP'
        try:
            self._project_list = self._cloud_client.projects().list().execute()
            account = self._project_list.get('projects')[0].get('parent')
            self._account = IaasLevel(account.get('type'), account.get('id'), '')
        except Exception as ex:
            print('GcpControllerError > %s' % ex.args[0])
            raise
        

    def list_vm(self):
        res_type = 'vm'
        compute_client = googleapiclient.discovery.build('compute', 'v1')

        instances: List[IaasResource] = list()

        # get VMs by Project
        for project_obj in list(self._project_list.get('projects')):
            project_id = project_obj.get('projectId')
            project_name = project_obj.get('name')
            if self._filter_by_project != 'all' and self._filter_by_project != project_id:
                continue

            # check for instances in all zones
            aggr_obj = compute_client.instances().aggregatedList(project=project_id).execute()

            zone_list = list()
            for item_key in aggr_obj.get('items'):
                item_val = aggr_obj.get('items').get(item_key)
                if item_val.get('instances'):
                    zone_list.append(item_key.replace('zones/', ''))

            for zone in zone_list:
                if self._filter_by_zone and self._filter_by_zone != zone:
                    continue

                vm_list_obj = compute_client.instances().list(project=project_id, zone=zone, maxResults=100).execute()
                for vm in vm_list_obj.get('items'):
                    #print(vm)
                    vm_labels = vm.get('labels') or dict()
                    if self._filter_by_label_name and not vm_labels.get(self._filter_by_label_name):
                        continue

                    # check network interface for address
                    net_interface = vm.get('networkInterfaces')[0]
                    private_ip = net_interface.get('networkIP') 
                    public_ip = ''
                    if net_interface.get('accessConfigs'):
                        access_conf = net_interface.get('accessConfigs')[0]
                        if access_conf.get('type') == 'ONE_TO_ONE_NAT':
                            public_ip = access_conf.get('natIP')

                    res_inst = IaasInstance(
                        type = res_type,
                        id = vm.get('id'),
                        name = vm.get('name'),
                        public_ip = public_ip,
                        private_ip = private_ip,
                        tags = vm_labels
                    )

                    res_parent = IaasLevel('project', project_id, project_name)
                    res_loc = IaasLocation('zone', zone, '')

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
    gcp = GcpController('all', 'us-east4-b')
    my_vms = gcp.list_vm()
    print(my_vms)
