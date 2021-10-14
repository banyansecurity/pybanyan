# IaaS

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

---

### Adding a new IaaS Provider

1. Python SDK - if the provider has a Python SDK use it. Else, roll your own.
2. Authentication -use the default authentication mechanism, with credentials issued at the **Master** level
3. Hierarchy - add a column above with the provider's resource hierarchy
4. Discovery - implement it!