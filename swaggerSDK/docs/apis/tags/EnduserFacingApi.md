<a name="__pageTop"></a>
# openapi_client.apis.tags.enduser_facing_api.EnduserFacingApi

All URIs are relative to *https://dev02.console.bnntest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_cert_exchange_get**](#v1_cert_exchange_get) | **get** /v1/cert_exchange |  Get device certificates
[**v1_cert_exchange_post**](#v1_cert_exchange_post) | **post** /v1/cert_exchange |  Post device certificates
[**v1_config_get**](#v1_config_get) | **get** /v1/config |  Get config for an invite code
[**v1_config_url_get**](#v1_config_url_get) | **get** /v1/config_url |  Get command center url for an invite code
[**v1_device_refresh_certs_post**](#v1_device_refresh_certs_post) | **post** /v1/device/refresh_certs |  POST to get refresh certificates of device
[**v1_device_register_post**](#v1_device_register_post) | **post** /v1/device/register |  Get device certificates
[**v1_enduser_facing_app_version_put**](#v1_enduser_facing_app_version_put) | **put** /v1/enduser_facing/app_version |  Update enduser device appversion
[**v1_enduser_facing_device_features_post**](#v1_enduser_facing_device_features_post) | **post** /v1/enduser_facing/device_features |  Submit device features
[**v1_enduser_facing_devices_get**](#v1_enduser_facing_devices_get) | **get** /v1/enduser_facing/devices |  List enduser devices
[**v1_enduser_facing_org_details_get**](#v1_enduser_facing_org_details_get) | **get** /v1/enduser_facing/org_details |  Get org details  
[**v1_enduser_facing_services_get**](#v1_enduser_facing_services_get) | **get** /v1/enduser_facing/services |  List enduser device accessible services
[**v1_enduser_facing_set_max_trust_level_post**](#v1_enduser_facing_set_max_trust_level_post) | **post** /v1/enduser_facing/set_max_trust_level | Set Max Trust Level
[**v1_enduser_facing_trustscores_get**](#v1_enduser_facing_trustscores_get) | **get** /v1/enduser_facing/trustscores |  List enduser device trustscores
[**v1_set_max_trust_level_post**](#v1_set_max_trust_level_post) | **post** /v1/set_max_trust_level |  Set Max Trust Level
[**v2_cert_request_device_only_registration_post**](#v2_cert_request_device_only_registration_post) | **post** /v2/cert_request/device_only_registration |  POST to get different types of certificates
[**v2_client_certificate_get**](#v2_client_certificate_get) | **get** /v2/client_certificate |  GET client certificate details
[**v2_enduser_facing_autorun_service_get**](#v2_enduser_facing_autorun_service_get) | **get** /v2/enduser_facing/autorun_service |  GET autorun services
[**v2_enduser_facing_autorun_service_service_id_delete**](#v2_enduser_facing_autorun_service_service_id_delete) | **delete** /v2/enduser_facing/autorun_service/{service_id} |  DELETE to remove a service from a user&#x27;s autorun list
[**v2_enduser_facing_autorun_service_service_id_post**](#v2_enduser_facing_autorun_service_service_id_post) | **post** /v2/enduser_facing/autorun_service/{service_id} |  POST to create a autorun service
[**v2_enduser_facing_bundle_bundle_id_put**](#v2_enduser_facing_bundle_bundle_id_put) | **put** /v2/enduser_facing/bundle/{bundle_id} |  Update an existing service bundle
[**v2_enduser_facing_bundle_bundle_id_service_post**](#v2_enduser_facing_bundle_bundle_id_service_post) | **post** /v2/enduser_facing/bundle/{bundle_id}/service |  Create a service bundle
[**v2_enduser_facing_bundle_get**](#v2_enduser_facing_bundle_get) | **get** /v2/enduser_facing/bundle |  GET service bundles
[**v2_enduser_facing_bundle_post**](#v2_enduser_facing_bundle_post) | **post** /v2/enduser_facing/bundle |  create a service bundle
[**v2_enduser_facing_client_cert_issue_post**](#v2_enduser_facing_client_cert_issue_post) | **post** /v2/enduser_facing/client_cert/issue |  issue client certificate
[**v2_enduser_facing_favorite_service_get**](#v2_enduser_facing_favorite_service_get) | **get** /v2/enduser_facing/favorite_service |  GET favorite services
[**v2_enduser_facing_favorite_service_service_id_delete**](#v2_enduser_facing_favorite_service_service_id_delete) | **delete** /v2/enduser_facing/favorite_service/{service_id} |  DELETE to remove a service from a user&#x27;s favorite list
[**v2_enduser_facing_favorite_service_service_id_post**](#v2_enduser_facing_favorite_service_service_id_post) | **post** /v2/enduser_facing/favorite_service/{service_id} |  POST to create a favorite service
[**v2_enduser_facing_integration_device_identity_command_get**](#v2_enduser_facing_integration_device_identity_command_get) | **get** /v2/enduser_facing/integration/device_identity_command |  GET integration device-identity commands
[**v2_enduser_facing_login_services_get**](#v2_enduser_facing_login_services_get) | **get** /v2/enduser_facing/login_services |  GET to return the list of services visible using a login token
[**v2_enduser_facing_logs_post**](#v2_enduser_facing_logs_post) | **post** /v2/enduser_facing/logs | Get the url to upload app logs
[**v2_enduser_facing_org_support_get**](#v2_enduser_facing_org_support_get) | **get** /v2/enduser_facing/org_support | Get org support info
[**v2_enduser_facing_service_tunnel_get**](#v2_enduser_facing_service_tunnel_get) | **get** /v2/enduser_facing/service_tunnel |  Get service tunnel config 
[**v2_enduser_facing_tunnel_config_get**](#v2_enduser_facing_tunnel_config_get) | **get** /v2/enduser_facing/tunnel_config |  Get enduser_device tunnel config 
[**v2_enduser_facing_tunnel_config_post**](#v2_enduser_facing_tunnel_config_post) | **post** /v2/enduser_facing/tunnel_config |  Save enduser_device tunnel config information for an organization
[**v2_staged_device_cert_password_get**](#v2_staged_device_cert_password_get) | **get** /v2/staged_device_cert_password |  GET to return the password needed to unlock a staged device cert

# **v1_cert_exchange_get**
<a name="v1_cert_exchange_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_cert_exchange_get()

 Get device certificates

This end point returns root and client certificate after validating the auth factor

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    query_params = {
        'Operation': "Operation_example",
        'Message': "Message_example",
        'ResponseType': "ResponseType_example",
        'IDToken': "IDToken_example",
        'ALTERNATERESPONSE': "ALTERNATERESPONSE_example",
        'AccessToken (optional)': "AccessToken (optional)_example",
    }
    try:
        #  Get device certificates
        api_response = api_instance.v1_cert_exchange_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_cert_exchange_get: %s\n" % e)
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
Operation | OperationSchema | | optional
Message | MessageSchema | | optional
ResponseType | ResponseTypeSchema | | optional
IDToken | IDTokenSchema | | optional
ALTERNATERESPONSE | ALTERNATERESPONSESchema | | optional
AccessToken (optional) | AccessTokenOptionalSchema | | optional


# OperationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MessageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResponseTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IDTokenSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ALTERNATERESPONSESchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccessTokenOptionalSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_cert_exchange_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_cert_exchange_get.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v1_cert_exchange_get.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#v1_cert_exchange_get.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#v1_cert_exchange_get.ApiResponseFor500) | Internal Server Error

#### v1_cert_exchange_get.ApiResponseFor200
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
**[root_ca_certs](#root_ca_certs)** | list, tuple,  | tuple,  |  | [optional] 
**[intermediate_ca_certs](#intermediate_ca_certs)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# root_ca_certs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# intermediate_ca_certs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### v1_cert_exchange_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_cert_exchange_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_cert_exchange_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_cert_exchange_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_cert_exchange_post**
<a name="v1_cert_exchange_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_cert_exchange_post(any_type)

 Post device certificates

This end point adds root and client certificate

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    body = dict(
        message="CSR goes here",
        operation="GetCACert or PKIOperation",
        response_type="JSON",
        id_token="Login token goes here",
        alternate_response="TRUE",
        access_token="Access token goes here",
    )
    try:
        #  Post device certificates
        api_response = api_instance.v1_cert_exchange_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_cert_exchange_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
**message** | str,  | str,  |  | [optional] 
**operation** | str,  | str,  |  | [optional] 
**response_type** | str,  | str,  |  | [optional] 
**id_token** | str,  | str,  |  | [optional] 
**alternate_response** | str,  | str,  |  | [optional] 
**access_token** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_cert_exchange_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_cert_exchange_post.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v1_cert_exchange_post.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_cert_exchange_post.ApiResponseFor500) | Internal Server Error

#### v1_cert_exchange_post.ApiResponseFor200
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
**certificate** | str,  | str,  |  | [optional] 
**ssh_certificate** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_cert_exchange_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_cert_exchange_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_cert_exchange_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_config_get**
<a name="v1_config_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_config_get()

 Get config for an invite code

This end point returns config for an org

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    query_params = {
        'org id': "org id_example",
    }
    try:
        #  Get config for an invite code
        api_response = api_instance.v1_config_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_config_get: %s\n" % e)
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
org id | OrgIdSchema | | optional


# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_config_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_config_get.ApiResponseFor400) | Bad request
500 | [ApiResponseFor500](#v1_config_get.ApiResponseFor500) | Internal Server Error

#### v1_config_get.ApiResponseFor200
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
**command_center_url** | str,  | str,  |  | [optional] 
**trust_provider_url** | str,  | str,  |  | [optional] 
**registration_trust_provider_url** | str,  | str,  |  | [optional] 
**login_client_id** | str,  | str,  |  | [optional] 
**registration_client_id** | str,  | str,  |  | [optional] 
**reporting_client_id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**org_name** | str,  | str,  |  | [optional] 
**shield_uuid** | str,  | str,  |  | [optional] 
**renewal_client_id** | str,  | str,  |  | [optional] 
**external_client_id** | str,  | str,  |  | [optional] 
**is_test_drive** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**user_info_url** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_config_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_config_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_config_url_get**
<a name="v1_config_url_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_config_url_get()

 Get command center url for an invite code

This end point calls meta command center to get the command center url for an invite code

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    query_params = {
        'invite code': "invite code_example",
    }
    try:
        #  Get command center url for an invite code
        api_response = api_instance.v1_config_url_get(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_config_url_get: %s\n" % e)
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
invite code | InviteCodeSchema | | optional


# InviteCodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_config_url_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_config_url_get.ApiResponseFor400) | Bad request
404 | [ApiResponseFor404](#v1_config_url_get.ApiResponseFor404) | NotFound
500 | [ApiResponseFor500](#v1_config_url_get.ApiResponseFor500) | Internal Server Error

#### v1_config_url_get.ApiResponseFor200
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
**org_id** | str,  | str,  |  | [optional] 
**command_center_url** | str,  | str,  |  | [optional] 
**invite_code** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_config_url_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_config_url_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_config_url_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_device_refresh_certs_post**
<a name="v1_device_refresh_certs_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_device_refresh_certs_post(any_type)

 POST to get refresh certificates of device

This end point is used to refresh client certificate of given device 

### Example

* Bearer (JWT) Authentication (bearerRenewalToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerRenewalToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        csr="test_csr_value",
        serial_number="test_serial_number_value",
    )
    try:
        #  POST to get refresh certificates of device
        api_response = api_instance.v1_device_refresh_certs_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_device_refresh_certs_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        csr="test_csr_value",
        serial_number="test_serial_number_value",
    )
    try:
        #  POST to get refresh certificates of device
        api_response = api_instance.v1_device_refresh_certs_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_device_refresh_certs_post: %s\n" % e)
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
**csr** | str,  | str,  |  | [optional] 
**serial_number** | str,  | str,  |  | [optional] 
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
200 | [ApiResponseFor200](#v1_device_refresh_certs_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_device_refresh_certs_post.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v1_device_refresh_certs_post.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_device_refresh_certs_post.ApiResponseFor500) | Internal Server Error

#### v1_device_refresh_certs_post.ApiResponseFor200
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
**[root_ca_certs](#root_ca_certs)** | list, tuple,  | tuple,  |  | [optional] 
**intermediate_ca_certs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**client_cert** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# root_ca_certs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### v1_device_refresh_certs_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_device_refresh_certs_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_device_refresh_certs_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerRenewalToken](../../../README.md#bearerRenewalToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_device_register_post**
<a name="v1_device_register_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_device_register_post(any_type)

 Get device certificates

This end point returns root and client certificate after validating the auth factor

### Example

* Bearer (JWT) Authentication (bearerRegistrationToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerRegistrationToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    header_params = {
    }
    body = dict(
        exp="1557433216331219184",
        req_id="NZWMF0ECi1p7A_Uf3obnmw",
        hash="HNtX+UfobdTR25sAOWEsQWU8ZzI4aWV2i4rY/HzjSvY=",
        auth_factor="323212",
        csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICuDCCAaACAQAwPjETMBEGA1\n-----END CERTIFICATE REQUEST-----\n",
        serial_number="VVF3232DADSK9",
        model="Macbook Pro",
        device_friendly_name="John's Macbook Pro",
        ownership="C",
        platform="Darwin",
        architecture="amd64",
        notification_token="'auej8120edi209i23di02di023di2' // only required for iOS devices",
        mdm_present=1,
    )
    try:
        #  Get device certificates
        api_response = api_instance.v1_device_register_post(
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_device_register_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'ALTERNATERESPONSE': True,
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        exp="1557433216331219184",
        req_id="NZWMF0ECi1p7A_Uf3obnmw",
        hash="HNtX+UfobdTR25sAOWEsQWU8ZzI4aWV2i4rY/HzjSvY=",
        auth_factor="323212",
        csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICuDCCAaACAQAwPjETMBEGA1\n-----END CERTIFICATE REQUEST-----\n",
        serial_number="VVF3232DADSK9",
        model="Macbook Pro",
        device_friendly_name="John's Macbook Pro",
        ownership="C",
        platform="Darwin",
        architecture="amd64",
        notification_token="'auej8120edi209i23di02di023di2' // only required for iOS devices",
        mdm_present=1,
    )
    try:
        #  Get device certificates
        api_response = api_instance.v1_device_register_post(
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_device_register_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
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
**exp** | str,  | str,  |  | [optional] 
**req_id** | str,  | str,  |  | [optional] 
**hash** | str,  | str,  |  | [optional] 
**auth_factor** | str,  | str,  |  | [optional] 
**csr** | str,  | str,  |  | [optional] 
**serial_number** | str,  | str,  |  | [optional] 
**model** | str,  | str,  |  | [optional] 
**device_friendly_name** | str,  | str,  |  | [optional] 
**ownership** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**architecture** | str,  | str,  |  | [optional] 
**notification_token** | str,  | str,  |  | [optional] 
**mdm_present** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ALTERNATERESPONSE | ALTERNATERESPONSESchema | | optional


# ALTERNATERESPONSESchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

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
200 | [ApiResponseFor200](#v1_device_register_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_device_register_post.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v1_device_register_post.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#v1_device_register_post.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#v1_device_register_post.ApiResponseFor500) | Internal Server Error

#### v1_device_register_post.ApiResponseFor200
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
**[root_ca_certs](#root_ca_certs)** | list, tuple,  | tuple,  |  | [optional] 
**[intermediate_ca_certs](#intermediate_ca_certs)** | list, tuple,  | tuple,  |  | [optional] 
**client_cert** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# root_ca_certs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# intermediate_ca_certs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### v1_device_register_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_device_register_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_device_register_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_device_register_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerRegistrationToken](../../../README.md#bearerRegistrationToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_enduser_facing_app_version_put**
<a name="v1_enduser_facing_app_version_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_enduser_facing_app_version_put(any_type)

 Update enduser device appversion

This endpoint updates appversion of an enduser device.

### Example

* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        app_version="1.0.0",
    )
    try:
        #  Update enduser device appversion
        api_response = api_instance.v1_enduser_facing_app_version_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_enduser_facing_app_version_put: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        'Content-Type': "Content-Type_example",
    }
    body = dict(
        app_version="1.0.0",
    )
    try:
        #  Update enduser device appversion
        api_response = api_instance.v1_enduser_facing_app_version_put(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_enduser_facing_app_version_put: %s\n" % e)
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
**app_version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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
200 | [ApiResponseFor200](#v1_enduser_facing_app_version_put.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v1_enduser_facing_app_version_put.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_enduser_facing_app_version_put.ApiResponseFor500) | Internal Server Error

#### v1_enduser_facing_app_version_put.ApiResponseFor200
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
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_enduser_facing_app_version_put.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_enduser_facing_app_version_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[error](#error)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**request_id** | str,  | str,  |  | [optional] 
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  |  | [optional] 
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_enduser_facing_device_features_post**
<a name="v1_enduser_facing_device_features_post"></a>
> v1_enduser_facing_device_features_post(any_type)

 Submit device features

This endpoint submits device features of an enduser device.

### Example

* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        kind="BanyanDeviceFeatures",
        api_version="ts.banyanops.com/v1",
        metadata=dict(
            email="",
            serialnumber="",
        ),
        spec=dict(
            source="BanyanApp",
            source_type="Banyan",
            running_applications=[
                dict(
                    name="Banyan",
                    version="0.3.1",
                    last_opened_at=1557356315816398000,
                    os_name="Mac OS X",
                    os_version="10.14.4",
                    os_build="18E227",
                    updates_check_enabled=1,
                    updates_download_enabled=1,
                    updates_install_enabled=1,
                    updates_install_system_enabled=1,
                    updates_install_critical_enabled=1,
                    screen_lock_enabled=1,
                    passcode_enabled=1,
                    touchid_enabled=1,
                    faceid_enabled=1,
                    biometric_lock_enabled=1,
                    firewall_enabled=1,
                    disk_encryption_enabled=1,
                    not_jailbroken=1,
                    integration_identities=[
                        dict(
                            integration_id="abcd",
                            device_identity="device-xyz",
                        )
                    ],
                )
            ],
        ),
    )
    try:
        #  Submit device features
        api_response = api_instance.v1_enduser_facing_device_features_post(
            header_params=header_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_enduser_facing_device_features_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        'Content-Type': "Content-Type_example",
    }
    body = dict(
        kind="BanyanDeviceFeatures",
        api_version="ts.banyanops.com/v1",
        metadata=dict(
            email="",
            serialnumber="",
        ),
        spec=dict(
            source="BanyanApp",
            source_type="Banyan",
            running_applications=[
                dict(
                    name="Banyan",
                    version="0.3.1",
                    last_opened_at=1557356315816398000,
                    os_name="Mac OS X",
                    os_version="10.14.4",
                    os_build="18E227",
                    updates_check_enabled=1,
                    updates_download_enabled=1,
                    updates_install_enabled=1,
                    updates_install_system_enabled=1,
                    updates_install_critical_enabled=1,
                    screen_lock_enabled=1,
                    passcode_enabled=1,
                    touchid_enabled=1,
                    faceid_enabled=1,
                    biometric_lock_enabled=1,
                    firewall_enabled=1,
                    disk_encryption_enabled=1,
                    not_jailbroken=1,
                    integration_identities=[
                        dict(
                            integration_id="abcd",
                            device_identity="device-xyz",
                        )
                    ],
                )
            ],
        ),
    )
    try:
        #  Submit device features
        api_response = api_instance.v1_enduser_facing_device_features_post(
            header_params=header_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_enduser_facing_device_features_post: %s\n" % e)
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
**kind** | str,  | str,  |  | [optional] 
**apiVersion** | str,  | str,  |  | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[spec](#spec)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**email** | str,  | str,  |  | [optional] 
**serialnumber** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# spec

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**source** | str,  | str,  |  | [optional] 
**source_type** | str,  | str,  |  | [optional] 
**[running_applications](#running_applications)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# running_applications

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
**name** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**last_opened_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**os_name** | str,  | str,  |  | [optional] 
**os_version** | str,  | str,  |  | [optional] 
**os_build** | str,  | str,  |  | [optional] 
**updates_check_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updates_download_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updates_install_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updates_install_system_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updates_install_critical_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**screen_lock_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**passcode_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**touchid_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**faceid_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**biometric_lock_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**firewall_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**disk_encryption_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**not_jailbroken** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[integration_identities](#integration_identities)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# integration_identities

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
**integration_id** | str,  | str,  |  | [optional] 
**device_identity** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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
200 | [ApiResponseFor200](#v1_enduser_facing_device_features_post.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v1_enduser_facing_device_features_post.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_enduser_facing_device_features_post.ApiResponseFor500) | Internal Server Error

#### v1_enduser_facing_device_features_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_enduser_facing_device_features_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_enduser_facing_device_features_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[error](#error)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**request_id** | str,  | str,  |  | [optional] 
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  |  | [optional] 
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_enduser_facing_devices_get**
<a name="v1_enduser_facing_devices_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] v1_enduser_facing_devices_get()

 List enduser devices

This end point lists all the devices for enduser

### Example

* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    query_params = {
        'active': "active_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  List enduser devices
        api_response = api_instance.v1_enduser_facing_devices_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_enduser_facing_devices_get: %s\n" % e)
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
active | ActiveSchema | | optional


# ActiveSchema

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
200 | [ApiResponseFor200](#v1_enduser_facing_devices_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v1_enduser_facing_devices_get.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_enduser_facing_devices_get.ApiResponseFor500) | Internal Server Error

#### v1_enduser_facing_devices_get.ApiResponseFor200
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
**DeviceID** | str,  | str,  |  | [optional] 
**SerialNumber** | str,  | str,  |  | [optional] 
**DeviceFriendlyName** | str,  | str,  |  | [optional] 
**Ownership** | str,  | str,  |  | [optional] 
**Platform** | str,  | str,  |  | [optional] 
**Model** | str,  | str,  |  | [optional] 
**Architecture** | str,  | str,  |  | [optional] 
**RegisteredStatus** | str,  | str,  |  | [optional] 
**[MdmData](#MdmData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[trust](#trust)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TrustData](#TrustData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[Roles](#Roles)** | list, tuple,  | tuple,  |  | [optional] 
**Banned** | str,  | str,  |  | [optional] 
**OS** | str,  | str,  |  | [optional] 
**AppVersion** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# MdmData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Source** | str,  | str,  |  | [optional] 
**CompromisedStatus** | str,  | str,  |  | [optional] 
**CompliantStatus** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# trust

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**value** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**level** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**[last_evaluated](#last_evaluated)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**expired_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[factors](#factors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# last_evaluated

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**last_evaluated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**last_evaluated_value** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**last_evaluated_level** | str,  | str,  |  | [optional] 
**[last_evaluated_factors](#last_evaluated_factors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# last_evaluated_factors

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
**name** | str,  | str,  |  | [optional] 
**value** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**source** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**[remediation](#remediation)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# remediation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | str,  | str,  |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# factors

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
**name** | str,  | str,  |  | [optional] 
**value** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**source** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**[remediation](#remediation)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# remediation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**description** | str,  | str,  |  | [optional] 
**url** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TrustData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**EntityTrustscore** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**OverrideTrustscore** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AccessTrustscore** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**OverrideActive** | str,  | str,  |  | [optional] 
**Level** | str,  | str,  |  | [optional] 
**UpdatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[Factors](#Factors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Factors

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
**Name** | str,  | str,  |  | [optional] 
**Value** | str,  | str,  |  | [optional] 
**Type** | str,  | str,  |  | [optional] 
**Source** | str,  | str,  |  | [optional] 
**Description** | str,  | str,  |  | [optional] 
**RemediationDescription** | str,  | str,  |  | [optional] 
**RemediationURL** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Roles

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### v1_enduser_facing_devices_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_enduser_facing_devices_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_enduser_facing_org_details_get**
<a name="v1_enduser_facing_org_details_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_enduser_facing_org_details_get()

 Get org details  

This end point returns org details such as the registration client id, trustprovider url, login client id, etc., required for banyan desktop app.

### Example

* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        'Content-Type': "Content-Type_example",
    }
    try:
        #  Get org details  
        api_response = api_instance.v1_enduser_facing_org_details_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_enduser_facing_org_details_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v1_enduser_facing_org_details_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v1_enduser_facing_org_details_get.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#v1_enduser_facing_org_details_get.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#v1_enduser_facing_org_details_get.ApiResponseFor500) | Internal Server Error

#### v1_enduser_facing_org_details_get.ApiResponseFor200
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
**command_center_url** | str,  | str,  |  | [optional] 
**trust_provider_url** | str,  | str,  |  | [optional] 
**registration_trust_provider_url** | str,  | str,  |  | [optional] 
**login_client_id** | str,  | str,  |  | [optional] 
**registration_client_id** | str,  | str,  |  | [optional] 
**reporting_client_id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**org_name** | str,  | str,  |  | [optional] 
**shield_uuid** | str,  | str,  |  | [optional] 
**renewal_client_id** | str,  | str,  |  | [optional] 
**external_client_id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_enduser_facing_org_details_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_enduser_facing_org_details_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_enduser_facing_org_details_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_enduser_facing_services_get**
<a name="v1_enduser_facing_services_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] v1_enduser_facing_services_get()

 List enduser device accessible services

This end point lists all the services which an enduser device can access

### Example

* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  List enduser device accessible services
        api_response = api_instance.v1_enduser_facing_services_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_enduser_facing_services_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v1_enduser_facing_services_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v1_enduser_facing_services_get.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_enduser_facing_services_get.ApiResponseFor500) | Internal Server Error

#### v1_enduser_facing_services_get.ApiResponseFor200
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
**ServiceID** | str,  | str,  |  | [optional] 
**FriendlyName** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Metadata** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_enduser_facing_services_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_enduser_facing_services_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_enduser_facing_set_max_trust_level_post**
<a name="v1_enduser_facing_set_max_trust_level_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_enduser_facing_set_max_trust_level_post(any_type)

Set Max Trust Level

This API enables endusers of test-drive orgs to apply a **override** to Banyan's trust-scoring algorithm, by setting a desired TrustLevel for their device. API only works if the org is in test-drive mode.

### Example

* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        level="AlwaysDeny",
        reason="test",
        ext_source="test",
    )
    try:
        # Set Max Trust Level
        api_response = api_instance.v1_enduser_facing_set_max_trust_level_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_enduser_facing_set_max_trust_level_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    body = dict(
        level="AlwaysDeny",
        reason="test",
        ext_source="test",
    )
    try:
        # Set Max Trust Level
        api_response = api_instance.v1_enduser_facing_set_max_trust_level_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_enduser_facing_set_max_trust_level_post: %s\n" % e)
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
**Level** | str,  | str,  |  | [optional] 
**Reason** | str,  | str,  |  | [optional] 
**ExtSource** | str,  | str,  |  | [optional] 
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
200 | [ApiResponseFor200](#v1_enduser_facing_set_max_trust_level_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_enduser_facing_set_max_trust_level_post.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v1_enduser_facing_set_max_trust_level_post.ApiResponseFor500) | Internal Server Error

#### v1_enduser_facing_set_max_trust_level_post.ApiResponseFor200
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
**TrustType** | str,  | str,  |  | [optional] 
**TrustID** | str,  | str,  |  | [optional] 
**Score** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Level** | str,  | str,  |  | [optional] 
**Reason** | str,  | str,  |  | [optional] 
**ExtSource** | str,  | str,  |  | [optional] 
**FactorsJSON** | str,  | str,  |  | [optional] 
**CreatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeletedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**LastUpdatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_enduser_facing_set_max_trust_level_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_enduser_facing_set_max_trust_level_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_enduser_facing_trustscores_get**
<a name="v1_enduser_facing_trustscores_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_enduser_facing_trustscores_get()

 List enduser device trustscores

This endpoint lists the trustscores of an enduser device

### Example

* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  List enduser device trustscores
        api_response = api_instance.v1_enduser_facing_trustscores_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_enduser_facing_trustscores_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v1_enduser_facing_trustscores_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v1_enduser_facing_trustscores_get.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_enduser_facing_trustscores_get.ApiResponseFor500) | Internal Server Error

#### v1_enduser_facing_trustscores_get.ApiResponseFor200
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
**EntityTrustscore** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**OverrideTrustscore** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AccessTrustscore** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**OverrideActive** | str,  | str,  |  | [optional] 
**Level** | str,  | str,  |  | [optional] 
**UpdatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[Factors](#Factors)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Factors

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
**Name** | str,  | str,  |  | [optional] 
**Value** | str,  | str,  |  | [optional] 
**Type** | str,  | str,  |  | [optional] 
**Source** | str,  | str,  |  | [optional] 
**Description** | str,  | str,  |  | [optional] 
**[Remediation](#Remediation)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Remediation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[Windows](#Windows)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[MacOS](#MacOS)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[Linux](#Linux)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Windows

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Description** | str,  | str,  |  | [optional] 
**URL** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# MacOS

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Description** | str,  | str,  |  | [optional] 
**URL** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Linux

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Description** | str,  | str,  |  | [optional] 
**URL** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_enduser_facing_trustscores_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_enduser_facing_trustscores_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_set_max_trust_level_post**
<a name="v1_set_max_trust_level_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_set_max_trust_level_post(any_type)

 Set Max Trust Level

Banyan's algorithms calculate a TrustScore (0 to 100) and convert it to a human-readable TrustLevel (AlwaysDeny, Low, Medium, High, AlwaysAllow) for every access based on User, Device and Application context. This API enables Admins to apply a **negative override** to Banyan's scoring algorithm, by setting a maximum possible TrustLevel for any given User or Device.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    header_params = {
    }
    body = dict(
        level="AlwaysDeny",
        reason="Known malware MWS-2019-9842 detected on device - quarantine action taken.",
        ext_source="CarbonBlack",
    )
    try:
        #  Set Max Trust Level
        api_response = api_instance.v1_set_max_trust_level_post(
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_set_max_trust_level_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'Email': "Email_example",
        'SerialNumber': "SerialNumber_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    body = dict(
        level="AlwaysDeny",
        reason="Known malware MWS-2019-9842 detected on device - quarantine action taken.",
        ext_source="CarbonBlack",
    )
    try:
        #  Set Max Trust Level
        api_response = api_instance.v1_set_max_trust_level_post(
            query_params=query_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v1_set_max_trust_level_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
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
**Level** | str,  | str,  |  | [optional] 
**Reason** | str,  | str,  |  | [optional] 
**ExtSource** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Email | EmailSchema | | optional
SerialNumber | SerialNumberSchema | | optional


# EmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SerialNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#v1_set_max_trust_level_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_set_max_trust_level_post.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v1_set_max_trust_level_post.ApiResponseFor500) | Internal Server Error

#### v1_set_max_trust_level_post.ApiResponseFor200
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
**TrustType** | str,  | str,  |  | [optional] 
**TrustID** | str,  | str,  |  | [optional] 
**Score** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Level** | str,  | str,  |  | [optional] 
**Reason** | str,  | str,  |  | [optional] 
**ExtSource** | str,  | str,  |  | [optional] 
**FactorsJSON** | str,  | str,  |  | [optional] 
**CreatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeletedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**LastUpdatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_set_max_trust_level_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_set_max_trust_level_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_cert_request_device_only_registration_post**
<a name="v2_cert_request_device_only_registration_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_cert_request_device_only_registration_post()

 POST to get different types of certificates

Request a certificate

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        cert_operation="issue || refresh",
        csr="",
        extra_details=dict(
            org_id="sjdksdsldlsdss",
            mdm_deploy_key="foo",
            mdm_vendor_name="xyz",
            mdm_present=True,
            mdm_vendor_udid="abcdr",
            serial_number="1235",
            model="",
            csr="",
            ownership="",
            platform="",
            os="",
            architecture="",
            device_friendly_name="",
            app_version="1.10.0",
        ),
    )
    try:
        #  POST to get different types of certificates
        api_response = api_instance.v2_cert_request_device_only_registration_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_cert_request_device_only_registration_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
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
**cert_operation** | str,  | str,  |  | [optional] 
**csr** | str,  | str,  |  | [optional] 
**[extra_details](#extra_details)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# extra_details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**org_id** | str,  | str,  |  | [optional] 
**mdm_deploy_key** | str,  | str,  |  | [optional] 
**mdm_vendor_name** | str,  | str,  |  | [optional] 
**mdm_present** | bool,  | BoolClass,  |  | [optional] 
**mdm_vendor_udid** | str,  | str,  |  | [optional] 
**serial_number** | str,  | str,  |  | [optional] 
**model** | str,  | str,  |  | [optional] 
**csr** | str,  | str,  |  | [optional] 
**ownership** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**os** | str,  | str,  |  | [optional] 
**architecture** | str,  | str,  |  | [optional] 
**device_friendly_name** | str,  | str,  |  | [optional] 
**app_version** | str,  | str,  |  | [optional] 
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
200 | [ApiResponseFor200](#v2_cert_request_device_only_registration_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_cert_request_device_only_registration_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_cert_request_device_only_registration_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_cert_request_device_only_registration_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_cert_request_device_only_registration_post.ApiResponseFor500) | Internal Server Error

#### v2_cert_request_device_only_registration_post.ApiResponseFor200
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
**root_ca_certs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**intermediate_ca_certs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**client_cert** | str,  | str,  |  | [optional] 
**client_cert_password** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_cert_request_device_only_registration_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_cert_request_device_only_registration_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_cert_request_device_only_registration_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_cert_request_device_only_registration_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_client_certificate_get**
<a name="v2_client_certificate_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_client_certificate_get()

 GET client certificate details

Get the details of client certificate

### Example

* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET client certificate details
        api_response = api_instance.v2_client_certificate_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_client_certificate_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v2_client_certificate_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_client_certificate_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_client_certificate_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_client_certificate_get.ApiResponseFor500) | Internal Server Error

#### v2_client_certificate_get.ApiResponseFor200
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
**id** | str,  | str,  |  | [optional] 
**device_serialnumber** | str,  | str,  |  | [optional] 
**email** | str,  | str,  |  | [optional] 
**certificate_serialnumber** | str,  | str,  |  | [optional] 
**expiry** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**revoked_status** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_client_certificate_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_client_certificate_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_client_certificate_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_autorun_service_get**
<a name="v2_enduser_facing_autorun_service_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_autorun_service_get()

 GET autorun services

Get the autorun services for a user

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        '&#x60;ContentType': "`ContentType_example",
    }
    try:
        #  GET autorun services
        api_response = api_instance.v2_enduser_facing_autorun_service_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_autorun_service_get: %s\n" % e)
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
&#x60;ContentType | ContentTypeSchema | | optional

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
200 | [ApiResponseFor200](#v2_enduser_facing_autorun_service_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_enduser_facing_autorun_service_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_autorun_service_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_autorun_service_get.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_autorun_service_get.ApiResponseFor200
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
**[autorun_services](#autorun_services)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# autorun_services

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
**service_id** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_autorun_service_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_autorun_service_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_autorun_service_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_autorun_service_service_id_delete**
<a name="v2_enduser_facing_autorun_service_service_id_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_autorun_service_service_id_delete(service_id)

 DELETE to remove a service from a user's autorun list

Remove a service from a user's autorun service list

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    header_params = {
    }
    try:
        #  DELETE to remove a service from a user's autorun list
        api_response = api_instance.v2_enduser_facing_autorun_service_service_id_delete(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_autorun_service_service_id_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  DELETE to remove a service from a user's autorun list
        api_response = api_instance.v2_enduser_facing_autorun_service_service_id_delete(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_autorun_service_service_id_delete: %s\n" % e)
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

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service_id | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_enduser_facing_autorun_service_service_id_delete.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_enduser_facing_autorun_service_service_id_delete.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_enduser_facing_autorun_service_service_id_delete.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_autorun_service_service_id_delete.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_autorun_service_service_id_delete.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_autorun_service_service_id_delete.ApiResponseFor200
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
**data** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_autorun_service_service_id_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_autorun_service_service_id_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_autorun_service_service_id_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_autorun_service_service_id_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_autorun_service_service_id_post**
<a name="v2_enduser_facing_autorun_service_service_id_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_autorun_service_service_id_post(service_id)

 POST to create a autorun service

Create a new autorun service

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    header_params = {
    }
    try:
        #  POST to create a autorun service
        api_response = api_instance.v2_enduser_facing_autorun_service_service_id_post(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_autorun_service_service_id_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  POST to create a autorun service
        api_response = api_instance.v2_enduser_facing_autorun_service_service_id_post(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_autorun_service_service_id_post: %s\n" % e)
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

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service_id | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_enduser_facing_autorun_service_service_id_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_enduser_facing_autorun_service_service_id_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_enduser_facing_autorun_service_service_id_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_autorun_service_service_id_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_autorun_service_service_id_post.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_autorun_service_service_id_post.ApiResponseFor200
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
**[autorun_services](#autorun_services)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# autorun_services

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
**service_id** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_autorun_service_service_id_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_autorun_service_service_id_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_autorun_service_service_id_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_autorun_service_service_id_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_bundle_bundle_id_put**
<a name="v2_enduser_facing_bundle_bundle_id_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_bundle_bundle_id_put(bundle_idany_type)

 Update an existing service bundle

Updates an existing service bundle.

### Example

* Bearer (JWT) Authentication (bearerLoginToken):
* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerLoginToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundle_id': "bundle_id_example",
    }
    header_params = {
    }
    body = dict(
        bundle_name="new bundle name",
        description="new description",
        service_ids="['1', '2', '3']",
        bulk_connect=False,
    )
    try:
        #  Update an existing service bundle
        api_response = api_instance.v2_enduser_facing_bundle_bundle_id_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_bundle_bundle_id_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'bundle_id': "bundle_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        bundle_name="new bundle name",
        description="new description",
        service_ids="['1', '2', '3']",
        bulk_connect=False,
    )
    try:
        #  Update an existing service bundle
        api_response = api_instance.v2_enduser_facing_bundle_bundle_id_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_bundle_bundle_id_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
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
**bundle_name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**service_ids** | str,  | str,  |  | [optional] 
**bulk_connect** | bool,  | BoolClass,  |  | [optional] 
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
bundle_id | BundleIdSchema | | 

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_enduser_facing_bundle_bundle_id_put.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_enduser_facing_bundle_bundle_id_put.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_enduser_facing_bundle_bundle_id_put.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_bundle_bundle_id_put.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_bundle_bundle_id_put.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_bundle_bundle_id_put.ApiResponseFor200
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
**id** | str,  | str,  |  | [optional] 
**bundle_name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**is_admin_created** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**bulk_connect** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**service_ids** | str,  | str,  |  | [optional] 
**created_by_user_id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_bundle_bundle_id_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_bundle_bundle_id_put.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_bundle_bundle_id_put.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_bundle_bundle_id_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerLoginToken](../../../README.md#bearerLoginToken), [bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_bundle_bundle_id_service_post**
<a name="v2_enduser_facing_bundle_bundle_id_service_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_bundle_bundle_id_service_post(bundle_idany_type)

 Create a service bundle

add one service to a bundle.

### Example

* Bearer (JWT) Authentication (bearerLoginToken):
* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerLoginToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'bundle_id': "bundle_id_example",
    }
    header_params = {
    }
    body = dict(
        service_id="my-react-app2.deepakorg-shield.bnn",
    )
    try:
        #  Create a service bundle
        api_response = api_instance.v2_enduser_facing_bundle_bundle_id_service_post(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_bundle_bundle_id_service_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'bundle_id': "bundle_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        service_id="my-react-app2.deepakorg-shield.bnn",
    )
    try:
        #  Create a service bundle
        api_response = api_instance.v2_enduser_facing_bundle_bundle_id_service_post(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_bundle_bundle_id_service_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
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
**service_id** | str,  | str,  |  | [optional] 
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
bundle_id | BundleIdSchema | | 

# BundleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_enduser_facing_bundle_bundle_id_service_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_enduser_facing_bundle_bundle_id_service_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_enduser_facing_bundle_bundle_id_service_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_bundle_bundle_id_service_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_bundle_bundle_id_service_post.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_bundle_bundle_id_service_post.ApiResponseFor200
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
**id** | str,  | str,  |  | [optional] 
**bundle_name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**is_admin_created** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**bulk_connect** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[service_ids](#service_ids)** | list, tuple,  | tuple,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_by_user_id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# service_ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### v2_enduser_facing_bundle_bundle_id_service_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_bundle_bundle_id_service_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_bundle_bundle_id_service_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_bundle_bundle_id_service_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerLoginToken](../../../README.md#bearerLoginToken), [bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_bundle_get**
<a name="v2_enduser_facing_bundle_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_bundle_get()

 GET service bundles

Get the service bundles in an Org

### Example

* Bearer (JWT) Authentication (bearerLoginToken):
* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerLoginToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    query_params = {
        'bundle_name': "bundle_name_example",
        'id': "id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET service bundles
        api_response = api_instance.v2_enduser_facing_bundle_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_bundle_get: %s\n" % e)
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
bundle_name | BundleNameSchema | | optional
id | IdSchema | | optional


# BundleNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

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
200 | [ApiResponseFor200](#v2_enduser_facing_bundle_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_enduser_facing_bundle_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_bundle_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_bundle_get.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_bundle_get.ApiResponseFor200
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
**[service_bundles](#service_bundles)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# service_bundles

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
**bundle_name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**is_admin_created** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**bulk_connect** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**service_ids** | str,  | str,  |  | [optional] 
**created_by_user_id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_bundle_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_bundle_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_bundle_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerLoginToken](../../../README.md#bearerLoginToken), [bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_bundle_post**
<a name="v2_enduser_facing_bundle_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_bundle_post(any_type)

 create a service bundle

create a service bundle

### Example

* Bearer (JWT) Authentication (bearerLoginToken):
* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerLoginToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        bundle_name="bundle 2",
        description="adding a bundle",
        service_ids="[\"my-react-app.deepakorg-shield.bnn\"]",
        bulk_connect=True,
    )
    try:
        #  create a service bundle
        api_response = api_instance.v2_enduser_facing_bundle_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_bundle_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        bundle_name="bundle 2",
        description="adding a bundle",
        service_ids="[\"my-react-app.deepakorg-shield.bnn\"]",
        bulk_connect=True,
    )
    try:
        #  create a service bundle
        api_response = api_instance.v2_enduser_facing_bundle_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_bundle_post: %s\n" % e)
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
**bundle_name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**service_ids** | str,  | str,  |  | [optional] 
**bulk_connect** | bool,  | BoolClass,  |  | [optional] 
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
200 | [ApiResponseFor200](#v2_enduser_facing_bundle_post.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_enduser_facing_bundle_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_bundle_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_bundle_post.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_bundle_post.ApiResponseFor200
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
**[service_bundles](#service_bundles)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# service_bundles

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
**bundle_name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**is_admin_created** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**bulk_connect** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**service_ids** | str,  | str,  |  | [optional] 
**created_by_user_id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_bundle_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_bundle_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_bundle_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerLoginToken](../../../README.md#bearerLoginToken), [bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_client_cert_issue_post**
<a name="v2_enduser_facing_client_cert_issue_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_client_cert_issue_post(any_type)

 issue client certificate

This endpoint issues a client certificate if 1) user has a staged certificate.2) user's certificate expires in given threshold (this is determined by value of    auto_renew_cert_expiry_window_days in org table)

### Example

* Bearer (JWT) Authentication (bearerLoginToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerLoginToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICuDCCAaACAQAwPjETMBEGA1\n-----END CERTIFICATE REQUEST-----\n",
        serialnumber="VVF3232DADSK9",
    )
    try:
        #  issue client certificate
        api_response = api_instance.v2_enduser_facing_client_cert_issue_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_client_cert_issue_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        '1. Authorization': "1. Authorization_example",
    }
    body = dict(
        csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICuDCCAaACAQAwPjETMBEGA1\n-----END CERTIFICATE REQUEST-----\n",
        serialnumber="VVF3232DADSK9",
    )
    try:
        #  issue client certificate
        api_response = api_instance.v2_enduser_facing_client_cert_issue_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_client_cert_issue_post: %s\n" % e)
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
**csr** | str,  | str,  |  | [optional] 
**serialnumber** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
1. Authorization | Model1AuthorizationSchema | | optional

# Model1AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_enduser_facing_client_cert_issue_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_enduser_facing_client_cert_issue_post.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v2_enduser_facing_client_cert_issue_post.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v2_enduser_facing_client_cert_issue_post.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_client_cert_issue_post.ApiResponseFor200
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
**client_cert** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_client_cert_issue_post.ApiResponseFor400
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

#### v2_enduser_facing_client_cert_issue_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_client_cert_issue_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerLoginToken](../../../README.md#bearerLoginToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_favorite_service_get**
<a name="v2_enduser_facing_favorite_service_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_favorite_service_get()

 GET favorite services

Get the favorite services for a user

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET favorite services
        api_response = api_instance.v2_enduser_facing_favorite_service_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_favorite_service_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v2_enduser_facing_favorite_service_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_enduser_facing_favorite_service_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_favorite_service_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_favorite_service_get.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_favorite_service_get.ApiResponseFor200
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
**[favorites](#favorites)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# favorites

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
**service_id** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_favorite_service_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_favorite_service_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_favorite_service_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_favorite_service_service_id_delete**
<a name="v2_enduser_facing_favorite_service_service_id_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_favorite_service_service_id_delete(service_idbody)

 DELETE to remove a service from a user's favorite list

Remove a service from a user's favorite list

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    header_params = {
    }
    body = dict()
    try:
        #  DELETE to remove a service from a user's favorite list
        api_response = api_instance.v2_enduser_facing_favorite_service_service_id_delete(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_favorite_service_service_id_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict()
    try:
        #  DELETE to remove a service from a user's favorite list
        api_response = api_instance.v2_enduser_facing_favorite_service_service_id_delete(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_favorite_service_service_id_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service_id | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_enduser_facing_favorite_service_service_id_delete.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_enduser_facing_favorite_service_service_id_delete.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_enduser_facing_favorite_service_service_id_delete.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_favorite_service_service_id_delete.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_favorite_service_service_id_delete.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_favorite_service_service_id_delete.ApiResponseFor200
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
**data** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_favorite_service_service_id_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_favorite_service_service_id_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_favorite_service_service_id_delete.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_favorite_service_service_id_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_favorite_service_service_id_post**
<a name="v2_enduser_facing_favorite_service_service_id_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_favorite_service_service_id_post(service_idbody)

 POST to create a favorite service

Create a new favorite service

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'service_id': "service_id_example",
    }
    header_params = {
    }
    body = dict()
    try:
        #  POST to create a favorite service
        api_response = api_instance.v2_enduser_facing_favorite_service_service_id_post(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_favorite_service_service_id_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'service_id': "service_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict()
    try:
        #  POST to create a favorite service
        api_response = api_instance.v2_enduser_facing_favorite_service_service_id_post(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_favorite_service_service_id_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
service_id | ServiceIdSchema | | 

# ServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_enduser_facing_favorite_service_service_id_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_enduser_facing_favorite_service_service_id_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_enduser_facing_favorite_service_service_id_post.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_favorite_service_service_id_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_favorite_service_service_id_post.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_favorite_service_service_id_post.ApiResponseFor200
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
**[favorites](#favorites)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# favorites

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
**service_id** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_favorite_service_service_id_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_favorite_service_service_id_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_favorite_service_service_id_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_favorite_service_service_id_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_integration_device_identity_command_get**
<a name="v2_enduser_facing_integration_device_identity_command_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_integration_device_identity_command_get()

 GET integration device-identity commands

Update the details of an integration device identity commands for all active integrations or a specific integration

### Example

* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    query_params = {
        'integration_id': "integration_id_example",
        'platform': "platform_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET integration device-identity commands
        api_response = api_instance.v2_enduser_facing_integration_device_identity_command_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_integration_device_identity_command_get: %s\n" % e)
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
integration_id | IntegrationIdSchema | | optional
platform | PlatformSchema | | optional


# IntegrationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PlatformSchema

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
200 | [ApiResponseFor200](#v2_enduser_facing_integration_device_identity_command_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_enduser_facing_integration_device_identity_command_get.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_enduser_facing_integration_device_identity_command_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_integration_device_identity_command_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_integration_device_identity_command_get.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_integration_device_identity_command_get.ApiResponseFor200
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
**id** | str,  | str,  |  | [optional] 
**org_id** | str,  | str,  |  | [optional] 
**integration_id** | str,  | str,  |  | [optional] 
**platform** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**partner** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_integration_device_identity_command_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_integration_device_identity_command_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_integration_device_identity_command_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_integration_device_identity_command_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_login_services_get**
<a name="v2_enduser_facing_login_services_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_login_services_get()

 GET to return the list of services visible using a login token

Get the list of services

### Example

* Bearer (JWT) Authentication (bearerLoginToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerLoginToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET to return the list of services visible using a login token
        api_response = api_instance.v2_enduser_facing_login_services_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_login_services_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v2_enduser_facing_login_services_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_enduser_facing_login_services_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_login_services_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_login_services_get.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_login_services_get.ApiResponseFor200
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
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**[Metadata](#Metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Metadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**cluster** | str,  | str,  |  | [optional] 
**[tags](#tags)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**template** | str,  | str,  |  | [optional] 
**user_facing** | str,  | str,  |  | [optional] 
**protocol** | str,  | str,  |  | [optional] 
**domain** | str,  | str,  |  | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**icon** | str,  | str,  |  | [optional] 
**service_app_type** | str,  | str,  |  | [optional] 
**banyanproxy_mode** | str,  | str,  |  | [optional] 
**app_listen_port** | str,  | str,  |  | [optional] 
**allow_user_override** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**kube_cluster_name** | str,  | str,  |  | [optional] 
**kube_ca_key** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_login_services_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_login_services_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_login_services_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerLoginToken](../../../README.md#bearerLoginToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_logs_post**
<a name="v2_enduser_facing_logs_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_logs_post()

Get the url to upload app logs

Get the url to upload app logs at specific location

### Example

* Bearer (JWT) Authentication (bearerLoginToken):
* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerLoginToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Get the url to upload app logs
        api_response = api_instance.v2_enduser_facing_logs_post(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_logs_post: %s\n" % e)
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
200 | [ApiResponseFor200](#v2_enduser_facing_logs_post.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_enduser_facing_logs_post.ApiResponseFor401) | Unauthorized error
403 | [ApiResponseFor403](#v2_enduser_facing_logs_post.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_enduser_facing_logs_post.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_logs_post.ApiResponseFor200
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
**url_to_upload** | str,  | str,  |  | [optional] 
**key** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_logs_post.ApiResponseFor401
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
**[error](#error)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**request_id** | str,  | str,  |  | [optional] 
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  |  | [optional] 
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_logs_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_logs_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[error](#error)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**request_id** | str,  | str,  |  | [optional] 
**Message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# error

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  |  | [optional] 
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[bearerLoginToken](../../../README.md#bearerLoginToken), [bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_org_support_get**
<a name="v2_enduser_facing_org_support_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_org_support_get()

Get org support info

To get the Org support info for given org.

### Example

* Bearer (JWT) Authentication (bearerLoginToken):
* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerLoginToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get org support info
        api_response = api_instance.v2_enduser_facing_org_support_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_org_support_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_enduser_facing_org_support_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_enduser_facing_org_support_get.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_enduser_facing_org_support_get.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_org_support_get.ApiResponseFor200
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
**[service_tunnels](#service_tunnels)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# service_tunnels

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
**support_message** | str,  | str,  |  | [optional] 
**support_link_title** | str,  | str,  |  | [optional] 
**support_link_url** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_org_support_get.ApiResponseFor401
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

#### v2_enduser_facing_org_support_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerLoginToken](../../../README.md#bearerLoginToken), [bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_service_tunnel_get**
<a name="v2_enduser_facing_service_tunnel_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_service_tunnel_get()

 Get service tunnel config 

To get the list of service tunnels for an org.

### Example

* Bearer (JWT) Authentication (bearerLoginToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerLoginToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Get service tunnel config 
        api_response = api_instance.v2_enduser_facing_service_tunnel_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_service_tunnel_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v2_enduser_facing_service_tunnel_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_enduser_facing_service_tunnel_get.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_enduser_facing_service_tunnel_get.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_service_tunnel_get.ApiResponseFor200
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
**[service_tunnels](#service_tunnels)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# service_tunnels

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
**org_id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**friendly_name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**description_link** | str,  | str,  |  | [optional] 
**icon** | str,  | str,  |  | [optional] 
**cidrs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_enduser_facing_service_tunnel_get.ApiResponseFor401
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

#### v2_enduser_facing_service_tunnel_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerLoginToken](../../../README.md#bearerLoginToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_tunnel_config_get**
<a name="v2_enduser_facing_tunnel_config_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_tunnel_config_get()

 Get enduser_device tunnel config 

To get the enduser_device tunnel config for an enduser_device pair.

### Example

* Bearer (JWT) Authentication (bearerLoginToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerLoginToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    query_params = {
        'service_tunnel_id': "service_tunnel_id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Get enduser_device tunnel config 
        api_response = api_instance.v2_enduser_facing_tunnel_config_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_tunnel_config_get: %s\n" % e)
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
service_tunnel_id | ServiceTunnelIdSchema | | optional


# ServiceTunnelIdSchema

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
200 | [ApiResponseFor200](#v2_enduser_facing_tunnel_config_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_enduser_facing_tunnel_config_get.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_enduser_facing_tunnel_config_get.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_tunnel_config_get.ApiResponseFor200
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
**local_ip_address** | str,  | str,  |  | [optional] 
**[access_tiers](#access_tiers)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# access_tiers

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
**org_id** | str,  | str,  |  | [optional] 
**access_tier_id** | str,  | str,  |  | [optional] 
**dns_search_domains** | str,  | str,  |  | [optional] 
**udp_port_number** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tunnel_ip_address** | str,  | str,  |  | [optional] 
**[cidrs](#cidrs)** | list, tuple,  | tuple,  |  | [optional] 
**wireguard_public_key** | str,  | str,  |  | [optional] 
**keepalive** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[domains](#domains)** | list, tuple,  | tuple,  |  | [optional] 
**dns_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**cname** | str,  | str,  |  | [optional] 
**site_name** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cidrs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# domains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### v2_enduser_facing_tunnel_config_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_tunnel_config_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerLoginToken](../../../README.md#bearerLoginToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_enduser_facing_tunnel_config_post**
<a name="v2_enduser_facing_tunnel_config_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_enduser_facing_tunnel_config_post()

 Save enduser_device tunnel config information for an organization

To save the enduser_device tunnel config information for an organization.

### Example

* Bearer (JWT) Authentication (bearerLoginToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerLoginToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Save enduser_device tunnel config information for an organization
        api_response = api_instance.v2_enduser_facing_tunnel_config_post(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_enduser_facing_tunnel_config_post: %s\n" % e)
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
200 | [ApiResponseFor200](#v2_enduser_facing_tunnel_config_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_enduser_facing_tunnel_config_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_enduser_facing_tunnel_config_post.ApiResponseFor401) | Status unauthorized
403 | [ApiResponseFor403](#v2_enduser_facing_tunnel_config_post.ApiResponseFor403) | Status unauthorized
500 | [ApiResponseFor500](#v2_enduser_facing_tunnel_config_post.ApiResponseFor500) | Internal Server Error

#### v2_enduser_facing_tunnel_config_post.ApiResponseFor200
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
**local_ip_address** | str,  | str,  |  | [optional] 
**[access_tiers](#access_tiers)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# access_tiers

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
**org_id** | str,  | str,  |  | [optional] 
**site_name** | str,  | str,  |  | [optional] 
**cname** | str,  | str,  |  | [optional] 
**dns_search_domains** | str,  | str,  |  | [optional] 
**udp_port_number** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tunnel_ip_address** | str,  | str,  |  | [optional] 
**[cidrs](#cidrs)** | list, tuple,  | tuple,  |  | [optional] 
**wireguard_public_key** | str,  | str,  |  | [optional] 
**keepalive** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[domains](#domains)** | list, tuple,  | tuple,  |  | [optional] 
**dns_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tunnel_peer_type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cidrs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# domains

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### v2_enduser_facing_tunnel_config_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_tunnel_config_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_tunnel_config_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_enduser_facing_tunnel_config_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerLoginToken](../../../README.md#bearerLoginToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_staged_device_cert_password_get**
<a name="v2_staged_device_cert_password_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_staged_device_cert_password_get()

 GET to return the password needed to unlock a staged device cert

Get the password needed to unlock the device cert

### Example

* Bearer (JWT) Authentication (bearerReportingToken):
```python
import openapi_client
from openapi_client.apis.tags import enduser_facing_api
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

# Configure Bearer authorization (JWT): bearerReportingToken
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enduser_facing_api.EnduserFacingApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  GET to return the password needed to unlock a staged device cert
        api_response = api_instance.v2_staged_device_cert_password_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling EnduserFacingApi->v2_staged_device_cert_password_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v2_staged_device_cert_password_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_staged_device_cert_password_get.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#v2_staged_device_cert_password_get.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#v2_staged_device_cert_password_get.ApiResponseFor500) | Internal Server Error

#### v2_staged_device_cert_password_get.ApiResponseFor200
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
**cert_password** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_staged_device_cert_password_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_staged_device_cert_password_get.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_staged_device_cert_password_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerReportingToken](../../../README.md#bearerReportingToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

