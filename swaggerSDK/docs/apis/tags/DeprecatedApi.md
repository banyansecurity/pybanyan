<a name="__pageTop"></a>
# openapi_client.apis.tags.deprecated_api.DeprecatedApi

All URIs are relative to *https://dev02.console.bnntest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_active_users_get**](#v1_active_users_get) | **get** /v1/active_users |  Get the active users from last 24 hrs
[**v1_all_apps_get**](#v1_all_apps_get) | **get** /v1/all_apps |  Summarize data into Apps
[**v1_mdm_otdp_get**](#v1_mdm_otdp_get) | **get** /v1/mdm/otdp |  Generate OTDP
[**v1_mdm_resend_otdp_mail_get**](#v1_mdm_resend_otdp_mail_get) | **get** /v1/mdm/resend_otdp_mail |  Resend OTDP Email
[**v2_access_tier_tunnel_get**](#v2_access_tier_tunnel_get) | **get** /v2/access_tier_tunnel |  Get details of api key 
[**v2_access_tier_tunnel_id_delete**](#v2_access_tier_tunnel_id_delete) | **delete** /v2/access_tier_tunnel/{id} |  Delete access tier tunnel config 
[**v2_access_tier_tunnel_id_get**](#v2_access_tier_tunnel_id_get) | **get** /v2/access_tier_tunnel/{id} |  Get details of api key 
[**v2_access_tier_tunnel_id_put**](#v2_access_tier_tunnel_id_put) | **put** /v2/access_tier_tunnel/{id} |  Update access tier tunnel config information for an organization
[**v2_access_tier_tunnel_post**](#v2_access_tier_tunnel_post) | **post** /v2/access_tier_tunnel |  Insert access tier tunnel config information for an organization

# **v1_active_users_get**
<a name="v1_active_users_get"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] v1_active_users_get()

 Get the active users from last 24 hrs

Fetches users information who were active in last 24 hrs

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import deprecated_api
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
    api_instance = deprecated_api.DeprecatedApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Get the active users from last 24 hrs
        api_response = api_instance.v1_active_users_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v1_active_users_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v1_active_users_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_active_users_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v1_active_users_get.ApiResponseFor500) | Internal Server Error

#### v1_active_users_get.ApiResponseFor200
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
**OrgID** | str,  | str,  |  | [optional] 
**Email** | str,  | str,  |  | [optional] 
**SerialNumber** | str,  | str,  |  | [optional] 
**Model** | str,  | str,  |  | [optional] 
**Ownership** | str,  | str,  |  | [optional] 
**Platform** | str,  | str,  |  | [optional] 
**OS** | str,  | str,  |  | [optional] 
**Architecture** | str,  | str,  |  | [optional] 
**Source** | str,  | str,  |  | [optional] 
**Name** | str,  | str,  |  | [optional] 
**Groups** | str,  | str,  |  | [optional] 
**DeviceFriendlyName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_active_users_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_active_users_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_all_apps_get**
<a name="v1_all_apps_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_all_apps_get()

 Summarize data into Apps

This is a complex and comprehensive endpoint that returns that returns all Nodes and Links in the system, converted into Apps and associated statistics. Handle with extreme care!

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import deprecated_api
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
    api_instance = deprecated_api.DeprecatedApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Summarize data into Apps
        api_response = api_instance.v1_all_apps_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v1_all_apps_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v1_all_apps_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_all_apps_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v1_all_apps_get.ApiResponseFor500) | Internal Server Error

#### v1_all_apps_get.ApiResponseFor200
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
**[AppsSummary](#AppsSummary)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# AppsSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[banyan-platform](#banyan-platform)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# banyan-platform

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[onpremise](#onpremise)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[TLSData](#TLSData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TLSData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkID** | str,  | str,  |  | [optional] 
**Version** | str,  | str,  |  | [optional] 
**CipherSuite** | str,  | str,  |  | [optional] 
**Subject** | str,  | str,  |  | [optional] 
**Issuer** | str,  | str,  |  | [optional] 
**NotBefore** | str,  | str,  |  | [optional] 
**NotAfter** | str,  | str,  |  | [optional] 
**ALPN** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.app** | str,  | str,  |  | [optional] 
**com.banyanops.command** | str,  | str,  |  | [optional] 
**com.banyanops.exe** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**com.banyanops.shield.version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[1200/tcp](#1200/tcp)** | list, tuple,  | tuple,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# 1200/tcp

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
**HostIP** | str,  | str,  |  | [optional] 
**HostPort** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# onpremise

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[TLSData](#TLSData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TLSData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkID** | str,  | str,  |  | [optional] 
**Version** | str,  | str,  |  | [optional] 
**CipherSuite** | str,  | str,  |  | [optional] 
**Subject** | str,  | str,  |  | [optional] 
**Issuer** | str,  | str,  |  | [optional] 
**NotBefore** | str,  | str,  |  | [optional] 
**NotAfter** | str,  | str,  |  | [optional] 
**ALPN** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[polaris-app](#polaris-app)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[AppsSummary](#AppsSummary)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**banyan.app** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[443/tcp](#443/tcp)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# 443/tcp

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
**HostIP** | str,  | str,  |  | [optional] 
**HostPort** | str,  | str,  |  | [optional] 
**[80/tcp](#80/tcp)** | list, tuple,  | tuple,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# 80/tcp

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
**HostIP** | str,  | str,  |  | [optional] 
**HostPort** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# polaris-app

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[ShieldConfig](#ShieldConfig)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**banyan.app** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[443/tcp](#443/tcp)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# 443/tcp

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
**HostIP** | str,  | str,  |  | [optional] 
**HostPort** | str,  | str,  |  | [optional] 
**[80/tcp](#80/tcp)** | list, tuple,  | tuple,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# 80/tcp

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
**HostIP** | str,  | str,  |  | [optional] 
**HostPort** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ShieldConfig

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**UUID** | str,  | str,  |  | [optional] 
**OrgID** | str,  | str,  |  | [optional] 
**ShieldName** | str,  | str,  |  | [optional] 
**GroupType** | str,  | str,  |  | [optional] 
**ClusterMgrType** | str,  | str,  |  | [optional] 
**ClusterMgrIP** | str,  | str,  |  | [optional] 
**ShieldVersion** | str,  | str,  |  | [optional] 
**AutoUpgrade** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# AppsSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[all-clusters](#all-clusters)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[banyan-platform](#banyan-platform)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[ShieldConfig](#ShieldConfig)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[AppsSummary](#AppsSummary)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# all-clusters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[TLSData](#TLSData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TLSData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkID** | str,  | str,  |  | [optional] 
**Version** | str,  | str,  |  | [optional] 
**CipherSuite** | str,  | str,  |  | [optional] 
**Subject** | str,  | str,  |  | [optional] 
**Issuer** | str,  | str,  |  | [optional] 
**NotBefore** | str,  | str,  |  | [optional] 
**NotAfter** | str,  | str,  |  | [optional] 
**ALPN** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**banyan.app** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**com.docker.swarm.constraints** | str,  | str,  |  | [optional] 
**com.docker.swarm.id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# banyan-platform

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[TLSData](#TLSData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TLSData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkID** | str,  | str,  |  | [optional] 
**Version** | str,  | str,  |  | [optional] 
**CipherSuite** | str,  | str,  |  | [optional] 
**Subject** | str,  | str,  |  | [optional] 
**Issuer** | str,  | str,  |  | [optional] 
**NotBefore** | str,  | str,  |  | [optional] 
**NotAfter** | str,  | str,  |  | [optional] 
**ALPN** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.app** | str,  | str,  |  | [optional] 
**com.banyanops.command** | str,  | str,  |  | [optional] 
**com.banyanops.exe** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**com.banyanops.shield.version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[1200/tcp](#1200/tcp)** | list, tuple,  | tuple,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# 1200/tcp

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
**HostIP** | str,  | str,  |  | [optional] 
**HostPort** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ShieldConfig

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**UUID** | str,  | str,  |  | [optional] 
**OrgID** | str,  | str,  |  | [optional] 
**ShieldName** | str,  | str,  |  | [optional] 
**GroupType** | str,  | str,  |  | [optional] 
**ClusterMgrType** | str,  | str,  |  | [optional] 
**ClusterMgrIP** | str,  | str,  |  | [optional] 
**ShieldVersion** | str,  | str,  |  | [optional] 
**AutoUpgrade** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# AppsSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[DOCKER-PLATFORM](#DOCKER-PLATFORM)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[E-COMMERCE-TEST](#E-COMMERCE-TEST)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[MYSQL-TEST](#MYSQL-TEST)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[RUBY-TEST](#RUBY-TEST)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# DOCKER-PLATFORM

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.app** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# E-COMMERCE-TEST

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.app** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**com.docker.swarm.id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# MYSQL-TEST

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**banyan.app** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**com.docker.swarm.constraints** | str,  | str,  |  | [optional] 
**com.docker.swarm.id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# RUBY-TEST

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[VOTE-FOR-ME](#VOTE-FOR-ME)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[AppsSummary](#AppsSummary)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.app** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**com.docker.swarm.constraints** | str,  | str,  |  | [optional] 
**com.docker.swarm.id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[4567/tcp](#4567/tcp)** | list, tuple,  | tuple,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# 4567/tcp

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
**HostIP** | str,  | str,  |  | [optional] 
**HostPort** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# VOTE-FOR-ME

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[azure_swarm_112](#azure_swarm_112)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[banyan-platform](#banyan-platform)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[ShieldConfig](#ShieldConfig)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**banyan.app** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**com.docker.swarm.constraints** | str,  | str,  |  | [optional] 
**com.docker.swarm.id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[6379/tcp](#6379/tcp)** | list, tuple,  | tuple,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# 6379/tcp

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
**HostIP** | str,  | str,  |  | [optional] 
**HostPort** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# azure_swarm_112

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[TLSData](#TLSData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TLSData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkID** | str,  | str,  |  | [optional] 
**Version** | str,  | str,  |  | [optional] 
**CipherSuite** | str,  | str,  |  | [optional] 
**Subject** | str,  | str,  |  | [optional] 
**Issuer** | str,  | str,  |  | [optional] 
**NotBefore** | str,  | str,  |  | [optional] 
**NotAfter** | str,  | str,  |  | [optional] 
**ALPN** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**banyan.app** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**com.docker.swarm.constraints** | str,  | str,  |  | [optional] 
**com.docker.swarm.id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# banyan-platform

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[TLSData](#TLSData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TLSData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkID** | str,  | str,  |  | [optional] 
**Version** | str,  | str,  |  | [optional] 
**CipherSuite** | str,  | str,  |  | [optional] 
**Subject** | str,  | str,  |  | [optional] 
**Issuer** | str,  | str,  |  | [optional] 
**NotBefore** | str,  | str,  |  | [optional] 
**NotAfter** | str,  | str,  |  | [optional] 
**ALPN** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.app** | str,  | str,  |  | [optional] 
**com.banyanops.command** | str,  | str,  |  | [optional] 
**com.banyanops.exe** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**com.banyanops.shield.version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[1200/tcp](#1200/tcp)** | list, tuple,  | tuple,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# 1200/tcp

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
**HostIP** | str,  | str,  |  | [optional] 
**HostPort** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ShieldConfig

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**UUID** | str,  | str,  |  | [optional] 
**OrgID** | str,  | str,  |  | [optional] 
**ShieldName** | str,  | str,  |  | [optional] 
**GroupType** | str,  | str,  |  | [optional] 
**ClusterMgrType** | str,  | str,  |  | [optional] 
**ClusterMgrIP** | str,  | str,  |  | [optional] 
**ShieldVersion** | str,  | str,  |  | [optional] 
**AutoUpgrade** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# AppsSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[aws_k8s_14](#aws_k8s_14)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# aws_k8s_14

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[banyan-platform](#banyan-platform)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[ShieldConfig](#ShieldConfig)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.app** | str,  | str,  |  | [optional] 
**com.banyanops.command** | str,  | str,  |  | [optional] 
**com.banyanops.exe** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**com.banyanops.shield.version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[1200/tcp](#1200/tcp)** | list, tuple,  | tuple,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# 1200/tcp

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
**HostIP** | str,  | str,  |  | [optional] 
**HostPort** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# banyan-platform

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[elasticsearch-logging](#elasticsearch-logging)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[guestbook](#guestbook)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[heapster](#heapster)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[influxGrafana](#influxGrafana)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[kibana-logging](#kibana-logging)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[kube-dns](#kube-dns)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[kubernetes-dashboard](#kubernetes-dashboard)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[redis](#redis)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[TLSData](#TLSData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TLSData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkID** | str,  | str,  |  | [optional] 
**Version** | str,  | str,  |  | [optional] 
**CipherSuite** | str,  | str,  |  | [optional] 
**Subject** | str,  | str,  |  | [optional] 
**Issuer** | str,  | str,  |  | [optional] 
**NotBefore** | str,  | str,  |  | [optional] 
**NotAfter** | str,  | str,  |  | [optional] 
**ALPN** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.app** | str,  | str,  |  | [optional] 
**com.banyanops.command** | str,  | str,  |  | [optional] 
**com.banyanops.exe** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**com.banyanops.servicetype** | str,  | str,  |  | [optional] 
**com.banyanops.shield.version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[1200/tcp](#1200/tcp)** | list, tuple,  | tuple,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# 1200/tcp

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
**HostIP** | str,  | str,  |  | [optional] 
**HostPort** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# elasticsearch-logging

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.serviceid** | str,  | str,  |  | [optional] 
**com.banyanops.serviceip** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**io.kubernetes.container.hash** | str,  | str,  |  | [optional] 
**io.kubernetes.container.name** | str,  | str,  |  | [optional] 
**io.kubernetes.container.ports** | str,  | str,  |  | [optional] 
**io.kubernetes.container.restartCount** | str,  | str,  |  | [optional] 
**io.kubernetes.container.terminationMessagePath** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.name** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.namespace** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.terminationGracePeriod** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.uid** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# guestbook

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**L7Protocols** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.serviceid** | str,  | str,  |  | [optional] 
**com.banyanops.serviceip** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**io.kubernetes.container.hash** | str,  | str,  |  | [optional] 
**io.kubernetes.container.name** | str,  | str,  |  | [optional] 
**io.kubernetes.container.ports** | str,  | str,  |  | [optional] 
**io.kubernetes.container.restartCount** | str,  | str,  |  | [optional] 
**io.kubernetes.container.terminationMessagePath** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.name** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.namespace** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.terminationGracePeriod** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.uid** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# heapster

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.serviceid** | str,  | str,  |  | [optional] 
**com.banyanops.serviceip** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**io.kubernetes.container.hash** | str,  | str,  |  | [optional] 
**io.kubernetes.container.name** | str,  | str,  |  | [optional] 
**io.kubernetes.container.restartCount** | str,  | str,  |  | [optional] 
**io.kubernetes.container.terminationMessagePath** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.name** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.namespace** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.terminationGracePeriod** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.uid** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# influxGrafana

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.serviceid** | str,  | str,  |  | [optional] 
**com.banyanops.serviceip** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**io.kubernetes.container.hash** | str,  | str,  |  | [optional] 
**io.kubernetes.container.name** | str,  | str,  |  | [optional] 
**io.kubernetes.container.ports** | str,  | str,  |  | [optional] 
**io.kubernetes.container.restartCount** | str,  | str,  |  | [optional] 
**io.kubernetes.container.terminationMessagePath** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.name** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.namespace** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.terminationGracePeriod** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.uid** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# kibana-logging

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**L7Protocols** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.serviceid** | str,  | str,  |  | [optional] 
**com.banyanops.serviceip** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**io.kubernetes.container.hash** | str,  | str,  |  | [optional] 
**io.kubernetes.container.name** | str,  | str,  |  | [optional] 
**io.kubernetes.container.ports** | str,  | str,  |  | [optional] 
**io.kubernetes.container.restartCount** | str,  | str,  |  | [optional] 
**io.kubernetes.container.terminationMessagePath** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.name** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.namespace** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.terminationGracePeriod** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.uid** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# kube-dns

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.serviceid** | str,  | str,  |  | [optional] 
**com.banyanops.serviceip** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**io.kubernetes.container.hash** | str,  | str,  |  | [optional] 
**io.kubernetes.container.name** | str,  | str,  |  | [optional] 
**io.kubernetes.container.ports** | str,  | str,  |  | [optional] 
**io.kubernetes.container.restartCount** | str,  | str,  |  | [optional] 
**io.kubernetes.container.terminationMessagePath** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.name** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.namespace** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.terminationGracePeriod** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.uid** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# kubernetes-dashboard

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.serviceid** | str,  | str,  |  | [optional] 
**com.banyanops.serviceip** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**io.kubernetes.container.hash** | str,  | str,  |  | [optional] 
**io.kubernetes.container.name** | str,  | str,  |  | [optional] 
**io.kubernetes.container.ports** | str,  | str,  |  | [optional] 
**io.kubernetes.container.restartCount** | str,  | str,  |  | [optional] 
**io.kubernetes.container.terminationMessagePath** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.name** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.namespace** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.terminationGracePeriod** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.uid** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# redis

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**AppName** | str,  | str,  |  | [optional] 
**NumNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtNodes** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumExtLinks** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[L7Protocols](#L7Protocols)** | list, tuple,  | tuple,  |  | [optional] 
**[TopTputLink](#TopTputLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[TopRTime95Link](#TopRTime95Link)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**Top5Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Top5RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[LastUpdatedNode](#LastUpdatedNode)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# L7Protocols

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TopTputLink

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# TopRTime95Link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LinkIDFE** | str,  | str,  |  | [optional] 
**LinkID** | str,  | str,  |  | [optional] 
**SrcID** | str,  | str,  |  | [optional] 
**DestID** | str,  | str,  |  | [optional] 
**SrcIP** | str,  | str,  |  | [optional] 
**DestIP** | str,  | str,  |  | [optional] 
**SrcName** | str,  | str,  |  | [optional] 
**DestName** | str,  | str,  |  | [optional] 
**DestPort** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TrafficType** | str,  | str,  |  | [optional] 
**L7ProtocolFE** | str,  | str,  |  | [optional] 
**QueryType** | str,  | str,  |  | [optional] 
**QueryResource** | str,  | str,  |  | [optional] 
**Tput** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTimeMean** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RTime95** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ErrorRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**RxRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**DeltaTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ConnRate** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**NumSamples** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**StatsEndTime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**TLSData** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**InsertTime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LastUpdatedNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**NodeType** | str,  | str,  |  | [optional] 
**NodeID** | str,  | str,  |  | [optional] 
**NodeName** | str,  | str,  |  | [optional] 
**Image** | str,  | str,  |  | [optional] 
**Repo** | str,  | str,  |  | [optional] 
**Tag** | str,  | str,  |  | [optional] 
**Hostname** | str,  | str,  |  | [optional] 
**[HostIPs](#HostIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[Labels](#Labels)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[NodeIPs](#NodeIPs)** | list, tuple,  | tuple,  |  | [optional] 
**[PortMap](#PortMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PID** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**AppName** | str,  | str,  |  | [optional] 
**ServiceName** | str,  | str,  |  | [optional] 
**ServiceID** | str,  | str,  |  | [optional] 
**ServiceType** | str,  | str,  |  | [optional] 
**Timestamp** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**Action** | str,  | str,  |  | [optional] 
**NodeStartTime** | str,  | str,  |  | [optional] 
**NodeStopTime** | str,  | str,  |  | [optional] 
**ClusterID** | str,  | str,  |  | [optional] 
**ClusterName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# HostIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**com.banyanops.serviceid** | str,  | str,  |  | [optional] 
**com.banyanops.serviceip** | str,  | str,  |  | [optional] 
**com.banyanops.servicename** | str,  | str,  |  | [optional] 
**io.kubernetes.container.hash** | str,  | str,  |  | [optional] 
**io.kubernetes.container.name** | str,  | str,  |  | [optional] 
**io.kubernetes.container.ports** | str,  | str,  |  | [optional] 
**io.kubernetes.container.restartCount** | str,  | str,  |  | [optional] 
**io.kubernetes.container.terminationMessagePath** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.name** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.namespace** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.terminationGracePeriod** | str,  | str,  |  | [optional] 
**io.kubernetes.pod.uid** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# NodeIPs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PortMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# ShieldConfig

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**UUID** | str,  | str,  |  | [optional] 
**OrgID** | str,  | str,  |  | [optional] 
**ShieldName** | str,  | str,  |  | [optional] 
**GroupType** | str,  | str,  |  | [optional] 
**ClusterMgrType** | str,  | str,  |  | [optional] 
**ClusterMgrIP** | str,  | str,  |  | [optional] 
**ShieldVersion** | str,  | str,  |  | [optional] 
**AutoUpgrade** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_all_apps_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_all_apps_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_mdm_otdp_get**
<a name="v1_mdm_otdp_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_mdm_otdp_get()

 Generate OTDP

This end point generates One Time Device Passcode (OTDP) and binary download path

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import deprecated_api
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
    api_instance = deprecated_api.DeprecatedApi(api_client)

    # example passing only optional values
    query_params = {
        'Email': "Email_example",
        'SerialNumber': "SerialNumber_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Generate OTDP
        api_response = api_instance.v1_mdm_otdp_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v1_mdm_otdp_get: %s\n" % e)
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

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_mdm_otdp_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_mdm_otdp_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v1_mdm_otdp_get.ApiResponseFor500) | Internal Server Error

#### v1_mdm_otdp_get.ApiResponseFor200
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
**Otdp** | str,  | str,  |  | [optional] 
**BinaryAppPath** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_mdm_otdp_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_mdm_otdp_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v1_mdm_resend_otdp_mail_get**
<a name="v1_mdm_resend_otdp_mail_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_mdm_resend_otdp_mail_get()

 Resend OTDP Email

This end point resends email containing otdp and binary download path info

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import deprecated_api
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
    api_instance = deprecated_api.DeprecatedApi(api_client)

    # example passing only optional values
    query_params = {
        'Email': "Email_example",
        'SerialNumber': "SerialNumber_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Resend OTDP Email
        api_response = api_instance.v1_mdm_resend_otdp_mail_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v1_mdm_resend_otdp_mail_get: %s\n" % e)
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

# AuthorizationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v1_mdm_resend_otdp_mail_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_mdm_resend_otdp_mail_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v1_mdm_resend_otdp_mail_get.ApiResponseFor500) | Internal Server Error

#### v1_mdm_resend_otdp_mail_get.ApiResponseFor200
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

#### v1_mdm_resend_otdp_mail_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_mdm_resend_otdp_mail_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_access_tier_tunnel_get**
<a name="v2_access_tier_tunnel_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_access_tier_tunnel_get()

 Get details of api key 

To get list of access tier tunnel config of an organization.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import deprecated_api
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
    api_instance = deprecated_api.DeprecatedApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Get details of api key 
        api_response = api_instance.v2_access_tier_tunnel_get(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v2_access_tier_tunnel_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v2_access_tier_tunnel_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_access_tier_tunnel_get.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_access_tier_tunnel_get.ApiResponseFor500) | Internal Server Error

#### v2_access_tier_tunnel_get.ApiResponseFor200
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
**site_name** | str,  | str,  |  | [optional] 
**cname** | str,  | str,  |  | [optional] 
**dns_search_domains** | str,  | str,  |  | [optional] 
**udp_port_number** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tunnel_ip_address** | str,  | str,  |  | [optional] 
**[cidrs](#cidrs)** | list, tuple,  | tuple,  |  | [optional] 
**wireguard_public_key** | str,  | str,  |  | [optional] 
**client_cidr_range** | str,  | str,  |  | [optional] 
**dns_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tunnel_peer_type** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
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

#### v2_access_tier_tunnel_get.ApiResponseFor401
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

#### v2_access_tier_tunnel_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_access_tier_tunnel_id_delete**
<a name="v2_access_tier_tunnel_id_delete"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_access_tier_tunnel_id_delete(id)

 Delete access tier tunnel config 

Delete the access tier tunnel config for an organization.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import deprecated_api
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
    api_instance = deprecated_api.DeprecatedApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    try:
        #  Delete access tier tunnel config 
        api_response = api_instance.v2_access_tier_tunnel_id_delete(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v2_access_tier_tunnel_id_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Delete access tier tunnel config 
        api_response = api_instance.v2_access_tier_tunnel_id_delete(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v2_access_tier_tunnel_id_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#v2_access_tier_tunnel_id_delete.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_access_tier_tunnel_id_delete.ApiResponseFor400) | Status Bad Request
401 | [ApiResponseFor401](#v2_access_tier_tunnel_id_delete.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_access_tier_tunnel_id_delete.ApiResponseFor500) | Internal Server Error

#### v2_access_tier_tunnel_id_delete.ApiResponseFor200
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

#### v2_access_tier_tunnel_id_delete.ApiResponseFor400
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

#### v2_access_tier_tunnel_id_delete.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_access_tier_tunnel_id_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_access_tier_tunnel_id_get**
<a name="v2_access_tier_tunnel_id_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_access_tier_tunnel_id_get(id)

 Get details of api key 

To get details of access tier tunnel config of an organization.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import deprecated_api
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
    api_instance = deprecated_api.DeprecatedApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    try:
        #  Get details of api key 
        api_response = api_instance.v2_access_tier_tunnel_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v2_access_tier_tunnel_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Get details of api key 
        api_response = api_instance.v2_access_tier_tunnel_id_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v2_access_tier_tunnel_id_get: %s\n" % e)
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
200 | [ApiResponseFor200](#v2_access_tier_tunnel_id_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_access_tier_tunnel_id_get.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_access_tier_tunnel_id_get.ApiResponseFor500) | Internal Server Error

#### v2_access_tier_tunnel_id_get.ApiResponseFor200
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
**org_id** | str,  | str,  |  | [optional] 
**site_name** | str,  | str,  |  | [optional] 
**cname** | str,  | str,  |  | [optional] 
**dns_search_domains** | str,  | str,  |  | [optional] 
**udp_port_number** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tunnel_ip_address** | str,  | str,  |  | [optional] 
**[cidrs](#cidrs)** | list, tuple,  | tuple,  |  | [optional] 
**wireguard_public_key** | str,  | str,  |  | [optional] 
**client_cidr_range** | str,  | str,  |  | [optional] 
**dns_enabled** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tunnel_peer_type** | str,  | str,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
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

#### v2_access_tier_tunnel_id_get.ApiResponseFor401
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

#### v2_access_tier_tunnel_id_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_access_tier_tunnel_id_put**
<a name="v2_access_tier_tunnel_id_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_access_tier_tunnel_id_put(idany_type)

 Update access tier tunnel config information for an organization

Update the access tier tunnel config information for an organization.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import deprecated_api
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
    api_instance = deprecated_api.DeprecatedApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    header_params = {
    }
    body = dict(
        cname="tunnel5",
        dns_search_domains="test-tunnel-2",
        udp_port_number=51821,
        cidrs=[
            "11.128.0.1/32"
        ],
        keepalive=1000,
        domains=[
            "domain_2"
        ],
        dns_enabled=True,
    )
    try:
        #  Update access tier tunnel config information for an organization
        api_response = api_instance.v2_access_tier_tunnel_id_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v2_access_tier_tunnel_id_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        cname="tunnel5",
        dns_search_domains="test-tunnel-2",
        udp_port_number=51821,
        cidrs=[
            "11.128.0.1/32"
        ],
        keepalive=1000,
        domains=[
            "domain_2"
        ],
        dns_enabled=True,
    )
    try:
        #  Update access tier tunnel config information for an organization
        api_response = api_instance.v2_access_tier_tunnel_id_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v2_access_tier_tunnel_id_put: %s\n" % e)
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
**cname** | str,  | str,  |  | [optional] 
**dns_search_domains** | str,  | str,  |  | [optional] 
**udp_port_number** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[cidrs](#cidrs)** | list, tuple,  | tuple,  |  | [optional] 
**keepalive** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[domains](#domains)** | list, tuple,  | tuple,  |  | [optional] 
**dns_enabled** | bool,  | BoolClass,  |  | [optional] 
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
200 | [ApiResponseFor200](#v2_access_tier_tunnel_id_put.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_access_tier_tunnel_id_put.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_access_tier_tunnel_id_put.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_access_tier_tunnel_id_put.ApiResponseFor500) | Internal Server Error

#### v2_access_tier_tunnel_id_put.ApiResponseFor200
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

#### v2_access_tier_tunnel_id_put.ApiResponseFor400
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

#### v2_access_tier_tunnel_id_put.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_access_tier_tunnel_id_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_access_tier_tunnel_post**
<a name="v2_access_tier_tunnel_post"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_access_tier_tunnel_post()

 Insert access tier tunnel config information for an organization

Insert the access tier tunnel config information for an organization.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import deprecated_api
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
    api_instance = deprecated_api.DeprecatedApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Insert access tier tunnel config information for an organization
        api_response = api_instance.v2_access_tier_tunnel_post(
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeprecatedApi->v2_access_tier_tunnel_post: %s\n" % e)
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
200 | [ApiResponseFor200](#v2_access_tier_tunnel_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_access_tier_tunnel_post.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#v2_access_tier_tunnel_post.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_access_tier_tunnel_post.ApiResponseFor500) | Internal Server Error

#### v2_access_tier_tunnel_post.ApiResponseFor200
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

#### v2_access_tier_tunnel_post.ApiResponseFor400
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

#### v2_access_tier_tunnel_post.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_access_tier_tunnel_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

