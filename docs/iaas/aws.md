# AWS

Banyan uses the [AWS SDK for Python](https://github.com/boto/boto3) to synchronize AWS resources into Banyan's inventory.

If you installed `pybanyan` using `pip`, get the AWS extra:
```console
$ pip install pybanyan[aws]
```

## Authentication

Create an [IAM User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) for programmatic access.

Assign the following built-in permissions for your IAM User:
- AmazonEC2ReadOnlyAccess
- AmazonRDSReadOnlyAccess
- ElasticLoadBalancingReadOnly

Add an access key for your IAM User and get the credentials.

Add a section named `aws` in the `~/.banyan.conf` file with your IAM User credentials:
```ini
[banyan]
api_url = ...
refresh_token = ...

[aws]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
```

## TODO: Multiple Accounts

You can discover resources across multiple accounts that belong to the same AWS organization. This capability hasn't been implemented yet.


## Test

Run the test command to verify access:

```
banyan cloud-resource test-aws
```

## Synchronize

Run the sync command to synchronize your Iaas resources:

```bash
banyan cloud-resource sync-aws
```