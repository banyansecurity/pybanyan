<a name="__pageTop"></a>
# openapi_client.apis.tags.org_api.OrgApi

All URIs are relative to *https://dev02.console.bnntest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_add_org_post**](#v1_add_org_post) | **post** /v1/add_org |  POST /v1/add_org
[**v1_admin_add_user_post**](#v1_admin_add_user_post) | **post** /v1/admin/add_user |  POST /v1/admin/add_user
[**v1_admin_delete_user_delete**](#v1_admin_delete_user_delete) | **delete** /v1/admin/delete_user |  DELETE /v1/admin/delete_user
[**v1_admin_list_orgs_get**](#v1_admin_list_orgs_get) | **get** /v1/admin/list_orgs |  GET /v1/admin/list_orgs
[**v1_admin_list_users_get**](#v1_admin_list_users_get) | **get** /v1/admin/list_users |  This API lists all the users for that Org.
[**v1_admin_update_user_post**](#v1_admin_update_user_post) | **post** /v1/admin/update_user |  POST /v1/admin/update_user
[**v1_api_v1_admin_saml_get**](#v1_api_v1_admin_saml_get) | **get** /v1/api/v1/admin/saml |  Get the admin SAML Sign-on Settings for an organization
[**v1_api_v1_admin_setup_saml_post**](#v1_api_v1_admin_setup_saml_post) | **post** /v1/api/v1/admin/setup_saml |  Set the admin Sign-on settings for an organization
[**v1_api_v1_reset_password_post**](#v1_api_v1_reset_password_post) | **post** /v1/api/v1/reset_password | Reset Password for a banyan console user
[**v1_ca_certs_get**](#v1_ca_certs_get) | **get** /v1/ca_certs | fetch ca certificates for an org
[**v1_delete_org_delete**](#v1_delete_org_delete) | **delete** /v1/delete_org |  Delete Org
[**v1_delete_pwless_config_delete**](#v1_delete_pwless_config_delete) | **delete** /v1/delete_pwless_config |  Delete pwless config for an org
[**v1_insert_pwless_config_post**](#v1_insert_pwless_config_post) | **post** /v1/insert_pwless_config |  Create pwless config for an org
[**v1_org_details_get**](#v1_org_details_get) | **get** /v1/org_details |  Get org details
[**v1_org_status_get**](#v1_org_status_get) | **get** /v1/org_status |  Get org status
[**v1_update_org_post**](#v1_update_org_post) | **post** /v1/update_org |  Update Org
[**v1_user_org_details_get**](#v1_user_org_details_get) | **get** /v1/user_org_details |  Get user&#x27;s org details
[**v2_admin_client_certificate_get**](#v2_admin_client_certificate_get) | **get** /v2/admin/client_certificate |  GET client certificate details
[**v2_mom_org_get**](#v2_mom_org_get) | **get** /v2/mom/org |  Get list of all Orgs
[**v2_mom_org_org_id_get**](#v2_mom_org_org_id_get) | **get** /v2/mom/org/{org_id} |  Get Org by org id
[**v2_mom_org_post**](#v2_mom_org_post) | **post** /v2/mom/org | Create and provision a Org
[**v2_mom_org_put**](#v2_mom_org_put) | **put** /v2/mom/org | Create and provision a Org
[**v2_onboarding_state_post**](#v2_onboarding_state_post) | **post** /v2/onboarding_state |  Set org onboarding state

# **v1_add_org_post**
<a name="v1_add_org_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_add_org_post()

 POST /v1/add_org

This adds a new Org and and Owner for this org. A welcome email is sent to the Owner of the org.Authorization: SuperAdminHeaders: Standard

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    query_params = {
        'OrgName': "OrgName_example",
        'NoVPNStatus': "NoVPNStatus_example",
        'NonAccessIdentityEventRetentionDurationInHours': "NonAccessIdentityEventRetentionDurationInHours_example",
        'AccessEventRetentionDurationInHours': "AccessEventRetentionDurationInHours_example",
        'IdentityEventRetentionDurationInHours': "IdentityEventRetentionDurationInHours_example",
        'OwnerEmail': "OwnerEmail_example",
        'First': "First_example",
        'Last': "Last_example",
        'APIServerLocation': "APIServerLocation_example",
        'IsTunnelEnabled': "IsTunnelEnabled_example",
        'IsTestDrive': "IsTestDrive_example",
        'Edition': "Edition_example",
        'ZoneID': "ZoneID_example",
        'GlobalDomainDirectoryURL': "GlobalDomainDirectoryURL_example",
        'IsAutoRenewCertsEnabled': "IsAutoRenewCertsEnabled_example",
    }
    try:
        #  POST /v1/add_org
        api_response = api_instance.v1_add_org_post(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_add_org_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
OrgName | OrgNameSchema | | optional
NoVPNStatus | NoVPNStatusSchema | | optional
NonAccessIdentityEventRetentionDurationInHours | NonAccessIdentityEventRetentionDurationInHoursSchema | | optional
AccessEventRetentionDurationInHours | AccessEventRetentionDurationInHoursSchema | | optional
IdentityEventRetentionDurationInHours | IdentityEventRetentionDurationInHoursSchema | | optional
OwnerEmail | OwnerEmailSchema | | optional
First | FirstSchema | | optional
Last | LastSchema | | optional
APIServerLocation | APIServerLocationSchema | | optional
IsTunnelEnabled | IsTunnelEnabledSchema | | optional
IsTestDrive | IsTestDriveSchema | | optional
Edition | EditionSchema | | optional
ZoneID | ZoneIDSchema | | optional
GlobalDomainDirectoryURL | GlobalDomainDirectoryURLSchema | | optional
IsAutoRenewCertsEnabled | IsAutoRenewCertsEnabledSchema | | optional


# OrgNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NoVPNStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NonAccessIdentityEventRetentionDurationInHoursSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccessEventRetentionDurationInHoursSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentityEventRetentionDurationInHoursSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OwnerEmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FirstSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# APIServerLocationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IsTunnelEnabledSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IsTestDriveSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EditionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ZoneIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GlobalDomainDirectoryURLSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IsAutoRenewCertsEnabledSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_add_org_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_add_org_post.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#v1_add_org_post.ApiResponseFor403) | forbidden
409 | [ApiResponseFor409](#v1_add_org_post.ApiResponseFor409) | Bad request

#### v1_add_org_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_add_org_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_add_org_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_add_org_post.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_admin_add_user_post**
<a name="v1_admin_add_user_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_admin_add_user_post()

 POST /v1/admin/add_user

This adds a new User for the Org. A welcome email is sent to the User of the org.Authorization: AdminHeaders: Standard

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    query_params = {
        'Email': "Email_example",
        'First': "First_example",
        'Last': "Last_example",
        'Profile': "Profile_example",
        'APIServerLocation': "APIServerLocation_example",
    }
    try:
        #  POST /v1/admin/add_user
        api_response = api_instance.v1_admin_add_user_post(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_admin_add_user_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Email | EmailSchema | | optional
First | FirstSchema | | optional
Last | LastSchema | | optional
Profile | ProfileSchema | | optional
APIServerLocation | APIServerLocationSchema | | optional


# EmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FirstSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LastSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# APIServerLocationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_admin_add_user_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_admin_add_user_post.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#v1_admin_add_user_post.ApiResponseFor403) | Forbidden

#### v1_admin_add_user_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_admin_add_user_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_admin_add_user_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_admin_delete_user_delete**
<a name="v1_admin_delete_user_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_admin_delete_user_delete()

 DELETE /v1/admin/delete_user

This deletes a user from an Org. Authorization: Admin+Headers: Standard

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    query_params = {
        'Email': "Email_example",
    }
    try:
        #  DELETE /v1/admin/delete_user
        api_response = api_instance.v1_admin_delete_user_delete(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_admin_delete_user_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Email | EmailSchema | | optional


# EmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_admin_delete_user_delete.ApiResponseFor200) | OK
403 | [ApiResponseFor403](#v1_admin_delete_user_delete.ApiResponseFor403) | Forbidden

#### v1_admin_delete_user_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_admin_delete_user_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_admin_list_orgs_get**
<a name="v1_admin_list_orgs_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] v1_admin_list_orgs_get()

 GET /v1/admin/list_orgs

This lists all the Orgs

### Example

* Bearer (JWT) Authentication (bearerSuperAdminToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerSuperAdminToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET /v1/admin/list_orgs
        api_response = api_instance.v1_admin_list_orgs_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_admin_list_orgs_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_admin_list_orgs_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v1_admin_list_orgs_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v1_admin_list_orgs_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v1_admin_list_orgs_get.ApiResponseFor500) | Internal Server Error

#### v1_admin_list_orgs_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**OrgName** | str,  | str,  |  | [optional] 
**OrgID** | str,  | str,  |  | [optional] 
**OrgRegisterDate** | str,  | str,  |  | [optional] 
**CollectorActive** | str,  | str,  |  | [optional] 
**CIRegistered** | str,  | str,  |  | [optional] 
**RTRegistered** | str,  | str,  |  | [optional] 
**ImagesAfter** | str,  | str,  |  | [optional] 
**MaxPerRepo** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**HistoryHours** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IDPType** | str,  | str,  |  | [optional] 
**IDPName** | str,  | str,  |  | [optional] 
**IDPConfig** | str,  | str,  |  | [optional] 
**IDPProto** | str,  | str,  |  | [optional] 
**MDMName** | str,  | str,  |  | [optional] 
**MDMConfig** | str,  | str,  |  | [optional] 
**NoVPN** | str,  | str,  |  | [optional] 
**DNSName** | str,  | str,  |  | [optional] 
**DNSConfig** | str,  | str,  |  | [optional] 
**LastUpdatedBy** | str,  | str,  |  | [optional] 
**LastUpdatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AccessHistoryHours** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrustConfig** | str,  | str,  |  | [optional] 
**IdentityHistoryHours** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**CloakExceptions** | str,  | str,  |  | [optional] 
**RootCerts** | str,  | str,  |  | [optional] 
**MDMDeployKey** | str,  | str,  |  | [optional] 
**MDMDeployOTPSkipRole** | str,  | str,  |  | [optional] 
**DeviceRegConfig** | str,  | str,  |  | [optional] 
**DeviceRegIDPName** | str,  | str,  |  | [optional] 
**DeviceRegIDPProto** | str,  | str,  |  | [optional] 
**PWLessConfig** | str,  | str,  |  | [optional] 
**AsyncAuthEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IsTestDrive** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IsTunnelEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Edition** | str,  | str,  |  | [optional] 
**ZoneID** | str,  | str,  |  | [optional] 
**IsZTCertUpdateEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**GlobalDomainDirectoryURL** | str,  | str,  |  | [optional] 
**EnduserInactivityThresholdDays** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IDPRoutedSaasAppRedirectURL** | str,  | str,  |  | [optional] 
**IsLocalLoginEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IsAutoRenewCertsEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IsZTUpnCertEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AutoRenewCertExpiryWindowDays** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RefreshTokenForSAMLEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**CreatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_admin_list_orgs_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_admin_list_orgs_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_admin_list_orgs_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerSuperAdminToken](../../../README.md#bearerSuperAdminToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_admin_list_users_get**
<a name="v1_admin_list_users_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_admin_list_users_get()

 This API lists all the users for that Org.

This API lists all the users for that Org.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        #  This API lists all the users for that Org.
        api_response = api_instance.v1_admin_list_users_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_admin_list_users_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_admin_list_users_get.ApiResponseFor200) | OK

#### v1_admin_list_users_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**First** | str,  | str,  |  | [optional] 
**Last** | str,  | str,  |  | [optional] 
**Email** | str,  | str,  |  | [optional] 
**Registered** | str,  | str,  |  | [optional] 
**Profile** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_admin_update_user_post**
<a name="v1_admin_update_user_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_admin_update_user_post()

 POST /v1/admin/update_user

This updates the User Profile (for now). Later this can be used to update any other User attributesAuthorization: Admin+Headers: Standard

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    query_params = {
        'Email': "Email_example",
        'Profile': "Profile_example",
    }
    try:
        #  POST /v1/admin/update_user
        api_response = api_instance.v1_admin_update_user_post(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_admin_update_user_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Email | EmailSchema | | optional
Profile | ProfileSchema | | optional


# EmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProfileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_admin_update_user_post.ApiResponseFor200) | OK
403 | [ApiResponseFor403](#v1_admin_update_user_post.ApiResponseFor403) | Forbidden

#### v1_admin_update_user_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_admin_update_user_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_api_v1_admin_saml_get**
<a name="v1_api_v1_admin_saml_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_api_v1_admin_saml_get()

 Get the admin SAML Sign-on Settings for an organization

Fetch admin SAML Sign-on Settings info for an organization 

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    query_params = {
        'orgid': "orgid_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Get the admin SAML Sign-on Settings for an organization
        api_response = api_instance.v1_api_v1_admin_saml_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_api_v1_admin_saml_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
orgid | OrgidSchema | | optional


# OrgidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_api_v1_admin_saml_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_api_v1_admin_saml_get.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#v1_api_v1_admin_saml_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v1_api_v1_admin_saml_get.ApiResponseFor500) | Internal Server Error

#### v1_api_v1_admin_saml_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**OrgID** | str,  | str,  |  | [optional] 
**OrgName** | str,  | str,  |  | [optional] 
**MetadataURL** | str,  | str,  |  | [optional] 
**IDPIssuerURL** | str,  | str,  |  | [optional] 
**CallbackURL** | str,  | str,  |  | [optional] 
**RawMetadata** | str,  | str,  |  | [optional] 
**SPMetadataURL** | str,  | str,  |  | [optional] 
**[SPCertificateInfo](#SPCertificateInfo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# SPCertificateInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Expires** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Issuer** | str,  | str,  |  | [optional] 
**Certificate** | str,  | str,  |  | [optional] 
**SPIssuer** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_api_v1_admin_saml_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_api_v1_admin_saml_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_api_v1_admin_saml_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_api_v1_admin_setup_saml_post**
<a name="v1_api_v1_admin_setup_saml_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_api_v1_admin_setup_saml_post()

 Set the admin Sign-on settings for an organization

Set the adminn sign-on settings for an organizationAuthorization: admin

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    query_params = {
        'orgid': "orgid_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
        'Content-Type': "Content-Type_example",
    }
    body = dict(
        callback_url="SSO URL redirect",
        idp_issuer_url="Identity Provider Issuer URL",
        metadata_url="IDP Metadata URL, in option to RawMetadata",
        raw_meta_data="IDP Raw Metadata",
        sp_issuer="Service Provider Issuer",
    )
    try:
        #  Set the admin Sign-on settings for an organization
        api_response = api_instance.v1_api_v1_admin_setup_saml_post(
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_api_v1_admin_setup_saml_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**CallbackURL** | str,  | str,  |  | [optional] 
**IDPIssuerURL** | str,  | str,  |  | [optional] 
**MetadataURL** | str,  | str,  |  | [optional] 
**RawMetaData** | str,  | str,  |  | [optional] 
**SPIssuer** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
orgid | OrgidSchema | | optional


# OrgidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional
Content-Type | ContentTypeSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_api_v1_admin_setup_saml_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_api_v1_admin_setup_saml_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v1_api_v1_admin_setup_saml_post.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_api_v1_admin_setup_saml_post.ApiResponseFor500) | Internal Server Error

#### v1_api_v1_admin_setup_saml_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_api_v1_admin_setup_saml_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_api_v1_admin_setup_saml_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_api_v1_admin_setup_saml_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_api_v1_reset_password_post**
<a name="v1_api_v1_reset_password_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_api_v1_reset_password_post()

Reset Password for a banyan console user

resets the password for a banyan console user

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    header_params = {
        'Content-Type': "Content-Type_example",
    }
    body = dict(
        uuid="Key used to verify reset password request",
        email="Email Id of user requesting password reset",
        org_name="Name of organization user belongs to",
        password="New password",
        password2="New password",
    )
    try:
        # Reset Password for a banyan console user
        api_response = api_instance.v1_api_v1_reset_password_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_api_v1_reset_password_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**UUID** | str,  | str,  |  | [optional] 
**Email** | str,  | str,  |  | [optional] 
**OrgName** | str,  | str,  |  | [optional] 
**Password** | str,  | str,  |  | [optional] 
**Password2** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_api_v1_reset_password_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_api_v1_reset_password_post.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#v1_api_v1_reset_password_post.ApiResponseFor403) | Forbidden
410 | [ApiResponseFor410](#v1_api_v1_reset_password_post.ApiResponseFor410) | Gone
500 | [ApiResponseFor500](#v1_api_v1_reset_password_post.ApiResponseFor500) | Internal Server Error

#### v1_api_v1_reset_password_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_api_v1_reset_password_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_api_v1_reset_password_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_api_v1_reset_password_post.ApiResponseFor410
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_api_v1_reset_password_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_ca_certs_get**
<a name="v1_ca_certs_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_ca_certs_get()

fetch ca certificates for an org

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    query_params = {
        'org_id': "org_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # fetch ca certificates for an org
        api_response = api_instance.v1_ca_certs_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_ca_certs_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
org_id | OrgIdSchema | | optional


# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_ca_certs_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_ca_certs_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v1_ca_certs_get.ApiResponseFor500) | Internal server error

#### v1_ca_certs_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**root_ca_certs** | str,  | str,  |  | [optional] 
**intermediate_ca_certs** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_ca_certs_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_ca_certs_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_delete_org_delete**
<a name="v1_delete_org_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_delete_org_delete()

 Delete Org

This end point deletes an org and its related tables from mysql, influxdb

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    query_params = {
        'OrgID': "OrgID_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Delete Org
        api_response = api_instance.v1_delete_org_delete(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_delete_org_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
OrgID | OrgIDSchema | | optional


# OrgIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_delete_org_delete.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_delete_org_delete.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#v1_delete_org_delete.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v1_delete_org_delete.ApiResponseFor500) | Internal Server Error

#### v1_delete_org_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_delete_org_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_delete_org_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_delete_org_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_delete_pwless_config_delete**
<a name="v1_delete_pwless_config_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_delete_pwless_config_delete()

 Delete pwless config for an org

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Delete pwless config for an org
        api_response = api_instance.v1_delete_pwless_config_delete(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_delete_pwless_config_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_delete_pwless_config_delete.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_delete_pwless_config_delete.ApiResponseFor400) | BadRequest
403 | [ApiResponseFor403](#v1_delete_pwless_config_delete.ApiResponseFor403) | Forbidden
422 | [ApiResponseFor422](#v1_delete_pwless_config_delete.ApiResponseFor422) | Unprocessable entity
500 | [ApiResponseFor500](#v1_delete_pwless_config_delete.ApiResponseFor500) | Internal Server Error

#### v1_delete_pwless_config_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_delete_pwless_config_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_delete_pwless_config_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_delete_pwless_config_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_delete_pwless_config_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_insert_pwless_config_post**
<a name="v1_insert_pwless_config_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_insert_pwless_config_post(redirect_url)

 Create pwless config for an org

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'redirect url': "redirect url_example",
    }
    header_params = {
    }
    try:
        #  Create pwless config for an org
        api_response = api_instance.v1_insert_pwless_config_post(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_insert_pwless_config_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'redirect url': "redirect url_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Create pwless config for an org
        api_response = api_instance.v1_insert_pwless_config_post(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_insert_pwless_config_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
redirect url | RedirectUrlSchema | | 


# RedirectUrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_insert_pwless_config_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_insert_pwless_config_post.ApiResponseFor400) | BadRequest
401 | [ApiResponseFor401](#v1_insert_pwless_config_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v1_insert_pwless_config_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v1_insert_pwless_config_post.ApiResponseFor500) | Internal Server Error

#### v1_insert_pwless_config_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_insert_pwless_config_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_insert_pwless_config_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_insert_pwless_config_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_insert_pwless_config_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_org_details_get**
<a name="v1_org_details_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_org_details_get()

 Get org details

This end point returns details of org 

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        'Content-Type': "Content-Type_example",
    }
    try:
        #  Get org details
        api_response = api_instance.v1_org_details_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_org_details_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional
Content-Type | ContentTypeSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_org_details_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_org_details_get.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v1_org_details_get.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_org_details_get.ApiResponseFor500) | Internal Server Error

#### v1_org_details_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**OrgName** | str,  | str,  |  | [optional] 
**OrgID** | str,  | str,  |  | [optional] 
**MDMName** | str,  | str,  |  | [optional] 
**MDMConfig** | str,  | str,  |  | [optional] 
**IDPName** | str,  | str,  |  | [optional] 
**IDPConfig** | str,  | str,  |  | [optional] 
**DNSName** | str,  | str,  |  | [optional] 
**DNSConfig** | str,  | str,  |  | [optional] 
**TrustConfig** | str,  | str,  |  | [optional] 
**[CACerts](#CACerts)** | list, tuple,  | tuple,  |  | [optional] 
**CAChain** | str,  | str,  |  | [optional] 
**CloakExceptions** | str,  | str,  |  | [optional] 
**AsyncAuthEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IsTestDrive** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IsTunnelEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Edition** | str,  | str,  |  | [optional] 
**ZoneID** | str,  | str,  |  | [optional] 
**IsZTCertUpdateEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**EnduserInactivityThresholdDays** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IsAutoRenewCertsEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IsZTUpnCertEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AutoRenewCertExpiryWindowDays** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**CreatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[OnboardingState](#OnboardingState)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**SupportMessage** | str,  | str,  |  | [optional] 
**SupportLinkTitle** | str,  | str,  |  | [optional] 
**SupportLinkUrl** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# CACerts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# OnboardingState

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**state** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**connectorId** | str,  | str,  |  | [optional] 
**serviceId** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_org_details_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_org_details_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_org_details_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_org_status_get**
<a name="v1_org_status_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_org_status_get()

 Get org status

This end point returns type of login for an org (either TEAM, SAML or BANYAN)

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    query_params = {
        'orgname': "orgname_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
        '2. Content-Type': "2. Content-Type_example",
    }
    try:
        #  Get org status
        api_response = api_instance.v1_org_status_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_org_status_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
orgname | OrgnameSchema | | optional


# OrgnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional
2. Content-Type | Model2ContentTypeSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Model2ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_org_status_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_org_status_get.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v1_org_status_get.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_org_status_get.ApiResponseFor500) | Internal Server Error

#### v1_org_status_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_org_status_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_org_status_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_org_status_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_update_org_post**
<a name="v1_update_org_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_update_org_post()

 Update Org

This end point updates org fields

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        images_after="Only images created after this time will be shown, format",
        max_per_repo="Max images per repo",
        idp_type="type of login for command center (BANYAN | SAML)",
        idp_protocol="main identity provider's protocol (OIDC | SAML)",
        idp_name="name of main identity provider",
        idp_config="config of main identity provider like id, secret, callback url",
        device_reg_idp_name="name of device registration identity provider",
        device_reg_idp_protocol="device registration identity provider's protocol (OIDC | SAML)",
        device_reg_config="config of device registration idp like id, secret, callback url",
        mdm_name="name of mdm",
        mdm_config="config of mdm",
        trust_config="json string that contains token expiry hours for registration, reporting, login/trust token. eg",
        cloak_exceptions="json string for incremental device rollout (permissive mode for device trust), indicating CIDR ranges for source IPs that are exempt from cloaking.",
        root_certs="String that contains Root Certificate(s). Cert sent from UI converts the newlines to spaces, which will be transformed into proper cert before saving. Cert from UI",
        is_tunnel_enabled="set true for satellite tunnel enabled org",
        enable_async_auth="to enable or disable async auth for sandbox apps. Since sandbox app doesn't have access to device keychain, user/client can present the certificate in async manner to authenticate",
        is_zt_cert_update_enabled_value="zero touch installed device has certificate with device-only claims, if this flag is enabled then device certificate will be updated in background while user tries to login using that certificate",
        edition="to set the Edition (and thus the feature set) of the Banyan Command Center. The default is 'Enterprise'   but we also accept 'Team'",
        zone_id="to update dns records for domains related to the org",
        global_domain_directory_url="Restapi server host where we want to store the directory of verified registered domains",
        enduser_inactivity_threshold_days="to set no of days which defines interval of inactive endusers.The value should be greater than or equal to 30. However, to disable this feature, it can be set to 0.",
        support_message="For support, please contact",
        support_link_title="banyan website",
        support_link_url="https://www.banyansec.com",
    )
    try:
        #  Update Org
        api_response = api_instance.v1_update_org_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_update_org_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ImagesAfter** | str,  | str,  |  | [optional] 
**MaxPerRepo** | str,  | str,  |  | [optional] 
**IDPType** | str,  | str,  |  | [optional] 
**IDPProtocol** | str,  | str,  |  | [optional] 
**IDPName** | str,  | str,  |  | [optional] 
**IDPConfig** | str,  | str,  |  | [optional] 
**DeviceRegIDPName** | str,  | str,  |  | [optional] 
**DeviceRegIDPProtocol** | str,  | str,  |  | [optional] 
**DeviceRegConfig** | str,  | str,  |  | [optional] 
**MDMName** | str,  | str,  |  | [optional] 
**MDMConfig** | str,  | str,  |  | [optional] 
**TrustConfig** | str,  | str,  |  | [optional] 
**CloakExceptions** | str,  | str,  |  | [optional] 
**RootCerts** | str,  | str,  |  | [optional] 
**IsTunnelEnabled** | str,  | str,  |  | [optional] 
**EnableAsyncAuth** | str,  | str,  |  | [optional] 
**isZTCertUpdateEnabledValue** | str,  | str,  |  | [optional] 
**Edition** | str,  | str,  |  | [optional] 
**ZoneID** | str,  | str,  |  | [optional] 
**GlobalDomainDirectoryURL** | str,  | str,  |  | [optional] 
**EnduserInactivityThresholdDays** | str,  | str,  |  | [optional] 
**SupportMessage** | str,  | str,  |  | [optional] 
**SupportLinkTitle** | str,  | str,  |  | [optional] 
**SupportLinkUrl** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_update_org_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_update_org_post.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#v1_update_org_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v1_update_org_post.ApiResponseFor500) | Internal Server Error

#### v1_update_org_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_update_org_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_update_org_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_update_org_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_user_org_details_get**
<a name="v1_user_org_details_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_user_org_details_get()

 Get user's org details

This end point returns details of org of an user

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        '2. Content-Type': "2. Content-Type_example",
    }
    try:
        #  Get user's org details
        api_response = api_instance.v1_user_org_details_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v1_user_org_details_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional
2. Content-Type | Model2ContentTypeSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# Model2ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_user_org_details_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_user_org_details_get.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v1_user_org_details_get.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_user_org_details_get.ApiResponseFor500) | Internal Server Error

#### v1_user_org_details_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**OrgName** | str,  | str,  |  | [optional] 
**First** | str,  | str,  |  | [optional] 
**Last** | str,  | str,  |  | [optional] 
**Email** | str,  | str,  |  | [optional] 
**HashedPassword** | str,  | str,  |  | [optional] 
**RegisterKey** | str,  | str,  |  | [optional] 
**RegisterDate** | str,  | str,  |  | [optional] 
**Notifications** | str,  | str,  |  | [optional] 
**LastNotifyTime** | str,  | str,  |  | [optional] 
**RefreshToken** | str,  | str,  |  | [optional] 
**Profile** | str,  | str,  |  | [optional] 
**OrgID** | str,  | str,  |  | [optional] 
**OrgRegisterDate** | str,  | str,  |  | [optional] 
**CollectorActive** | str,  | str,  |  | [optional] 
**CIRegistered** | str,  | str,  |  | [optional] 
**RTRegistered** | str,  | str,  |  | [optional] 
**ImagesAfter** | str,  | str,  |  | [optional] 
**MaxPerRepo** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**HistoryHours** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IDPName** | str,  | str,  |  | [optional] 
**IDPConfig** | str,  | str,  |  | [optional] 
**IDPProto** | str,  | str,  |  | [optional] 
**MDMName** | str,  | str,  |  | [optional] 
**MDMConfig** | str,  | str,  |  | [optional] 
**NoVPN** | str,  | str,  |  | [optional] 
**DNSName** | str,  | str,  |  | [optional] 
**DNSConfig** | str,  | str,  |  | [optional] 
**LastUpdatedBy** | str,  | str,  |  | [optional] 
**LastUpdatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AccessHistoryHours** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrustConfig** | str,  | str,  |  | [optional] 
**IdentityHistoryHours** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**CloakExceptions** | str,  | str,  |  | [optional] 
**RootCert** | str,  | str,  |  | [optional] 
**MDMDeployKey** | str,  | str,  |  | [optional] 
**MDMDeployOTPSkipRole** | str,  | str,  |  | [optional] 
**DeviceRegIDPName** | str,  | str,  |  | [optional] 
**DeviceRegIDPConfig** | str,  | str,  |  | [optional] 
**DeviceRegIDPProto** | str,  | str,  |  | [optional] 
**PWLessConfig** | str,  | str,  |  | [optional] 
**ID** | str,  | str,  |  | [optional] 
**IsLocalLoginEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RefreshTokenForSAMLEnabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**SupportMessage** | str,  | str,  |  | [optional] 
**SupportLinkTitle** | str,  | str,  |  | [optional] 
**SupportLinkUrl** | str,  | str,  |  | [optional] 
**AccountType** | str,  | str,  |  | [optional] 
**HasRefreshToken** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**IDPType** | str,  | str,  |  | [optional] 
**[ShieldLastActivity](#ShieldLastActivity)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[ShieldLastActivityMap](#ShieldLastActivityMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**TrustproviderURL** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ShieldLastActivity

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**InsertTime** | str,  | str,  |  | [optional] 
**Status** | str,  | str,  |  | [optional] 
**UUID** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ShieldLastActivityMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[example-udid](#example-udid)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# example-udid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**InsertTime** | str,  | str,  |  | [optional] 
**Status** | str,  | str,  |  | [optional] 
**UUID** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_user_org_details_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_user_org_details_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_user_org_details_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_admin_client_certificate_get**
<a name="v2_admin_client_certificate_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_admin_client_certificate_get()

 GET client certificate details

Get the list of client certificates under an organization

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    query_params = {
        'revoked_status': "revoked_status_example",
        'skip': 1,
        'limit': 1,
        'expiry_start_time': 1,
        'expiry_end_time': 1,
    }
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  GET client certificate details
        api_response = api_instance.v2_admin_client_certificate_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v2_admin_client_certificate_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
revoked_status | RevokedStatusSchema | | optional
skip | SkipSchema | | optional
limit | LimitSchema | | optional
expiry_start_time | ExpiryStartTimeSchema | | optional
expiry_end_time | ExpiryEndTimeSchema | | optional


# RevokedStatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SkipSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExpiryStartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ExpiryEndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional
ContentType | ContentTypeSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_admin_client_certificate_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_admin_client_certificate_get.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_admin_client_certificate_get.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v2_admin_client_certificate_get.ApiResponseFor500) | Internal Server Error

#### v2_admin_client_certificate_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[certificates](#certificates)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# certificates

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**device_serialnumber** | str,  | str,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**certificate_serialnumber** | str,  | str,  |  | [optional] 
**expiry** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**revoked_status** | str,  | str,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_admin_client_certificate_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**data** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_admin_client_certificate_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_admin_client_certificate_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_mom_org_get**
<a name="v2_mom_org_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_mom_org_get()

 Get list of all Orgs

lists all the Orgs

### Example

* Bearer (JWT) Authentication (bearerMOMToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerMOMToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only optional values
    query_params = {
        'name': "name_example",
        'customerId': "customerId_example",
        'type': "type_example",
        'limit': 1,
        'skip': 1,
    }
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  Get list of all Orgs
        api_response = api_instance.v2_mom_org_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v2_mom_org_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | optional
customerId | CustomerIdSchema | | optional
type | TypeSchema | | optional
limit | LimitSchema | | optional
skip | SkipSchema | | optional


# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CustomerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SkipSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional
ContentType | ContentTypeSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_mom_org_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_mom_org_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_mom_org_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_mom_org_get.ApiResponseFor500) | Internal Server Error

#### v2_mom_org_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**org_name** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**last_updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**last_updated_by** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_by** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**customer_id** | str,  | str,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**global_edge** | bool,  | BoolClass,  |  | [optional] 
**private_edge** | bool,  | BoolClass,  |  | [optional] 
**[provision_status](#provision_status)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# provision_status

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_tier** | str,  | str,  |  | [optional] 
**connector** | str,  | str,  |  | [optional] 
**org_data** | str,  | str,  |  | [optional] 
**invite_code** | str,  | str,  |  | [optional] 
**user_pool_domain** | str,  | str,  |  | [optional] 
**user_pool** | str,  | str,  |  | [optional] 
**user** | str,  | str,  |  | [optional] 
**registered_domain** | str,  | str,  |  | [optional] 
**shield** | str,  | str,  |  | [optional] 
**default_groups_user** | str,  | str,  |  | [optional] 
**user_pool_client** | str,  | str,  |  | [optional] 
**default_groups_user_pool** | str,  | str,  |  | [optional] 
**update_user_pool** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_mom_org_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_mom_org_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_mom_org_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerMOMToken](../../../README.md#bearerMOMToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_mom_org_org_id_get**
<a name="v2_mom_org_org_id_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_mom_org_org_id_get(org_id)

 Get Org by org id

Get org by org id

### Example

* Bearer (JWT) Authentication (bearerMOMToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerMOMToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'org_id': "org_id_example",
    }
    header_params = {
    }
    try:
        #  Get Org by org id
        api_response = api_instance.v2_mom_org_org_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v2_mom_org_org_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'org_id': "org_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  Get Org by org id
        api_response = api_instance.v2_mom_org_org_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v2_mom_org_org_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional
ContentType | ContentTypeSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
org_id | OrgIdSchema | | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_mom_org_org_id_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_mom_org_org_id_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_mom_org_org_id_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_mom_org_org_id_get.ApiResponseFor500) | Internal Server Error

#### v2_mom_org_org_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[items](#items)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**org_name** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**last_updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**last_updated_by** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_by** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**customer_id** | str,  | str,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**global_edge** | bool,  | BoolClass,  |  | [optional] 
**private_edge** | bool,  | BoolClass,  |  | [optional] 
**[provision_status](#provision_status)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# provision_status

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_tier** | str,  | str,  |  | [optional] 
**connector** | str,  | str,  |  | [optional] 
**org_data** | str,  | str,  |  | [optional] 
**invite_code** | str,  | str,  |  | [optional] 
**user_pool_domain** | str,  | str,  |  | [optional] 
**user_pool** | str,  | str,  |  | [optional] 
**user** | str,  | str,  |  | [optional] 
**registered_domain** | str,  | str,  |  | [optional] 
**shield** | str,  | str,  |  | [optional] 
**default_groups_user** | str,  | str,  |  | [optional] 
**user_pool_client** | str,  | str,  |  | [optional] 
**default_groups_user_pool** | str,  | str,  |  | [optional] 
**update_user_pool** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_mom_org_org_id_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_mom_org_org_id_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_mom_org_org_id_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerMOMToken](../../../README.md#bearerMOMToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_mom_org_post**
<a name="v2_mom_org_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_mom_org_post(any_type)

Create and provision a Org

Create and provision an org

### Example

* Bearer (JWT) Authentication (bearerMOMToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerMOMToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        org_name="testorg",
        first_name="TestFirst",
        last_name="TestLast",
        email="test@bnntest.com",
        edition="Enterprise",
        type="Internal",
        customer_id="testorg",
        global_edge=True,
        private_edge=False,
        archived=False,
    )
    try:
        # Create and provision a Org
        api_response = api_instance.v2_mom_org_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v2_mom_org_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    body = dict(
        org_name="testorg",
        first_name="TestFirst",
        last_name="TestLast",
        email="test@bnntest.com",
        edition="Enterprise",
        type="Internal",
        customer_id="testorg",
        global_edge=True,
        private_edge=False,
        archived=False,
    )
    try:
        # Create and provision a Org
        api_response = api_instance.v2_mom_org_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v2_mom_org_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**org_name** | str,  | str,  |  | [optional] 
**first_name** | str,  | str,  |  | [optional] 
**last_name** | str,  | str,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**customer_id** | str,  | str,  |  | [optional] 
**global_edge** | bool,  | BoolClass,  |  | [optional] 
**private_edge** | bool,  | BoolClass,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional
ContentType | ContentTypeSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_mom_org_post.ApiResponseFor200) | OK

#### v2_mom_org_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[items](#items)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**org_name** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**last_updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**last_updated_by** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_by** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**customer_id** | str,  | str,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**global_edge** | bool,  | BoolClass,  |  | [optional] 
**private_edge** | bool,  | BoolClass,  |  | [optional] 
**[provision_status](#provision_status)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# provision_status

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_tier** | str,  | str,  |  | [optional] 
**connector** | str,  | str,  |  | [optional] 
**org_data** | str,  | str,  |  | [optional] 
**invite_code** | str,  | str,  |  | [optional] 
**user_pool_domain** | str,  | str,  |  | [optional] 
**user_pool** | str,  | str,  |  | [optional] 
**user** | str,  | str,  |  | [optional] 
**registered_domain** | str,  | str,  |  | [optional] 
**shield** | str,  | str,  |  | [optional] 
**default_groups_user** | str,  | str,  |  | [optional] 
**user_pool_client** | str,  | str,  |  | [optional] 
**default_groups_user_pool** | str,  | str,  |  | [optional] 
**update_user_pool** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[bearerMOMToken](../../../README.md#bearerMOMToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_mom_org_put**
<a name="v2_mom_org_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_mom_org_put(any_type)

Create and provision a Org

Create and provision an org

### Example

* Bearer (JWT) Authentication (bearerMOMToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerMOMToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        org_name="testorg",
        first_name="TestFirst",
        last_name="TestLast",
        email="test@bnntest.com",
        edition="Enterprise",
        type="Internal",
        customer_id="testorg",
        global_edge=True,
        private_edge=False,
        archived=False,
    )
    try:
        # Create and provision a Org
        api_response = api_instance.v2_mom_org_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v2_mom_org_put: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    body = dict(
        org_name="testorg",
        first_name="TestFirst",
        last_name="TestLast",
        email="test@bnntest.com",
        edition="Enterprise",
        type="Internal",
        customer_id="testorg",
        global_edge=True,
        private_edge=False,
        archived=False,
    )
    try:
        # Create and provision a Org
        api_response = api_instance.v2_mom_org_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v2_mom_org_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**org_name** | str,  | str,  |  | [optional] 
**first_name** | str,  | str,  |  | [optional] 
**last_name** | str,  | str,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**customer_id** | str,  | str,  |  | [optional] 
**global_edge** | bool,  | BoolClass,  |  | [optional] 
**private_edge** | bool,  | BoolClass,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional
ContentType | ContentTypeSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_mom_org_put.ApiResponseFor200) | OK

#### v2_mom_org_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**[items](#items)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**org_name** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**last_updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**last_updated_by** | str,  | str,  |  | [optional] 
**edition** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_by** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**customer_id** | str,  | str,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**global_edge** | bool,  | BoolClass,  |  | [optional] 
**private_edge** | bool,  | BoolClass,  |  | [optional] 
**[provision_status](#provision_status)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# provision_status

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_tier** | str,  | str,  |  | [optional] 
**connector** | str,  | str,  |  | [optional] 
**org_data** | str,  | str,  |  | [optional] 
**invite_code** | str,  | str,  |  | [optional] 
**user_pool_domain** | str,  | str,  |  | [optional] 
**user_pool** | str,  | str,  |  | [optional] 
**user** | str,  | str,  |  | [optional] 
**registered_domain** | str,  | str,  |  | [optional] 
**shield** | str,  | str,  |  | [optional] 
**default_groups_user** | str,  | str,  |  | [optional] 
**user_pool_client** | str,  | str,  |  | [optional] 
**default_groups_user_pool** | str,  | str,  |  | [optional] 
**update_user_pool** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[bearerMOMToken](../../../README.md#bearerMOMToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_onboarding_state_post**
<a name="v2_onboarding_state_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_onboarding_state_post(any_type)

 Set org onboarding state

Set onboarding state for an org

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import org_api
from pprint import pprint
# Defining the host is optional and defaults to https://dev02.console.bnntest.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://dev02.console.bnntest.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuthToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = org_api.OrgApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        state="hosted_service_success",
        type="ssh",
        connector_id="test-connector",
        service_id="test-service",
    )
    try:
        #  Set org onboarding state
        api_response = api_instance.v2_onboarding_state_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v2_onboarding_state_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        state="hosted_service_success",
        type="ssh",
        connector_id="test-connector",
        service_id="test-service",
    )
    try:
        #  Set org onboarding state
        api_response = api_instance.v2_onboarding_state_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrgApi->v2_onboarding_state_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**state** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**connectorId** | str,  | str,  |  | [optional] 
**serviceId** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Authorization | AuthorizationSchema | | optional

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_onboarding_state_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_onboarding_state_post.ApiResponseFor400) | BadRequest
401 | [ApiResponseFor401](#v2_onboarding_state_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_onboarding_state_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_onboarding_state_post.ApiResponseFor500) | InternalServerError

#### v2_onboarding_state_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**data** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_onboarding_state_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**data** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_onboarding_state_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**data** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_onboarding_state_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_onboarding_state_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

