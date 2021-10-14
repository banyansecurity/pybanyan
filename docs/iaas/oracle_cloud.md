# Oracle Cloud Infra

Banyan uses the [OCI Python SDK](https://github.com/oracle/oci-python-sdk) to synchronize OCI resources into Banyan's inventory.

## Credentials

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

**Note:** if you're on Windows, Python still uses `/` not `\` in the path to key file, so you'd use `C:/Users/foobar/key.json` and not `C:\Users\foobar\key.json`.


## Try it

Run the test command to verify access:

```bash
banyan cloud-resource test-oci
```
