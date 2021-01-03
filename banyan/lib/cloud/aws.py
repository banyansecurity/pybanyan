import boto3
from ec2_metadata import ec2_metadata


class AwsCloud:
    def __init__(self):
        self._elb = boto3.client('elbv2')
        self._instance_id = ec2_metadata.instance_id

    def _has_banyanops_tag(self, elb_arn: str) -> bool:
        response = self._elb.describe_tags(ResourceArns=[elb_arn])
        assert ('TagDescriptions' in response)
        for tag_desc in response['TagDescriptions']:
            for tag in tag_desc['Tags']:
                if tag['Key'] == 'Provider' and tag['Value'] == 'BanyanOps':
                    return True
        return False

    def _get_target_group_443_arn(self, elb_arn: str) -> str:
        response = self._elb.describe_target_groups(LoadBalancerArn=elb_arn)
        assert ('TargetGroups' in response)
        for tg in response['TargetGroups']:
            if tg['Port'] == 443:
                return tg['TargetGroupArn']
        raise ValueError(f'ELB with ARN {elb_arn} does not have a target group on :443')

    # noinspection PyMethodMayBeStatic
    def _is_healthy_nlb(self, elb: dict) -> bool:
        return elb['Type'] == 'network' and elb['Scheme'] == 'internet-facing' and elb['State']['Code'] == 'active'

    def _am_i_a_target(self, tg_arn: str, instance_id: str) -> bool:
        response = self._elb.describe_target_health(TargetGroupArn=tg_arn)
        assert ('TargetHealthDescriptions' in response)
        for tg_health in response['TargetHealthDescriptions']:
            target_id = tg_health['Target']['Id']
            if target_id == instance_id:
                return True
        return False

    def get_public_dns_name(self) -> str:
        response = self._elb.describe_load_balancers()
        assert ('LoadBalancers' in response)
        for elb in response['LoadBalancers']:
            elb_arn = elb['LoadBalancerArn']
            elb_dns_name = elb['DNSName']
            if not self._is_healthy_nlb(elb):
                continue
            tg_arn = self._get_target_group_443_arn(elb_arn)
            if not self._am_i_a_target(tg_arn, self._instance_id):
                continue
            return elb_dns_name
        raise RuntimeError(f'could not find a public NLB for instance-id {self._instance_id}')
