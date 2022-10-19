<a name="__pageTop"></a>
# openapi_client.apis.tags.registered_service_api.RegisteredServiceApi

All URIs are relative to *https://dev02.console.bnntest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_delete_registered_service_delete**](#v1_delete_registered_service_delete) | **delete** /v1/delete_registered_service |  Delete a service
[**v1_disable_registered_service_post**](#v1_disable_registered_service_post) | **post** /v1/disable_registered_service | Disable a registered service
[**v1_enable_registered_service_post**](#v1_enable_registered_service_post) | **post** /v1/enable_registered_service | Enable a registered service
[**v1_insert_default_registered_services_post**](#v1_insert_default_registered_services_post) | **post** /v1/insert_default_registered_services |  Create default registered service
[**v1_insert_registered_service_post**](#v1_insert_registered_service_post) | **post** /v1/insert_registered_service |  Create a new service or update an existing service
[**v1_registered_services_get**](#v1_registered_services_get) | **get** /v1/registered_services |  List services
[**v1_service_connection_test_post**](#v1_service_connection_test_post) | **post** /v1/service_connection_test |  POST to start the service connection test
[**v1_services_stats_get**](#v1_services_stats_get) | **get** /v1/services/stats |  Get the services statistics for an org
[**v2_access_tier_id_registered_services_get**](#v2_access_tier_id_registered_services_get) | **get** /v2/access_tier/{id}/registered_services |  List registered services attached to Access Tier for an organization

# **v1_delete_registered_service_delete**
<a name="v1_delete_registered_service_delete"></a>
> v1_delete_registered_service_delete()

 Delete a service

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import registered_service_api
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
    api_instance = registered_service_api.RegisteredServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'ServiceID': "ServiceID_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Delete a service
        api_response = api_instance.v1_delete_registered_service_delete(
            query_params=query_params,
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling RegisteredServiceApi->v1_delete_registered_service_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ServiceID | ServiceIDSchema | | optional


# ServiceIDSchema

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
200 | [ApiResponseFor200](#v1_delete_registered_service_delete.ApiResponseFor200) | OK

#### v1_delete_registered_service_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_disable_registered_service_post**
<a name="v1_disable_registered_service_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_disable_registered_service_post()

Disable a registered service

This endpoint disables a registered service and then sends the notification to all Shields of its Organization.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import registered_service_api
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
    api_instance = registered_service_api.RegisteredServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'ServiceID': "ServiceID_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Disable a registered service
        api_response = api_instance.v1_disable_registered_service_post(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegisteredServiceApi->v1_disable_registered_service_post: %s\n" % e)
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
ServiceID | ServiceIDSchema | | optional


# ServiceIDSchema

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
200 | [ApiResponseFor200](#v1_disable_registered_service_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_disable_registered_service_post.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v1_disable_registered_service_post.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_disable_registered_service_post.ApiResponseFor500) | Internal Server Error

#### v1_disable_registered_service_post.ApiResponseFor200
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

#### v1_disable_registered_service_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_disable_registered_service_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_disable_registered_service_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_enable_registered_service_post**
<a name="v1_enable_registered_service_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_enable_registered_service_post()

Enable a registered service

Enables a registered service and then sends the notification to all Shields of its Organization

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import registered_service_api
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
    api_instance = registered_service_api.RegisteredServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'ServiceID': "ServiceID_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        # Enable a registered service
        api_response = api_instance.v1_enable_registered_service_post(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegisteredServiceApi->v1_enable_registered_service_post: %s\n" % e)
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
ServiceID | ServiceIDSchema | | optional


# ServiceIDSchema

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
200 | [ApiResponseFor200](#v1_enable_registered_service_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_enable_registered_service_post.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v1_enable_registered_service_post.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_enable_registered_service_post.ApiResponseFor500) | Internal Server Error

#### v1_enable_registered_service_post.ApiResponseFor200
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

#### v1_enable_registered_service_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_enable_registered_service_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_enable_registered_service_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_insert_default_registered_services_post**
<a name="v1_insert_default_registered_services_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_insert_default_registered_services_post()

 Create default registered service

This endpoint creates 3 default registered services if they do not exist, for:1. Device Registration, called `deviceregistrationservice`2. App Login, called `loginservice`3. Device Factor Reporting, called `reportingservice`

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import registered_service_api
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
    api_instance = registered_service_api.RegisteredServiceApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Create default registered service
        api_response = api_instance.v1_insert_default_registered_services_post(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegisteredServiceApi->v1_insert_default_registered_services_post: %s\n" % e)
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
200 | [ApiResponseFor200](#v1_insert_default_registered_services_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_insert_default_registered_services_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v1_insert_default_registered_services_post.ApiResponseFor401) | Forbidden
404 | [ApiResponseFor404](#v1_insert_default_registered_services_post.ApiResponseFor404) | NotFound (org not found)
409 | [ApiResponseFor409](#v1_insert_default_registered_services_post.ApiResponseFor409) | Conflict (default service already exists)
422 | [ApiResponseFor422](#v1_insert_default_registered_services_post.ApiResponseFor422) | Unprocessable (Org NoVPN !&#x3D; ENABLED)
500 | [ApiResponseFor500](#v1_insert_default_registered_services_post.ApiResponseFor500) | Internal Server Error

#### v1_insert_default_registered_services_post.ApiResponseFor200
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

#### v1_insert_default_registered_services_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_insert_default_registered_services_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_insert_default_registered_services_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_insert_default_registered_services_post.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_insert_default_registered_services_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_insert_default_registered_services_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_insert_registered_service_post**
<a name="v1_insert_registered_service_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_insert_registered_service_post()

 Create a new service or update an existing service

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import registered_service_api
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
    api_instance = registered_service_api.RegisteredServiceApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  Create a new service or update an existing service
        api_response = api_instance.v1_insert_registered_service_post(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegisteredServiceApi->v1_insert_registered_service_post: %s\n" % e)
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
200 | [ApiResponseFor200](#v1_insert_registered_service_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_insert_registered_service_post.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v1_insert_registered_service_post.ApiResponseFor500) | Internal Server Error

#### v1_insert_registered_service_post.ApiResponseFor200
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
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**FriendlyName** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**ServiceDiscovery** | str,  | str,  |  | [optional] 
**ServiceVersion** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Description** | str,  | str,  |  | [optional] 
**CreatedBy** | str,  | str,  |  | [optional] 
**CreatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**LastUpdatedBy** | str,  | str,  |  | [optional] 
**LastUpdatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeletedBy** | str,  | str,  |  | [optional] 
**DeletedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**External** | str,  | str,  |  | [optional] 
**OIDCEnabled** | str,  | str,  |  | [optional] 
**OIDCClientSpec** | str,  | str,  |  | [optional] 
**ServiceSpec** | str,  | str,  |  | [optional] 
**UserFacing** | str,  | str,  |  | [optional] 
**Protocol** | str,  | str,  |  | [optional] 
**Domain** | str,  | str,  |  | [optional] 
**Port** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Enabled** | str,  | str,  |  | [optional] 
**IsDefault** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_insert_registered_service_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_insert_registered_service_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_registered_services_get**
<a name="v1_registered_services_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] v1_registered_services_get()

 List services

Review the [Service Spec Syntax](/docs/feature-guides/administer-security-policies/services/saasapp-spec-syntax/) for more information on the Service data structures.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import registered_service_api
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
    api_instance = registered_service_api.RegisteredServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'ServiceID': "ServiceID_example",
        'DefaultServices': True,
        'ServiceName': "ServiceName_example",
        'FriendlyName': "FriendlyName_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  List services
        api_response = api_instance.v1_registered_services_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegisteredServiceApi->v1_registered_services_get: %s\n" % e)
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
ServiceID | ServiceIDSchema | | optional
DefaultServices | DefaultServicesSchema | | optional
ServiceName | ServiceNameSchema | | optional
FriendlyName | FriendlyNameSchema | | optional


# ServiceIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DefaultServicesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ServiceNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FriendlyNameSchema

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
200 | [ApiResponseFor200](#v1_registered_services_get.ApiResponseFor200) | OK

#### v1_registered_services_get.ApiResponseFor200
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
**ServiceName** | str,  | str,  |  | [optional] 
**FriendlyName** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**ServiceDiscovery** | str,  | str,  |  | [optional] 
**ServiceVersion** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Description** | str,  | str,  |  | [optional] 
**CreatedBy** | str,  | str,  |  | [optional] 
**CreatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**LastUpdatedBy** | str,  | str,  |  | [optional] 
**LastUpdatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeletedBy** | str,  | str,  |  | [optional] 
**DeletedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**External** | str,  | str,  |  | [optional] 
**OIDCEnabled** | str,  | str,  |  | [optional] 
**OIDCClientSpec** | str,  | str,  |  | [optional] 
**ServiceSpec** | str,  | str,  |  | [optional] 
**UserFacing** | str,  | str,  |  | [optional] 
**Protocol** | str,  | str,  |  | [optional] 
**Domain** | str,  | str,  |  | [optional] 
**Port** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Enabled** | str,  | str,  |  | [optional] 
**IsDefault** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_service_connection_test_post**
<a name="v1_service_connection_test_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_service_connection_test_post(any_type)

 POST to start the service connection test

This end point is used to start the service connection test for a service spec

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import registered_service_api
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
    api_instance = registered_service_api.RegisteredServiceApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
    }
    body = dict(
        service_id="dsrini-dev05-httpconnect.dev05-banyan.bnn",
    )
    try:
        #  POST to start the service connection test
        api_response = api_instance.v1_service_connection_test_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegisteredServiceApi->v1_service_connection_test_post: %s\n" % e)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        service_id="dsrini-dev05-httpconnect.dev05-banyan.bnn",
    )
    try:
        #  POST to start the service connection test
        api_response = api_instance.v1_service_connection_test_post(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegisteredServiceApi->v1_service_connection_test_post: %s\n" % e)
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
**ServiceID** | str,  | str,  |  | [optional] 
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
200 | [ApiResponseFor200](#v1_service_connection_test_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_service_connection_test_post.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v1_service_connection_test_post.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#v1_service_connection_test_post.ApiResponseFor500) | Internal Server Error

#### v1_service_connection_test_post.ApiResponseFor200
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
**[FrontendConnStatus](#FrontendConnStatus)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[BackendConnStatus](#BackendConnStatus)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# FrontendConnStatus

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**DomainNameResolutionStatus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Reachability** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorMsg** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# BackendConnStatus

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
**SiteName** | str,  | str,  |  | [optional] 
**[AccessTierStatus](#AccessTierStatus)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NetagentBackendStatus](#NetagentBackendStatus)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# AccessTierStatus

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**DomainNameResolutionStatus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Reachability** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorMsg** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NetagentBackendStatus

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
**ID** | str,  | str,  |  | [optional] 
**SiteName** | str,  | str,  |  | [optional] 
**NetagentHostname** | str,  | str,  |  | [optional] 
**[ConnStatus](#ConnStatus)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**ValidBefore** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ConnStatus

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**DomainNameResolutionStatus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Reachability** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorMsg** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_service_connection_test_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_service_connection_test_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_service_connection_test_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_services_stats_get**
<a name="v1_services_stats_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_services_stats_get()

 Get the services statistics for an org

Fetch services statistics for an org

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import registered_service_api
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
    api_instance = registered_service_api.RegisteredServiceApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Get the services statistics for an org
        api_response = api_instance.v1_services_stats_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegisteredServiceApi->v1_services_stats_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v1_services_stats_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_services_stats_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v1_services_stats_get.ApiResponseFor500) | Internal Server Error

#### v1_services_stats_get.ApiResponseFor200
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
**total** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[type](#type)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hosted** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**saas_app** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**idp_routed** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_services_stats_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_services_stats_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_access_tier_id_registered_services_get**
<a name="v2_access_tier_id_registered_services_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_access_tier_id_registered_services_get(id)

 List registered services attached to Access Tier for an organization

List registered services attached to access tier for an organization 

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import registered_service_api
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
    api_instance = registered_service_api.RegisteredServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        #  List registered services attached to Access Tier for an organization
        api_response = api_instance.v2_access_tier_id_registered_services_get(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegisteredServiceApi->v2_access_tier_id_registered_services_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'skip': 1,
        'limit': 1,
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  List registered services attached to Access Tier for an organization
        api_response = api_instance.v2_access_tier_id_registered_services_get(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegisteredServiceApi->v2_access_tier_id_registered_services_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
skip | SkipSchema | | optional
limit | LimitSchema | | optional


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
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_access_tier_id_registered_services_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_access_tier_id_registered_services_get.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_access_tier_id_registered_services_get.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_access_tier_id_registered_services_get.ApiResponseFor500) | Internal Server Error

#### v2_access_tier_id_registered_services_get.ApiResponseFor200
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
**[registered_services](#registered_services)** | list, tuple,  | tuple,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# registered_services

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
**ServiceName** | str,  | str,  |  | [optional] 
**FriendlyName** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**ServiceDiscovery** | str,  | str,  |  | [optional] 
**ServiceVersion** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Description** | str,  | str,  |  | [optional] 
**CreatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**CreatedBy** | str,  | str,  |  | [optional] 
**LastUpdatedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**LastUpdatedBy** | str,  | str,  |  | [optional] 
**DeletedAt** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeletedBy** | str,  | str,  |  | [optional] 
**External** | str,  | str,  |  | [optional] 
**OIDCEnabled** | str,  | str,  |  | [optional] 
**OIDCClientSpec** | str,  | str,  |  | [optional] 
**ServiceSpec** | str,  | str,  |  | [optional] 
**UserFacing** | str,  | str,  |  | [optional] 
**Protocol** | str,  | str,  |  | [optional] 
**Domain** | str,  | str,  |  | [optional] 
**Port** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Enabled** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_access_tier_id_registered_services_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_access_tier_id_registered_services_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_access_tier_id_registered_services_get.ApiResponseFor500
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
**request_id** | str,  | str,  |  | [optional] 
**error_code** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**error_description** | str,  | str,  |  | [optional] 
**data** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

