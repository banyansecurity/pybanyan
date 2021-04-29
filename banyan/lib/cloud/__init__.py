from abc import ABC


has_aws = True
try:
    import boto3
except ImportError:
    has_aws = False


has_cloud = has_aws


def get_cloud_vendor() -> str:
    with open('/sys/devices/virtual/dmi/id/board_vendor', 'r') as f:
        vendor = f.read()
        if 'Amazon' in vendor:
            return 'aws'
        elif 'Google' in vendor:
            return 'gcp'
        elif 'Microsoft' in vendor:
            return 'azure'
        else:
            raise RuntimeError(f'unknown cloud vendor: {vendor}')


class CloudVendor(ABC):
    def get_public_dns_name(self) -> str:
        pass
