# Oracle Cloud Infra

## 1. Python SDK

Install the [OCI Python SDK](https://github.com/oracle/oci-python-sdk).

```bash
pip install -r requirements.txt
```

## 2. Credentials

Create an [IAM User](https://docs.oracle.com/en-us/iaas/Content/GSG/Tasks/addingusers.htm#Adding_Users).

Assign the user to a Group that is restricted to the following Policy statements: 
- Allow group Viewers to inspect all-resources in tenancy

Create an API key for this user, and download your configuration file.

Add a section named `iaas-oci` in the `~/.banyan.conf` file with these configurations:
```ini
[banyan]
api_url = ...
refresh_token = ...

[iaas-oci]
user=ocid1.user.oc1..<unique_ID>
fingerprint=<your_fingerprint>
key_file=/path/to/oci_api_key.pem
tenancy=ocid1.tenancy.oc1..<unique_ID>
region=us-ashburn-1
```

Note that if you're on Windows, use `/` not `\` in the path here, so you'd use `C:/Users/foobar/key.json` and not `C:\Users\foobar\key.json`.

## 3. Test

Confirm you are set up correctly, by running:

```bash
python main.py
```

You should see a list of your OCI VM resources.


---

## Development Notes

https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#Required_Keys_and_OCIDs
https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/core/models/oci.core.models.Instance.html#oci.core.models.Instance
https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/core/models/oci.core.models.Vnic.html
https://github.com/oracle/oci-python-sdk/blob/master/examples/get_all_instance_ip_addresses_and_dns_info.py