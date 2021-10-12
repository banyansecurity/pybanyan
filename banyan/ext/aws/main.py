from typing import List, ClassVar, Type, Optional, Union
from dataclasses import dataclass, field

try:
    import boto3
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise

@dataclass
class AwsResourceModel:
    account: str

    region: str

    type: str
    id: str
    name: str = ''
    
    public_dns_name: str = ''
    public_ip: str = ''
    private_dns_name: str = ''
    private_ip: str = ''
    ports: str = ''
    tags: List = field(default_factory=list)

    PROVIDER = 'AWS'

class AwsController:
    #TODO: support more filters - vpc, owner
    def __init__(self, region: str = None, tag_name: str = None):
        try:
            self._session = boto3.session.Session(region_name=region)
            self._sts = self._session.client('sts')
        except Exception as ex:
            print('BotoError (AWS SDK) > %s' % ex.args[0])
            raise        
        self._provider = 'AWS'
        self._region = self._session.region_name
        self._account = self._sts.get_caller_identity().get('Account')
        self._tag_name = tag_name
        

    def list_ec2(self, check_security_groups: bool = False):
        resource_type = 'ec2'
        client = self._session.client(resource_type)

        filters = []
        if self._tag_name:
            filters.append({
                'Name': 'tag:%s' % self._tag_name,
                'Values': ['*']
            })
        describe_instances = client.describe_instances(Filters=filters, MaxResults=100)
       
        instances: List[AwsResourceModel] = list()
        reservations = describe_instances.get('Reservations')
        for reservation in reservations:
            for inst in reservation.get('Instances'):
                res = AwsResourceModel(
                    account = self._account,
                    region = self._region,
                    type = resource_type,
                    id = inst.get('InstanceId'),
                    public_ip = inst.get('PublicIpAddress'),
                    private_ip = inst.get('PrivateIpAddress'),
                    tags = inst.get('Tags')
                )

                # EC2 resource name in tag called Name
                for tag in res.tags:
                    if tag['Key'] == 'Name':
                        res.name = tag['Value']
                        break
                
                # guess ports from inbound security groups
                if check_security_groups:
                    security_groups = inst.get('SecurityGroups')
                    listeners = []
                    valid_ports = []
                    for security_group in security_groups:
                        sg_details = client.describe_security_groups(GroupIds=[security_group['GroupId']])
                        for sg_detail in sg_details.get('SecurityGroups'):
                            inbound_rules = sg_detail.get('IpPermissions')
                            if inbound_rules:
                                for inbound_rule in inbound_rules:
                                    listeners.append({
                                        'port': inbound_rule.get('FromPort'), 
                                        'protocol': inbound_rule.get('IpProtocol')
                                    })                    
                    for listener in listeners:
                        if listener['port'] and listener['port'] > 0:
                            valid_ports.append(f'{listener["port"]}/{listener["protocol"]}')
                    res.ports = ','.join(valid_ports)

                instances.append(res)

        return instances


    def list_rds(self):
        resource_type = 'rds'
        client = self._session.client(resource_type)
        
        describe_db_instances = client.describe_db_instances(Filters=[], MaxRecords=100)

        instances: List[AwsResourceModel] = list()
        db_instances = describe_db_instances.get('DBInstances')
        for inst in db_instances:
            res = AwsResourceModel(
                    account = self._account,
                    region = self._region,
                    type = resource_type,
                    id = inst.get('DBInstanceArn'),
                    name = inst.get('DBInstanceIdentifier'),
                    public_dns_name = inst.get('Endpoint').get('Address'),
                    ports = '%d/tcp' % inst.get('Endpoint').get('Port'),
                    tags = inst.get('TagList')
            )

            # implement tag-based filtering ourselves because RDS API doesn't
            if not self._tag_name:
                instances.append(res)
            else:
                for tag in res.tags:
                    if tag['Key'] == self._tag_name:
                        instances.append(res)
                        break
        
        return instances


    def list_elb(self):
        resource_type = 'elb'
        resource_type_v1 = 'elb'    # classic
        resource_type_v2 = 'elbv2'  # current
        client_v1 = self._session.client(resource_type_v1)
        client_v2 = self._session.client(resource_type_v2)
        
        describe_v1_lbs = client_v1.describe_load_balancers(PageSize=100)
        describe_v2_lbs = client_v2.describe_load_balancers(PageSize=100)

        instances: List[AwsResourceModel] = list()
        v1_lbs = describe_v1_lbs.get('LoadBalancerDescriptions')
        for v1_lb in v1_lbs:
            res = AwsResourceModel(
                    account = self._account,
                    region = self._region,
                    type = resource_type,
                    id = v1_lb.get('LoadBalancerName'),
                    name = v1_lb.get('LoadBalancerName'),
                    public_dns_name = v1_lb.get('DNSName')  # public DNS, resolves to public or private IP
            )

            listeners = []
            valid_ports = []
            for ld in v1_lb.get('ListenerDescriptions'):
                ld_l = ld.get('Listener')
                listeners.append({
                    'port': ld_l.get('LoadBalancerPort'),
                    'protocol': ld_l.get('Protocol')
                })
            for listener in listeners:
                if listener['port'] and listener['port'] > 0:
                    valid_ports.append(f'{listener["port"]}/{listener["protocol"]}')            
            res.ports = ','.join(valid_ports)

            describe_tags = client_v1.describe_tags(LoadBalancerNames=[v1_lb.get('LoadBalancerName')])
            tags = describe_tags.get('TagDescriptions')[0].get('Tags')
            res.tags = tags

            # add a tag for internet-facing | internal
            res.tags.append({
                "Key": "Scheme",
                "Value": v1_lb.get('Scheme')
            })

            # implement tag-based filtering ourselves because ELB API doesn't
            if not self._tag_name:
                instances.append(res)
            else:
                for tag in res.tags:
                    if tag['Key'] == self._tag_name:
                        instances.append(res)
                        break

        v2_lbs = describe_v2_lbs.get('LoadBalancers')
        for v2_lb in v2_lbs:
            res = AwsResourceModel(
                    account = self._account,
                    region = self._region,
                    type = resource_type,
                    id = v2_lb.get('LoadBalancerArn'),
                    name = v2_lb.get('LoadBalancerName'),
                    public_dns_name = v2_lb.get('DNSName')  # public DNS, resolves to public or private IP
            )

            listeners = []
            valid_ports = []
            describe_listeners = client_v2.describe_listeners(LoadBalancerArn=v2_lb.get('LoadBalancerArn'))
            for ld in describe_listeners.get('Listeners'):
                listeners.append({
                    'port': ld.get('Port'),
                    'protocol': ld.get('Protocol')
                })
            for listener in listeners:
                if listener['port'] and listener['port'] > 0:
                    valid_ports.append(f'{listener["port"]}/{listener["protocol"]}')            
            res.ports = ','.join(valid_ports)

            describe_tags = client_v2.describe_tags(ResourceArns=[v2_lb.get('LoadBalancerArn')])
            tags = describe_tags.get('TagDescriptions')[0].get('Tags')
            res.tags = tags

            # add a tag for internet-facing | internal
            res.tags.append({
                "Key": "Scheme",
                "Value": v2_lb.get('Scheme')
            })

            # implement tag-based filtering ourselves because ELB API doesn't
            if not self._tag_name:
                instances.append(res)
            else:
                for tag in res.tags:
                    if tag['Key'] == self._tag_name:
                        instances.append(res)
                        break

        return instances



if __name__ == '__main__':
    aws = AwsController('us-east-1', 'banyan:discovery')
    ec2_instances = aws.list_ec2(False)
    print(ec2_instances)
    rds_instances = aws.list_rds()
    print(rds_instances)
    elb_instances = aws.list_elb()
    print(elb_instances)

