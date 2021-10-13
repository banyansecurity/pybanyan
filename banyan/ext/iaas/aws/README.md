# AWS

Ensure you have the [AWS SDK for Python](https://github.com/boto/boto3) installed and configured.

```bash
pip install -r requirements.txt
```

## Configuration

Set up credentials (in ~/.aws/credentials):
```ini
[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
```

Set up a default region (in ~/.aws/config):
```
[default]
region=us-east-1
```

Other credentials configuration methods are available. See the AWS docs for details.

## Test

Confirm you are set up correctly, by running:

```bash
python main.py
```

You should see a list of your AWS EC2, ELB and RDS resources.


---

EC2 Model
```python
shape = instance.meta.client.meta.service_model.shape_for('Instance')
print(instance.meta.resource_model.get_attributes(shape))
```

```
{
    'ami_launch_index': ('AmiLaunchIndex', <Shape(Integer)>),
    'image_id': ('ImageId', <StringShape(String)>),
    'instance_id': ('InstanceId', <StringShape(String)>),
    'instance_type': ('InstanceType', <StringShape(InstanceType)>),
    'kernel_id': ('KernelId', <StringShape(String)>),
    'key_name': ('KeyName', <StringShape(String)>),
    'launch_time': ('LaunchTime', <Shape(DateTime)>),
    'monitoring': ('Monitoring', <StructureShape(Monitoring)>),
    'placement': ('Placement', <StructureShape(Placement)>),
    'platform': ('Platform', <StringShape(PlatformValues)>),
    'private_dns_name': ('PrivateDnsName', <StringShape(String)>),
    'private_ip_address': ('PrivateIpAddress', <StringShape(String)>),
    'product_codes': ('ProductCodes', <ListShape(ProductCodeList)>),
    'public_dns_name': ('PublicDnsName', <StringShape(String)>),
    'public_ip_address': ('PublicIpAddress', <StringShape(String)>),
    'ramdisk_id': ('RamdiskId', <StringShape(String)>),
    'state': ('State', <StructureShape(InstanceState)>),
    'state_transition_reason': ('StateTransitionReason', <StringShape(String)>),
    'subnet_id': ('SubnetId', <StringShape(String)>),
    'vpc_id': ('VpcId', <StringShape(String)>),
    'architecture': ('Architecture', <StringShape(ArchitectureValues)>),
    'block_device_mappings': ('BlockDeviceMappings', <ListShape(InstanceBlockDeviceMappingList)>),
    'client_token': ('ClientToken', <StringShape(String)>),
    'ebs_optimized': ('EbsOptimized', <Shape(Boolean)>),
    'ena_support': ('EnaSupport', <Shape(Boolean)>),
    'hypervisor': ('Hypervisor', <StringShape(HypervisorType)>),
    'iam_instance_profile': ('IamInstanceProfile', <StructureShape(IamInstanceProfile)>),
    'instance_lifecycle': ('InstanceLifecycle', <StringShape(InstanceLifecycleType)>),
    'elastic_gpu_associations': ('ElasticGpuAssociations', <ListShape(ElasticGpuAssociationList)>),
    'elastic_inference_accelerator_associations': ('ElasticInferenceAcceleratorAssociations', <ListShape(ElasticInferenceAcceleratorAssociationList)>),
    'network_interfaces_attribute': ('NetworkInterfaces', <ListShape(InstanceNetworkInterfaceList)>),
    'outpost_arn': ('OutpostArn', <StringShape(String)>),
    'root_device_name': ('RootDeviceName', <StringShape(String)>),
    'root_device_type': ('RootDeviceType', <StringShape(DeviceType)>),
    'security_groups': ('SecurityGroups', <ListShape(GroupIdentifierList)>),
    'source_dest_check': ('SourceDestCheck', <Shape(Boolean)>),
    'spot_instance_request_id': ('SpotInstanceRequestId', <StringShape(String)>),
    'sriov_net_support': ('SriovNetSupport', <StringShape(String)>),
    'state_reason': ('StateReason', <StructureShape(StateReason)>),
    'tags': ('Tags', <ListShape(TagList)>),
    'virtualization_type': ('VirtualizationType', <StringShape(VirtualizationType)>),
    'cpu_options': ('CpuOptions', <StructureShape(CpuOptions)>),
    'capacity_reservation_id': ('CapacityReservationId', <StringShape(String)>),
    'capacity_reservation_specification': ('CapacityReservationSpecification', <StructureShape(CapacityReservationSpecificationResponse)>),
    'hibernation_options': ('HibernationOptions', <StructureShape(HibernationOptions)>),
    'licenses': ('Licenses', <ListShape(LicenseList)>),
    'metadata_options': ('MetadataOptions', <StructureShape(InstanceMetadataOptionsResponse)>),
    'enclave_options': ('EnclaveOptions', <StructureShape(EnclaveOptions)>),
    'boot_mode': ('BootMode', <StringShape(BootModeValues)>)
}
```