# AWS

## 1. Python SDK

Install the [AWS SDK for Python](https://github.com/boto/boto3):

```bash
pip install -r requirements.txt
```

## 2. Credentials

Create an [IAM User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) for programmatic access.

Assign the following built-in permissions for your IAM User:
- AmazonEC2ReadOnlyAccess
- AmazonRDSReadOnlyAccess
- ElasticLoadBalancingReadOnly

Add an access key for your IAM User and get the credentials.

Add a section named `iaas-aws` in the `~/.banyan.conf` file with these credentials:
```ini
[banyan]
api_url = ...
refresh_token = ...

[iaas-aws]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
```

## 3. Test

Confirm you are set up correctly by running:

```bash
python main.py
```

You should see a list of your AWS EC2, ELB and RDS resources.

---

## Development Notes

1. You can set up AWS organizations and assume Roles into Member Accounts

```
response = client.assume_role(RoleArn=arn, RoleSessionName=session_name)
```

2. You can check boto3 Resource models via:

```
shape = instance.meta.client.meta.service_model.shape_for('Instance')
print(instance.meta.resource_model.get_attributes(shape))
```

