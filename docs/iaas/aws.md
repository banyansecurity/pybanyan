# AWS

Banyan uses the [AWS SDK for Python](https://github.com/boto/boto3) to synchronize AWS resources into Banyan's inventory.

## Credentials

Create an [IAM User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) for programmatic access.

Assign the following built-in permissions for your IAM User:
- AmazonEC2ReadOnlyAccess
- AmazonRDSReadOnlyAccess
- ElasticLoadBalancingReadOnly

Add an access key for your IAM User and get the credentials.

Add a section named `iaas-aws` in the `~/.banyan.conf` file with your IAM User credentials:
```ini
[banyan]
api_url = ...
refresh_token = ...

[iaas-aws]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
```

## Try it

Run the test command to verify access:

```
banyan cloud-resource test-aws
```
