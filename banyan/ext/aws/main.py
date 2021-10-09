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


class Ec2Controller:
    TYPE = 'ec2'

    #TODO: support more filters - region, vpc, owner
    def list(self, tag_name: str = None, tag_values: list = ['*'], check_security_groups: bool = False):
        try:
            session = boto3.session.Session()
            sts = session.client('sts')
            client = session.client(Ec2Controller.TYPE)
        except Exception as ex:
            print('BotoError (AWS SDK) > %s' % ex.args[0])
            raise

        caller_identity = sts.get_caller_identity()

        filters = []
        if tag_name:
            filters.append({
                'Name': 'tag:%s' % tag_name,
                'Values': tag_values
            })
        describe_instances = client.describe_instances(Filters=filters, MaxResults=100)
       
        instances: List[AwsResourceModel] = list()
        reservations = describe_instances.get('Reservations')
        for reservation in reservations:
            for inst in reservation.get('Instances'):
                res = AwsResourceModel(
                    account = caller_identity.get('Account'),
                    region = session.region_name,
                    type = Ec2Controller.TYPE,
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


class RdsController:
    TYPE = 'rds'

    def list(self, tag_name: str = None):
        try:
            session = boto3.session.Session()
            sts = session.client('sts')
            client = session.client(RdsController.TYPE)
        except Exception as ex:
            print('BotoError (AWS SDK) > %s' % ex.args[0])
            raise        

        caller_identity  = sts.get_caller_identity()
        describe_db_instances = client.describe_db_instances(Filters=[], MaxRecords=100)

        instances: List[AwsResourceModel] = list()
        db_instances = describe_db_instances.get('DBInstances')
        for inst in db_instances:
            res = AwsResourceModel(
                    account = caller_identity.get('Account'),
                    region = session.region_name,
                    type = RdsController.TYPE,
                    id = inst.get('DBInstanceArn'),
                    name = inst.get('DBInstanceIdentifier'),
                    public_dns_name = inst.get('Endpoint').get('Address'),
                    ports = '%d/tcp' % inst.get('Endpoint').get('Port'),
                    tags = inst.get('TagList')
            )

            # implement tag filtering ourselves, don't implement tag_values
            if not tag_name:
                instances.append(res)
            else:
                for tag in res.tags:
                    if tag['Key'] == tag_name:
                        # assume tag_values == ['*']:
                        instances.append(res)
                        break
        
        return instances


class ElbController:
    TYPE = 'elb'
    TYPE_V1 = 'elb'     # classic
    TYPE_V2 = 'elbv2'   # current

    def list(self, tag_name: str = None):
        try:
            session = boto3.session.Session()
            sts = session.client('sts')
            client_v1 = session.client(ElbController.TYPE_V1)
            client_v2 = session.client(ElbController.TYPE_V2)
        except Exception as ex:
            print('BotoError (AWS SDK) > %s' % ex.args[0])
            raise        

        caller_identity  = sts.get_caller_identity()        
        describe_v1_lbs = client_v1.describe_load_balancers(PageSize=100)
        describe_v2_lbs = client_v2.describe_load_balancers(PageSize=100)

        instances: List[AwsResourceModel] = list()
        v1_lbs = describe_v1_lbs.get('LoadBalancerDescriptions')
        for v1_lb in v1_lbs:
            res = AwsResourceModel(
                    account = caller_identity.get('Account'),
                    region = session.region_name,
                    type = ElbController.TYPE_V1,
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

            # implement tag filtering ourselves, don't implement tag_values
            if not tag_name:
                instances.append(res)
            else:
                for tag in res.tags:
                    if tag['Key'] == tag_name:
                        # assume tag_values == ['*']:
                        instances.append(res)
                        break

        v2_lbs = describe_v2_lbs.get('LoadBalancers')
        for v2_lb in v2_lbs:
            res = AwsResourceModel(
                    account = caller_identity.get('Account'),
                    region = session.region_name,
                    type = ElbController.TYPE_V2,
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

            # implement tag filtering ourselves, don't implement tag_values
            if not tag_name:
                instances.append(res)
            else:
                for tag in res.tags:
                    if tag['Key'] == tag_name:
                        # assume tag_values == ['*']:
                        instances.append(res)
                        break

        return instances



if __name__ == '__main__':
    ec2 = Ec2Controller()
    ec2_instances = ec2.list('', ['*'], True)
    print(ec2_instances)
    rds = RdsController()
    rds_instances = rds.list('')
    print(rds_instances)
    elb = ElbController()
    elb_instances = elb.list('')
    print(elb_instances)

