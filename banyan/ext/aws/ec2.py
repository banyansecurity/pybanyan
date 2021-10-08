from typing import List, ClassVar, Type, Optional, Union
from dataclasses import dataclass

try:
    import boto3
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise

@dataclass
class Ec2Model:
    class Meta:
        help = "AWS EC2 Model"

    account: str
    region: str
    id: str
    public_ip: str
    private_ip: str
    tags: List
    cloud_provider: str = 'AWS'
    type: str = 'ec2'
    name: str = ''
    ports: str = ''


class Ec2Controller:
    class Meta:
        help = "AWS EC2 Controller"

    #TODO: support more filters - region, vpc, owner
    def list(self, tag_name: str = None, tag_values: list = ['*'], check_security_groups: bool = False):
        try:
            session = boto3.session.Session()
            sts = session.client('sts')
            client = session.client(Ec2Model.type)
        except Exception as ex:
            print('BotoError (AWS SDK) > %s' % ex.args[0])
            raise

        caller_identity  = sts.get_caller_identity()

        filters = []
        if tag_name is not None:
            filters.append({
                'Name': 'tag:%s' % tag_name,
                'Values': tag_values
            })
        describe_instances = client.describe_instances(Filters=filters, MaxResults=100)
       
        instances: List[Ec2Model] = list()
        reservations = describe_instances['Reservations']
        for reservation in reservations:
            for inst in reservation['Instances']:
                res = Ec2Model(
                    account = caller_identity.get('Account'),
                    region = session.region_name,
                    id = inst.get('InstanceId'),
                    public_ip = inst.get('PublicIpAddress'),
                    private_ip = inst.get('PrivateIpAddress'),
                    tags = inst.get('Tags')
                )

                # resource name
                for tag in res.tags:
                    if tag['Key'] == 'Name':
                        res.name = tag['Value']
                        break
                
                # guess ports from inbound security groups
                if check_security_groups:
                    security_groups = inst.get('SecurityGroups')
                    listeners = []
                    for security_group in security_groups:
                        sg_details = client.describe_security_groups(GroupIds=[security_group['GroupId']])
                        for sg_detail in sg_details.get('SecurityGroups'):
                            inbound_rules = sg_detail.get('IpPermissions')
                            if inbound_rules:
                                for inbound_rule in inbound_rules:
                                    listeners.append({
                                        'port': inbound_rule.get("FromPort"), 
                                        'protocol': inbound_rule.get("IpProtocol")
                                    })
                    
                    valid_ports = []
                    for listener in listeners:
                        if listener['port'] and listener['port'] > 0:
                            valid_ports.append(f'{listener["port"]}/{listener["protocol"]}')
                    
                    res.ports = ','.join(valid_ports)

                instances.append(res)

        return instances



if __name__ == '__main__':
    ec2 = Ec2Controller()
    my_instances = ec2.list('banyan:discovery', ['true'], True)
    print(my_instances)
