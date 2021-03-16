#!/usr/bin/env python
import json
import logging
import boto3
from banyan.bcolors import bcolors
from .base import ResourceBase


class Ec2(ResourceBase):
    """
    Sync Ec2 instances

    Args:
        ResourceBase ([type]): [description]

    Raises:
        AttributeError: [description]

    Returns:
        [type]: [description]
    """

    @property
    def resource_type(self) -> str:
        """
        Returns resource type.
        """
        return "EC2"

    def sync(self, region=None):
        try:
            client = self.boto_session.client(service_name="ec2")
            list_of_regions = []
            if not region:
                all_regions = client.describe_regions()
                for reg in all_regions['Regions']:
                    list_of_regions.append(reg['RegionName'])
            else:
                list_of_regions.append(region)

            responses = []
            for ereg in list_of_regions:
                print(
                    f"**********\t Sync EC2 instances for Region {ereg} \t****************")
                reg_resource = self.boto_session.resource(
                    region_name=ereg, service_name="ec2")
                for instance in reg_resource.instances.all():
                    tag_name = None if instance.tags is None else [tag['Value']
                                                                   for tag in instance.tags if tag['Key'] == 'Name']
                    ec2_name = None if tag_name is None else tag_name[0] if len(
                        tag_name) > 0 else None

                    coverted_tags = self.addAccountTags()
                    if instance.tags:
                        for tag in instance.tags:
                            coverted_tags.append(
                                {'name': tag['Key'], 'value': tag['Value']})

                    sgs = instance.security_groups
                    sgs_rules = []
                    listeners = []
                    for sg in sgs:
                        sg_details = reg_resource.SecurityGroup(
                            sg['GroupId'])
                        # InBound permissions ##########################################
                        inbound = sg_details.ip_permissions
                        outbound = sg_details.ip_permissions_egress
                        sgs_rules.append({
                            'GroupName': sg["GroupName"],
                            'GroupId': sg["GroupId"],
                            'Inbound': inbound,
                            'Outbound': outbound
                        })
                        for inbound_rule in inbound:
                            listeners.append(
                                {'port': inbound_rule.get("FromPort"), 'protocol': inbound_rule.get("IpProtocol")})
                    coverted_tags.append(
                        {'name': 'security.rules', 'value': json.dumps(sgs_rules)})
                    coverted_tags.append(
                        {'name': 'security.listeners', 'value': json.dumps(listeners)})
                    ec2 = {
                        'resource_id': instance.id,
                        'resource_name': ec2_name,
                        'resource_type': self.resource_type,
                        'parent_id': None,
                        'public_dns_name': instance.public_dns_name,
                        'private_dns_name': instance.private_dns_name,
                        'public_ip': instance.public_ip_address,
                        'private_ip': instance.private_ip_address,
                        'region': ereg,
                        'service_id': "",
                        'status': 'new',
                        'cloud_provider': 'AWS',
                        'tags': coverted_tags,
                    }
                    response = self.client.inventory.create(ec2)
                    responses.append(response)
                    if not response:
                        print(
                            bcolors.FAIL + f" \U0001F61E error creating loadbalancer inventory. Id {ec2['resource_id']}" + bcolors.ENDC)
                    else:
                        logging.debug(
                            "EC2 instance has been added to inventory. Id %s", ec2['resource_id'])
                        print(bcolors.OKGREEN +
                              f"  \u2713  EC2 instance has been added to inventory. Id {ec2['resource_id']}" + bcolors.ENDC)
            return responses
        except Exception as err:  # pylint: disable=broad-except
            print("Unable to sync EC2 instances.", err)

    def get_tag(self, ec2, id):
        instance = ec2.Instance(id)
        return instance.tags[0]['Value']

    def get_details(self, instance_id, region_name):
        if self.config["debug"]:
            print(
                f'Instance region: {region_name}')
            print(f'Getting details for instance: {instance_id}')

        ec2 = boto3.resource('ec2', region_name=region_name)
        instance = ec2.Instance(instance_id)
        details = self.__get_instace_details(ec2, instance)
        return details

    def __get_instace_details(self, ec2, ec2_instace):
        print(dir(ec2_instace))
        if ec2_instace is None:
            raise AttributeError('ec2_instace is missing')

        sgs = ec2_instace.security_groups
        sgs_rules = []
        for sg in sgs:
            sg_details = ec2.SecurityGroup(sg['GroupId'])
            # InBound permissions ##########################################
            inbound = sg_details.ip_permissions
            outbound = sg_details.ip_permissions_egress
            sgs_rules.append({
                'GroupName': sg["GroupName"],
                'GroupId': sg["GroupId"],
                'Inbound': inbound,
                'Outbound': outbound
            })

        devices = []
        for _, dev in enumerate(ec2_instace.block_device_mappings, start=1):
            devices.append({
                'DeviceName': dev['DeviceName'],
                'VolumeId': dev['Ebs']['VolumeId'],
                'Status': dev['Ebs']['Status'],
                'DeleteOnTermination': dev['Ebs']['DeleteOnTermination'],
                'AttachTime': dev['Ebs']['AttachTime']
            })

        tags = []
        if ec2_instace.tags:
            for _, tag in enumerate(ec2_instace.tags, start=1):
                tags.append({
                    'Key': tag['Key'],
                    'Value': tag['Value']
                })

        products = []
        for _, product in enumerate(ec2_instace.product_codes, start=1):
            products.append({
                'ProductCodeId': product['ProductCodeId'],
                'ProductCodeType': product['ProductCodeType']
            })

        details = {
            'Details': {
                'Id': ec2_instace.id,
                'State': ec2_instace.state['Name'],
                'Launched': ec2_instace.launch_time,
                'RootDeviceName': ec2_instace.root_device_name,
                'Arch': ec2_instace.architecture,
                'Hypervisor': ec2_instace.hypervisor,
                'PrivateIp': ec2_instace.private_ip_address,
                'PublicIp': ec2_instace.public_ip_address,
                'PrivateDns': ec2_instace.private_dns_name,
                'PublicDns': ec2_instace.public_dns_name,
                'SubnetId': ec2_instace.subnet_id,
                'KernelId': ec2_instace.kernel_id,
                'InstanceType': ec2_instace.instance_type,
                'RamDiskId': ec2_instace.ramdisk_id,
                'AMIId': ec2_instace.image_id,
                'Platform': ec2_instace.platform,
                'EBSOptimized': 'Yes' if ec2_instace.ebs_optimized else 'No',
                'VPCId': ec2_instace.vpc_id,
                'VirtualizationType': ec2_instace.virtualization_type,

            },
            'CpuOptions': {
                'CoreCount': ec2_instace.cpu_options['CoreCount'],
                'ThreadsPerCore': ec2_instace.cpu_options['ThreadsPerCore']
            },
            'Products': products,
            'Devices': devices,
            'Tags': tags,
            'SecurityRules': sgs_rules,
        }
        return details
