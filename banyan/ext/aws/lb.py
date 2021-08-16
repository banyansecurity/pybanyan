from typing import List, ClassVar, Type, Optional, Union
from dataclasses import dataclass

try:
    import boto3
except ImportError as ex:
    print('ImportError > %s' % ex.args[0])
    raise


@dataclass
class LBModel:
    class Meta:
        help = "AWS LB Model"

    region: str
    id: str
    public_dns_name: str
    tags: List
    ports: str = ''
    account: str = ''
    status: str = 'discovered'
    private_dns_name: str = ''
    parent_id: str = ''
    cloud_provider: str = 'AWS'
    type: str = 'lb'
    public_ip: str = ''
    private_ip: str = ''
    name: str = ''


class LBController():
    """
    Sync Rds
    Args:
        ResourceBase ([type]): [description]
    Returns:
        [type]: [description]
    """

    class Meta:
        help = "AWS LB Controller"

    @property
    def resource_type(self) -> str:
        """
        Returns resource type.
        """
        return "lb"

    # TODO: support more filters - region, vpc, owner
    def list(self, tag_name: str = None, tag_values: list = ['*']):
        try:
            session = boto3.session.Session()
            # TODO: pshetty hardcoded region for testing
            client = session.client('elbv2', region_name='us-east-2')
            user_profile = session.client('sts').get_caller_identity()
        except Exception as ex:
            print('BotoError (AWS SDK) > %s' % ex.args[0])
            raise

        filters = []
        if tag_name is not None:
            filters.append({
                'Name': 'tag:%s' % tag_name,
                'Values': tag_values
            })
        response = client.describe_load_balancers(PageSize=100)
        # print("response", response)
        instances: List[LBModel] = list()
        for index in range(len(response.get('LoadBalancers'))):
            tags = []
            tag_response = client.describe_tags(
                ResourceArns=[response.get('LoadBalancers')[index].get('LoadBalancerArn'), ])
            for tag_desc in tag_response['TagDescriptions']:
                tags = tag_desc['Tags']
            listeners = []
            listeners_response = client.describe_listeners(
                LoadBalancerArn=response.get('LoadBalancers')[index].get('LoadBalancerArn'))
            for listener in listeners_response['Listeners']:
                listeners.append(
                    {'port': listener['Port'], 'protocol': listener['Protocol']})

            lb_model = LBModel(
                id=response.get('LoadBalancers')[index].get('LoadBalancerArn'),
                name=response.get('LoadBalancers')[index].get('LoadBalancerName'),
                public_dns_name=response.get('LoadBalancers')[index].get('DNSName'),
                ports='',
                account=user_profile.get('Account'),
                region='us-east-2',
                tags=tags
            )
            lb_model.ports = ','.join(str(listner['port']) for listner in listeners if listner['port'] is not None)
            instances.append(lb_model)

        # classic ELB (application load balancers)
        classic_elb_list = session.client(
            'elb', region_name='us-east-2')
        classic_lb = classic_elb_list.describe_load_balancers()
        for lb_desc in classic_lb['LoadBalancerDescriptions']:
            listeners = []
            for listener in lb_desc['ListenerDescriptions']:
                listeners.append(
                    {'port': listener['Listener']['LoadBalancerPort'], 'protocol': listener['Listener']['Protocol']})
            tags = []
            tag_response = classic_elb_list.describe_tags(
                LoadBalancerNames=[lb_desc['LoadBalancerName'], ])
            for tag_desc in tag_response['TagDescriptions']:
                tags = tag_desc['Tags']

            classic_lb_model = LBModel(
                id=lb_desc['LoadBalancerName'],
                name=lb_desc['LoadBalancerName'],
                public_dns_name=lb_desc['DNSName'],
                ports='',
                account=user_profile.get('Account'),
                region='us-east-2',
                tags=tags
            )
            classic_lb_model.ports = ','.join(str(listner['port'])
                                              for listner in listeners if listner['port'] is not None)
            instances.append(classic_lb_model)
        return instances


if __name__ == '__main__':
    lb = LBController()
    my_instances = lb.list('banyan:discovery', ['true'])
    print(my_instances)
