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