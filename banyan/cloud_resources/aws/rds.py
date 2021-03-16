#!/usr/bin/env python
import json
import botocore
from .base import ResourceBase
from banyan.bcolors import bcolors


class Rds(ResourceBase):
    """
    Sync Rds
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
        return "RDS"

    def sync(self, region=None):
        """
        Sync RDS to Banayan Inventory
        Args:
            region ([type], optional): [description]. Defaults to None.
        """
        list_of_regions = []
        if not region:
            available_regions = self.boto_session.get_available_regions('rds')
            for reg in available_regions:
                list_of_regions.append(reg)
        else:
            list_of_regions.append(region)

        list_of_rds = []

        print("...............\t Sync RDS has been started\t.....................")
        for ereg in list_of_regions:
            try:
                client = self.boto_session.client(
                    service_name="rds", region_name=ereg)
                print(
                    f"**********\t Sync RDS instances for Region {ereg} \t****************")
                instances = client.describe_db_instances()
                for index in range(len(instances.get('DBInstances'))):
                    listeners = []
                    tags = instances.get('DBInstances')[index].get('TagList')
                    coverted_tags = self.addAccountTags()
                    if len(tags) > 0:
                        for tag in tags:
                            coverted_tags.append(
                                {'name': tag['Key'], 'value': tag['Value']})
                    listeners.append(
                        {'port': instances.get('DBInstances')[index].get('Endpoint').get('Port'), 'protocol': 'tcp'})
                    coverted_tags.append(
                        {'name': 'security.listeners', 'value': json.dumps(listeners)})
                    list_of_rds.append({
                        'resource_id': instances.get('DBInstances')[index].get('DBInstanceArn'),
                        'resource_name': instances.get('DBInstances')[index].get('DBInstanceIdentifier'),
                        'resource_type': self.resource_type,
                        'public_dns_name': instances.get('DBInstances')[index].get('Endpoint').get('Address'),
                        'status': instances.get('DBInstances')[index].get('DBInstanceStatus'),
                        'private_dns_name': None,
                        'public_ip': None,
                        'private_ip': None,
                        'parent_id': None,
                        'service_id': None,
                        'region': ereg,
                        'cloud_provider': 'AWS',
                        'tags': coverted_tags,
                    })
            except botocore.exceptions.ClientError as exception:
                print(bcolors.FAIL +
                      f"Unable to sync RDS. {exception}" + bcolors.ENDC)

        # print(list_of_rds)
        responses = []
        for rds_instance in list_of_rds:
            response = self.client.inventory.create(rds_instance)
            responses.append(response)
            if not response:
                print(
                    bcolors.FAIL + f" \U0001F61E error creating RDS inventory. Id {rds_instance['resource_id']}" + bcolors.ENDC)
            else:
                print(bcolors.OKGREEN +
                      f" \u2713 RDS instance has been added to inventory. Id {rds_instance['resource_id']}" + bcolors.ENDC)
        return responses
