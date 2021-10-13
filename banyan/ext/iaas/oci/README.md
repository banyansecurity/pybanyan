# Oracle Cloud Infra

Ensure you have the [OCI Python SDK](https://github.com/oracle/oci-python-sdk) installed and configured.

```bash
pip install -r requirements.txt
```

## Configuration

Set up credentials (in ~/.oci/config):
```
[DEFAULT]
user=ocid1.user.oc1..<unique_ID>
fingerprint=<your_fingerprint>
key_file=~/.oci/oci_api_key.pem
tenancy=ocid1.tenancy.oc1..<unique_ID>
region=us-ashburn-1
``` 

Other credentials configuration methods are available. See the OCI docs for details.

## Test

Confirm you are set up correctly, by running:

```bash
python main.py
```

You should see a list of your OCI VM resources.


---

https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#Required_Keys_and_OCIDs
https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/core/models/oci.core.models.Instance.html#oci.core.models.Instance
https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/core/models/oci.core.models.Vnic.html
https://github.com/oracle/oci-python-sdk/blob/master/examples/get_all_instance_ip_addresses_and_dns_info.py