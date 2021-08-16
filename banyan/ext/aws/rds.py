from typing import List, ClassVar, Type, Optional, Union
from dataclasses import dataclass

try:
    import boto3
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise


@dataclass
class RdsModel:
    class Meta:
        help = "AWS RDS Model"

    region: str
    id: str
    public_dns_name: str
    ports: str
    account: str
    tags: List
    public_ip: str = ''
    private_ip: str = ''
    status: str = 'discovered'
    private_dns_name: str = ''
    parent_id: str = ''
    cloud_provider: str = 'AWS'
    type: str = 'rds'
    name: str = ''


class RdsController():
    """
    Sync Rds
    Args:
        ResourceBase ([type]): [description]
    Returns:
        [type]: [description]
    """

    class Meta:
        help = "AWS RDS Controller"

    @property
    def resource_type(self) -> str:
        """
        Returns resource type.
        """
        return "RDS"

    # TODO: support more filters - region, vpc, owner
    def list(self, tag_name: str = None, tag_values: list = ['*']):
        try:
            session = boto3.session.Session()
            # todo: pshetty hardcoded region for testing
            client = session.client(RdsModel.type, region_name='us-east-2')
            user_profile = session.client('sts').get_caller_identity()
        except Exception as ex:
            print('BotoError (AWS SDK) > %s' % ex.args[0])
            raise

        filters = []
        # if tag_name is not None:
        #     filters.append({
        #         'Name': 'tag:%s' % tag_name,
        #         'Values': tag_values
        #     })
        response = client.describe_db_instances(Filters=filters, MaxRecords=100)
        #print("response", response)
        instances: List[RdsModel] = list()
        for index in range(len(response.get('DBInstances'))):
            rds_model = RdsModel(
                id=response.get('DBInstances')[index].get('DBInstanceArn'),
                name=response.get('DBInstances')[index].get('DBInstanceIdentifier'),
                public_dns_name=response.get('DBInstances')[index].get('Endpoint').get('Address'),
                ports=response.get('DBInstances')[index].get('Endpoint').get('Port'),
                region=response.get('DBInstances')[index].get('AvailabilityZone'),
                tags=response.get('DBInstances')[index].get('TagList'),
                account=user_profile.get('Account')
            )
            instances.append(rds_model)
        #print("instances", instances)
        return instances


if __name__ == '__main__':
    rds = RdsController()
    my_instances = rds.list('banyan:discovery', ['true'])
    print(my_instances)
