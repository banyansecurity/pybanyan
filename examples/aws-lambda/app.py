from typing import List
from time import sleep
import os

from banyan.api import BanyanApiClient
from banyan.model.cloud_resource import CloudResourceInfo
from banyan.controllers.base import Base
from banyan.ext.iaas.aws import AwsController
from banyan.ext.iaas.base import IaasResource


# sync_aws
def handler(event, context):
    print("--> entering Lambda handler")

    # env vars: BANYAN_API_URL, BANYAN_REFRESH_TOKEN
    bnn = BanyanApiClient()

    resource_type = os.getenv('RESOURCE_TYPE')
    region = os.getenv('REGION')
    tag_name = os.getenv('TAG_NAME')
    rt = resource_type.lower()

    # env vars: none (Lambda sets the correct env vars automatically)
    aws = AwsController(region, tag_name)

    instances: List[IaasResource] = list()
    if rt == 'ec2' or rt == 'all':
        instances += aws.list_ec2()
    if rt == 'rds' or rt == 'all':
        instances += aws.list_rds()
    if rt == 'elb' or rt == 'all':
        instances += aws.list_elb() 

    if len(instances) == 0:
        print('--> No AWS resources to sync')
        return

    params={'cloud_provider': aws.provider, 'resource_type': rt, 'region': region}
    synced_resources: List[CloudResourceInfo] = bnn.cloud_resources.list(params=Base.sanitize_alls(params))
    added_instances = Base.added_iaas_resources(instances, synced_resources)

    if len(added_instances) == 0:
        print('--> No new AWS resources to sync')
        return

    for instance in added_instances:
        res = Base.convert_iaas_resource(instance)
        bnn.cloud_resources.create(res)
        print('\n--> Added AWS resource id(name): %s(%s)' % (res.resource_id, res.resource_name))
        sleep(0.05)
        
    print('\n--> Sync with AWS successful.')


if __name__ == '__main__':
    handler(None, None)
