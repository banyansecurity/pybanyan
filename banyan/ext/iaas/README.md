# IaaS

Banyan uses IaaS (Infrastructure As A Service) providers' Python SDK to synchronize IaaS resources into Banyan's inventory. IaaS providers have different **resource hierarchies** to organize resources inside an IaaS account. To discover resources across multiple IaaS providers consistently, we create our own "meta" resource hierarchy model as follows:


| Hierarchy          	 | AWS            | Azure               | GCP           | VMware            | OCI           |
| --------- 		 	 | --- 		 	  | -----				| ---			| ------		    | ---			|
| **Management**         | Org, Org Unit  | Root, Mgmt Group    | Org, Folder   | -		            | -		        |
| **Account**            | Account        | Subscription        | Project       | Account   	    | Tenant        | 
| **Parent**             | -              | Resource Groups     | -             | Datacenters       | Containers    |
| **Location**			 | Regions		  | Locations			| Zones			| -				    | Regions		|
| **Tag**                | Tags           | Tags                | Labels        | Tags, Categories  | Tags          |
| **Instance**           | EC2, RDS, etc  | VM, LB, etc         | VM, LB, etc   | VM                | VM, DB, etc   |

With this model, we can generalize our discovery implementation for the various IaaS providers:

1. **Management** level(s) is ignored entirely
2. SDK credentials are issued at the **Account** level
3. Discovery filters are always implemented for **Location** and **Tag**
4. Discovery filters is implemented for the **Parent** level if it exists in the IaaS

---

### Adding a new IaaS Provider

1. Python SDK - if the provider has a Python SDK use it. Else, roll your own.
2. Authentication - ensure you work with the default authentication mechanism
3. Hierarchy - add a column above with the provider's resource hierarchy
4. Discovery - implement it!