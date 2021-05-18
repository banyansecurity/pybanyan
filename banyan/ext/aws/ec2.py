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

    region: str
    id: str
    public_ip: str
    private_ip: str
    tags: List
    cloud_provider: str = 'AWS'
    type: str = 'ec2'
    name: str = ''


class Ec2Controller:
    class Meta:
        help = "AWS EC2 Controller"

    #TODO: support more filters - region, vpc, owner
    def list(self, tag_name: str = None, tag_values: list = ['*']):
        try:
            session = boto3.session.Session()
            client = session.client(Ec2Model.type)
        except Exception as ex:
            print('BotoError (AWS SDK) > %s' % ex.args[0])
            raise

        filters = []
        if tag_name is not None:
            filters.append({
                'Name': 'tag:%s' % tag_name,
                'Values': tag_values
            })
        response = client.describe_instances(Filters=filters, MaxResults=100)
       
        instances: List[Ec2Model] = list()
        reservations = response['Reservations']
        for reservation in reservations:
            for inst in reservation['Instances']:
                res = Ec2Model(
                    session.region_name,
                    inst.get('InstanceId'),
                    inst.get('PublicIpAddress'),
                    inst.get('PrivateIpAddress'),
                    inst.get('Tags')
                )
                for tag in res.tags:
                    if tag['Key'] == 'Name':
                        res.resource_name = tag['Value']
                        break
                instances.append(res)

        return instances



if __name__ == '__main__':
    ec2 = Ec2Controller()
    my_instances = ec2.list('banyan:discovery', ['true'])
    print(my_instances)
