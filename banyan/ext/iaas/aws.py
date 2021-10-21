import logging
import os
from typing import List

from banyan.ext.iaas.base import IaasAccount, IaasResource, IaasInstance, IaasRegion, IaasConf, IaasController

import boto3


class AwsController(IaasController):
    def __init__(self, filter_by_region: str, filter_by_tag_name: str = None):
        self._provider = 'aws'
        _aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        _aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        if not _aws_access_key_id:
            _creds = IaasConf.get_creds(self._provider)
            _aws_access_key_id = _creds['aws_access_key_id']
            _aws_secret_access_key = _creds['aws_secret_access_key']

        try:
            self._session = boto3.Session(
                aws_access_key_id = _aws_access_key_id,
                aws_secret_access_key = _aws_secret_access_key,
            )
            sts_client = self._session.client('sts')
            ec2_client = self._session.client('ec2')
        except Exception as ex:
            print('BotoError (AWS SDK) > %s' % ex.args[0])
            raise
        self._filter_by_region = filter_by_region
        self._filter_by_tag_name = filter_by_tag_name

        try:
            account_id = sts_client.get_caller_identity().get('Account')
            #NOTE: cannot get account_name without requiring IAM or Organizations permissions
            self._account = IaasAccount('account', account_id)
            self._region_list = ec2_client.describe_regions().get('Regions')
        except Exception as ex:
            print('AwsControllerError > %s' % ex.args[0])
            raise


    def list_ec2(self):
        res_type = 'ec2'
        instances: List[IaasResource] = list()

        # loop through all regions
        for region_obj in self._region_list:
            region_name = region_obj.get('RegionName')
            if self._filter_by_region != 'all' and self._filter_by_region != region_name:
                continue

            res_regn = IaasRegion('region', region_name)
            ec2 = self._session.resource(res_type, region_name=region_name)

            filters = []
            if self._filter_by_tag_name:
                filters.append({
                    'Name': 'tag:%s' % self._filter_by_tag_name,
                    'Values': ['*']
                })
            vm_list = list(ec2.instances.filter(Filters=filters))

            for vm in vm_list:
                res_tags = dict()
                res_name = ''
                for tag in vm.tags:
                    key = tag['Key']
                    val = tag['Value']
                    res_tags[key] = val
                    # EC2 resource name in tag called Name
                    if key == 'Name':
                        res_name = val 

                res_inst = IaasInstance(
                    type = res_type,
                    id = vm.instance_id,
                    name = res_name,
                    private_ip = vm.private_ip_address,
                    private_dns_name = vm.private_dns_name,
                    public_ip = vm.public_ip_address,
                    public_dns_name = vm.public_dns_name
                )

                res = IaasResource(
                    provider = self._provider,
                    account = self._account,
                    region = res_regn,
                    instance = res_inst,
                    tags = res_tags
                )
                instances.append(res)

        return instances


    def list_rds(self):
        res_type = 'rds'
        instances: List[IaasResource] = list()

        # loop through all regions
        for region_obj in self._region_list:
            region_name = region_obj.get('RegionName')
            if self._filter_by_region != 'all' and self._filter_by_region != region_name:
                continue

            res_regn = IaasRegion('region', region_name)
            rds_client = self._session.client(res_type, region_name=region_name)

            describe_db_instances = rds_client.describe_db_instances(Filters=[], MaxRecords=100)

            db_instances = describe_db_instances.get('DBInstances')
            for inst in db_instances:
                res_tags = dict()
                for tag in inst.get('Tags', dict()):
                    key = tag['Key']
                    val = tag['Value']
                    res_tags[key] = val

                # implement tag-based filtering ourselves because RDS Client doesn't
                if self._filter_by_tag_name and not res_tags.get(self._filter_by_tag_name):
                    continue

                res_inst = IaasInstance(
                    type = res_type,
                    id = inst.get('DBInstanceArn'),
                    name = inst.get('DBInstanceIdentifier'),
                    public_dns_name = inst.get('Endpoint').get('Address'),
                    ports = ['%d/tcp' % inst.get('Endpoint').get('Port')]
                )
                
                res = IaasResource(
                    provider = self._provider,
                    account = self._account,
                    region = res_regn,
                    instance = res_inst,
                    tags = res_tags
                )
                instances.append(res)
        
        return instances


    def list_elb(self):
        res_type = 'elb'
        instances: List[IaasResource] = list()

        # loop through all regions
        for region_obj in self._region_list:
            region_name = region_obj.get('RegionName')
            if self._filter_by_region != 'all' and self._filter_by_region != region_name:
                continue

            res_regn = IaasRegion('region', region_name)
            elbv1_client = self._session.client('elb', region_name=region_name) # classic
            elbv2_client = self._session.client('elbv2', region_name=region_name) # current

            describe_v1_lbs = elbv1_client.describe_load_balancers(PageSize=100)
            describe_v2_lbs = elbv2_client.describe_load_balancers(PageSize=100)

            v1_lbs = describe_v1_lbs.get('LoadBalancerDescriptions')
            for v1_lb in v1_lbs:
                describe_tags = elbv1_client.describe_tags(LoadBalancerNames=[v1_lb.get('LoadBalancerName')])
                res_tags = dict()
                for tag in describe_tags.get('TagDescriptions', list())[0].get('Tags', dict()):
                    key = tag['Key']
                    val = tag['Value']
                    res_tags[key] = val

                # add a tag for internet-facing | internal
                res_tags['Scheme'] = v1_lb.get('Scheme')

                # implement tag-based filtering ourselves because ELB API doesn't
                if self._filter_by_tag_name and not res_tags.get(self._filter_by_tag_name):
                    continue

                res_ports = list()
                for ld in v1_lb.get('ListenerDescriptions'):
                    ld_l = ld.get('Listener')
                    res_ports.append('%d/%s' % (ld_l.get('LoadBalancerPort'), ld_l.get('Protocol')))

                res_inst = IaasInstance(
                    type = res_type,
                    id = v1_lb.get('LoadBalancerName'),
                    name = v1_lb.get('LoadBalancerName'),
                    public_dns_name = v1_lb.get('DNSName'),  # public DNS, resolves to public or private IP
                    ports = res_ports
                )

                res = IaasResource(
                    provider = self._provider,
                    account = self._account,
                    region = res_regn,
                    instance = res_inst,
                    tags = res_tags
                )
                instances.append(res)

            v2_lbs = describe_v2_lbs.get('LoadBalancers')
            for v2_lb in v2_lbs:
                describe_tags = elbv2_client.describe_tags(ResourceArns=[v2_lb.get('LoadBalancerArn')])
                res_tags = dict()
                for tag in describe_tags.get('TagDescriptions', list())[0].get('Tags', dict()):
                    key = tag['Key']
                    val = tag['Value']
                    res_tags[key] = val

                # add a tag for internet-facing | internal
                res_tags['Scheme'] = v2_lb.get('Scheme')

                # implement tag-based filtering ourselves because ELB API doesn't
                if self._filter_by_tag_name and not res_tags.get(self._filter_by_tag_name):
                    continue

                res_ports = list()
                describe_listeners = elbv2_client.describe_listeners(LoadBalancerArn=v2_lb.get('LoadBalancerArn'))
                for ld in describe_listeners.get('Listeners'):
                    res_ports.append('%d/%s' % (ld.get('Port'), ld.get('Protocol')))

                res_inst = IaasInstance(
                    type = res_type,
                    id = v2_lb.get('LoadBalancerArn'),
                    name = v2_lb.get('LoadBalancerName'),
                    public_dns_name = v2_lb.get('DNSName'),  # public DNS, resolves to public or private IP
                    ports = res_ports
                )

                res = IaasResource(
                    provider = self._provider,
                    account = self._account,
                    region = res_regn,
                    instance = res_inst,
                    tags = res_tags
                )
                instances.append(res)

        return instances


if __name__ == '__main__':
    aws = AwsController('us-east-2', None)
    ec2_instances = aws.list_ec2()
    print(ec2_instances)
    rds_instances = aws.list_rds()
    print(rds_instances)
    elb_instances = aws.list_elb()
    print(elb_instances)

