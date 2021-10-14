# Synchronize IaaS Resources

Banyan uses IaaS (Infrastructure As A Service) providers' Python SDK to synchronize IaaS resources into Banyan's inventory. 

IaaS providers have different **resource hierarchies** to group resources inside an IaaS account. To discover resources across multiple IaaS providers consistently, we create our own "meta" resource hierarchy model as follows:

| Hierarchy              | AWS                | Azure               | GCP           | VMware            | OCI           |
| --------      		 | --- 		 	      | -----				| ---			| ------		    | ---			|
| **Billing** level      | Org, Org Unit      | Root, Mgmt Group    | -             | -		            | -		        |
| **Owner** level        | (Account)          | Subscription        | Org           | Vsphere   	    | Tenant        | 
| **Account** level      | Account            | Resource Groups     | Projects      | Datacenters       | Compartments  |
| **Region**			 | Regions		      | Locations			| Zones			| -				    | Regions		|
| **Instance**           | EC2, RDS, etc      | VM, LB, etc         | VM, LB, etc   | VM                | VM, DB, etc   |


IaaS providers also have different **tagging mechanisms** to organize resources inside an IaaS account. 

| Tagging Scheme         | AWS            | Azure               | GCP           | VMware            | OCI           |
| --------------         | --- 		 	  | -----				| ---			| ------		    | ---			|
| **Tags**               | Tags           | Tags                | Labels        | Tags, Categories  | Tags          |


Now, we can generalize our discovery implementation for the various IaaS providers:

1. **Billing** levels are ignored entirely
2. SDK credentials are issued at the **Owner** level
3. Discovery filters are implemented for **Account** level, **Region** and **Tags**
4. **Instances** public and private network addresses are recorded

---

## Development Nodes

### Adding a new IaaS Provider

1. Python SDK - if the provider has a Python SDK use it. Else, roll your own.
2. Authentication - use the default authentication mechanism, with credentials issued at the **Owner** level
3. Hierarchy - add a column above with the provider's resource hierarchy
4. Discovery - implement it!

### AWS 

1. You can set up AWS organizations and assume Roles into Member Accounts

```
response = client.assume_role(RoleArn=arn, RoleSessionName=session_name)
```

2. You can check boto3 Resource models via:

```
shape = instance.meta.client.meta.service_model.shape_for('Instance')
print(instance.meta.resource_model.get_attributes(shape))
```

## Azure

1. The `az ad sp create-for-rbac --name localtest-sp-rbac --skip-assignment` command generates JSON output similar to the following values.

  {
    "appId": "12345678-1111-2222-3333-1234567890ab",
    "displayName": "localtest-sp-rbac",
    "name": "http://localtest-sp-rbac",
    "password": "abcdef00-4444-5555-6666-1234567890ab",
    "tenant": "00112233-7777-8888-9999-aabbccddeeff"
  }
  
In this output, `tenant` is the `tenant_id`, `appId` is the `client_id`, and password is the `client_secret`.

2. To retrieve your subscription ID, run the `az account show` command and look for the id property in the output.


## GCP

1. Python models

https://github.com/alfonsof/google-cloud-python-examples/blob/master/gcloudcomputeengine/computeenginehelper.py
https://googleapis.github.io/google-api-python-client/docs/epy/index.html
https://googleapis.github.io/google-api-python-client/docs/dyn/compute_v1.instances.html#aggregatedList


### OCI

1. Concepts

https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm#Required_Keys_and_OCIDs
https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/core/models/oci.core.models.Instance.html#oci.core.models.Instance
https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/core/models/oci.core.models.Vnic.html
https://github.com/oracle/oci-python-sdk/blob/master/examples/get_all_instance_ip_addresses_and_dns_info.py