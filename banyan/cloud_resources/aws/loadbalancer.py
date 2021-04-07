import json
from .base import ResourceBase
from banyan.bcolors import bcolors


class Loadbalancer(ResourceBase):
    """
    Sync Loadbalancer, ALB, ELB and Classic

    Args:
        ResourceBase ([type]): [description]

    Returns:
        [type]: [description]
    """

    @property
    def resource_type(self) -> str:
        """
        Returns resource type.
        """
        return "LB"

    def sync(self, region=None):
        try:
            regions = []
            client = self.boto_session.client(service_name="ec2")
            ec2_regions = client.describe_regions()
            for _region in ec2_regions['Regions']:
                regions.append(_region['RegionName'])

            elb_resources = []
            for ec2_reg in regions:
                print(
                    f"**********\t Sync ELB for Region {ec2_reg} \t****************")
                elb_list = self.boto_session.client(
                    'elbv2', region_name=ec2_reg)
                # ec2 = session.resource('ec2', region_name=ec2_reg)
                lb = elb_list.describe_load_balancers()
                # print(lb)
                for lb_desc in lb['LoadBalancers']:
                    target_group = []
                    tags = []
                    instances = []

                    listeners = []
                    listenersResponse = elb_list.describe_listeners(
                        LoadBalancerArn=lb_desc['LoadBalancerArn'])
                    for listener in listenersResponse['Listeners']:
                        listeners.append(
                            {'port': listener['Port'], 'protocol': listener['Protocol']})

                    # target group
                    target_group_response = elb_list.describe_target_groups(
                        LoadBalancerArn=lb_desc['LoadBalancerArn'])

                    # todo: Persist Target Group details?
                    for target in target_group_response['TargetGroups']:
                        health_targets = []
                        health_response = elb_list.describe_target_health(
                            TargetGroupArn=target['TargetGroupArn'])
                        for health_target in health_response['TargetHealthDescriptions']:
                            health_targets.append(
                                health_target['Target'])

                        target_group.append({
                            'Arn': target['TargetGroupArn'],
                            'Name': target['TargetGroupName'],
                            'Protocol': target['Protocol'],
                            'Port': target['Port'],
                            'Instances': json.dumps(health_targets)
                        })
                        for ins in health_targets:
                            new_instance = {
                                'InstanceId': ins['Id']}
                            if new_instance not in instances:
                                instances.append(new_instance)

                    # print(target_group)
                    tag_response = elb_list.describe_tags(
                        ResourceArns=[lb_desc['LoadBalancerArn'], ])
                    for tag_desc in tag_response['TagDescriptions']:
                        tags = tag_desc['Tags']

                    coverted_tags = self.addAccountTags()
                    coverted_tags.append(
                        {'name': 'security.listeners', 'value': json.dumps(listeners)})
                    if tags:
                        for tag in tags:
                            coverted_tags.append(
                                {'name': tag['Key'], 'value': tag['Value']})

                    elb_resources.append({
                        'resource_id': lb_desc['LoadBalancerArn'],
                        'resource_name': lb_desc['LoadBalancerName'],
                        # lb_desc['Type'],
                        'resource_type': self.resource_type,
                        'parent_id': None,
                        'public_dns_name': lb_desc['DNSName'],
                        'private_dns_name': "",
                        'public_ip': "",
                        'private_ip': "",
                        'region': ec2_reg,
                        'service_id': "",
                        'status': 'new',
                        'cloud_provider': 'AWS',
                        'tags': coverted_tags,
                        'Instances': instances
                    })

                classic_elb_list = self.boto_session.client(
                    'elb', region_name=ec2_reg)
                classic_lb = classic_elb_list.describe_load_balancers()
                # print(classic_lb)
                for lb_desc in classic_lb['LoadBalancerDescriptions']:
                    # listeners
                    listeners = []
                    for listener in lb_desc['ListenerDescriptions']:
                        listeners.append(
                            {'port': listener['Listener']['LoadBalancerPort'], 'protocol': listener['Listener']['Protocol']})

                    tags = []
                    tag_response = classic_elb_list.describe_tags(
                        LoadBalancerNames=[lb_desc['LoadBalancerName'], ])
                    for tag_desc in tag_response['TagDescriptions']:
                        tags = tag_desc['Tags']

                    coverted_tags = self.addAccountTags()
                    coverted_tags.append(
                        {'name': 'security.listeners', 'value': json.dumps(listeners)})
                    if tags:
                        for tag in tags:
                            coverted_tags.append(
                                {'name': tag['Key'], 'value': tag['Value']})

                    elb_resources.append({
                        'resource_id': lb_desc['LoadBalancerName'],
                        'resource_name': lb_desc['LoadBalancerName'],
                        'resource_type': self.resource_type,
                        'parent_id': None,
                        'public_dns_name': lb_desc['DNSName'],
                        'private_dns_name': "",
                        'public_ip': "",
                        'private_ip': "",
                        'region': ec2_reg,
                        'service_id': "",
                        'status': 'new',
                        'cloud_provider': 'AWS',
                        'tags': coverted_tags,
                        'Instances': lb_desc['Instances']
                    })
            responses = []
            for load_balancer in elb_resources:
                response = self.client.inventory.create(load_balancer)
                responses.append(response)
                if not response:
                    print(
                        bcolors.FAIL + f" \U0001F61E Error creating loadbalancer inventory. Id {load_balancer['resource_id']}" + bcolors.ENDC)
                else:
                    print(bcolors.OKGREEN +
                          f" \u2713  Loadblancer instance has been added to inventory. Id {load_balancer['resource_id']}" + bcolors.ENDC)
            return responses
        except Exception as err:  # pylint: disable=broad-except
            print(bcolors.FAIL +
                  f"Unable to sync loadbalancer. {err}" + bcolors.ENDC)
