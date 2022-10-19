<a name="__pageTop"></a>
# openapi_client.apis.tags.tunnel_resource_api.TunnelResourceApi

All URIs are relative to *https://dev02.console.bnntest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_tunnel_resource_ct_get**](#v2_tunnel_resource_ct_get) | **get** /v2/tunnel_resource/ct |  Get List of Tunnel Resource Conntrack Logs
[**v2_tunnel_resource_ct_post**](#v2_tunnel_resource_ct_post) | **post** /v2/tunnel_resource/ct |  Creates unique service discovery logs
[**v2_tunnel_resource_dns_get**](#v2_tunnel_resource_dns_get) | **get** /v2/tunnel_resource/dns |  Get List of Tunnel Resource DNS Query Logs
[**v2_tunnel_resource_dns_post**](#v2_tunnel_resource_dns_post) | **post** /v2/tunnel_resource/dns |  Creates unique service discovery logs
[**v2_tunnel_resource_get**](#v2_tunnel_resource_get) | **get** /v2/tunnel_resource |  Get List of Tunnel Resource Logs
[**v2_tunnel_resource_id_get**](#v2_tunnel_resource_id_get) | **get** /v2/tunnel_resource/{id} |  Get details of Tunnel Resource log by id

# **v2_tunnel_resource_ct_get**
<a name="v2_tunnel_resource_ct_get"></a>
> v2_tunnel_resource_ct_get()

 Get List of Tunnel Resource Conntrack Logs

This end point returns service discovery conntrack logs with in an org. API also supports filter by different fields in query params.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import tunnel_resource_api
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
    api_instance = tunnel_resource_api.TunnelResourceApi(api_client)

    # example passing only optional values
    query_params = {
        'id': "id_example",
        'src_ip': "src_ip_example",
        'dst_ip': "dst_ip_example",
        'dst_port': "dst_port_example",
        'order_by': "order_by_example",
        'sort': "sort_example",
        'limit': "limit_example",
        'skip': "skip_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  Get List of Tunnel Resource Conntrack Logs
        api_response = api_instance.v2_tunnel_resource_ct_get(
            query_params=query_params,
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TunnelResourceApi->v2_tunnel_resource_ct_get: %s\n" % e)
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
id | IdSchema | | optional
src_ip | SrcIpSchema | | optional
dst_ip | DstIpSchema | | optional
dst_port | DstPortSchema | | optional
order_by | OrderBySchema | | optional
sort | SortSchema | | optional
limit | LimitSchema | | optional
skip | SkipSchema | | optional


# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SrcIpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DstIpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DstPortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SkipSchema

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
200 | [ApiResponseFor200](#v2_tunnel_resource_ct_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_tunnel_resource_ct_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v2_tunnel_resource_ct_get.ApiResponseFor500) | Internal Server Error

#### v2_tunnel_resource_ct_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_ct_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_ct_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_tunnel_resource_ct_post**
<a name="v2_tunnel_resource_ct_post"></a>
> v2_tunnel_resource_ct_post()

 Creates unique service discovery logs

This end point will process service discovery conntrack logs from Shield in batches. API also filters unique logs per device/tunnel address.Bearer token minimum profile must be ProfileEventWriter

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import tunnel_resource_api
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
    api_instance = tunnel_resource_api.TunnelResourceApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  Creates unique service discovery logs
        api_response = api_instance.v2_tunnel_resource_ct_post(
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TunnelResourceApi->v2_tunnel_resource_ct_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
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
200 | [ApiResponseFor200](#v2_tunnel_resource_ct_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_tunnel_resource_ct_post.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v2_tunnel_resource_ct_post.ApiResponseFor500) | Internal Server Error

#### v2_tunnel_resource_ct_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_ct_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_ct_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_tunnel_resource_dns_get**
<a name="v2_tunnel_resource_dns_get"></a>
> v2_tunnel_resource_dns_get()

 Get List of Tunnel Resource DNS Query Logs

This end point returns service discovery dns query logs with in an org. API also supports filter by different fields in query params.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import tunnel_resource_api
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
    api_instance = tunnel_resource_api.TunnelResourceApi(api_client)

    # example passing only optional values
    query_params = {
        'id': "id_example",
        'src_ip': "src_ip_example",
        'dst_ip': "dst_ip_example",
        'fqdn': "fqdn_example",
        'order_by': "order_by_example",
        'sort': "sort_example",
        'limit': "limit_example",
        'skip': "skip_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  Get List of Tunnel Resource DNS Query Logs
        api_response = api_instance.v2_tunnel_resource_dns_get(
            query_params=query_params,
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TunnelResourceApi->v2_tunnel_resource_dns_get: %s\n" % e)
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
id | IdSchema | | optional
src_ip | SrcIpSchema | | optional
dst_ip | DstIpSchema | | optional
fqdn | FqdnSchema | | optional
order_by | OrderBySchema | | optional
sort | SortSchema | | optional
limit | LimitSchema | | optional
skip | SkipSchema | | optional


# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SrcIpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DstIpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FqdnSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SkipSchema

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
200 | [ApiResponseFor200](#v2_tunnel_resource_dns_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_tunnel_resource_dns_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v2_tunnel_resource_dns_get.ApiResponseFor500) | Internal Server Error

#### v2_tunnel_resource_dns_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_dns_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_dns_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_tunnel_resource_dns_post**
<a name="v2_tunnel_resource_dns_post"></a>
> v2_tunnel_resource_dns_post()

 Creates unique service discovery logs

This end point will process service discovery dns query logs from Shield in batches. API also filters unique logs per device/tunnel address.Bearer token minimum profile must be ProfileEventWriter

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import tunnel_resource_api
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
    api_instance = tunnel_resource_api.TunnelResourceApi(api_client)

    # example passing only optional values
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  Creates unique service discovery logs
        api_response = api_instance.v2_tunnel_resource_dns_post(
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TunnelResourceApi->v2_tunnel_resource_dns_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
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
200 | [ApiResponseFor200](#v2_tunnel_resource_dns_post.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_tunnel_resource_dns_post.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v2_tunnel_resource_dns_post.ApiResponseFor500) | Internal Server Error

#### v2_tunnel_resource_dns_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_dns_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_dns_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_tunnel_resource_get**
<a name="v2_tunnel_resource_get"></a>
> v2_tunnel_resource_get()

 Get List of Tunnel Resource Logs

This end point returns service discovery list with in an org. API also supports filter by different fields in query params.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import tunnel_resource_api
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
    api_instance = tunnel_resource_api.TunnelResourceApi(api_client)

    # example passing only optional values
    query_params = {
        'protocol': "protocol_example",
        'dst_ip': "dst_ip_example",
        'dst_port': "dst_port_example",
        'status': "status_example",
        'service_tunnel_name': "service_tunnel_name_example",
        'updated_at': "updated_at_example",
        'order_by': "order_by_example",
        'sort': "sort_example",
        'limit': "limit_example",
        'skip': "skip_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  Get List of Tunnel Resource Logs
        api_response = api_instance.v2_tunnel_resource_get(
            query_params=query_params,
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TunnelResourceApi->v2_tunnel_resource_get: %s\n" % e)
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
protocol | ProtocolSchema | | optional
dst_ip | DstIpSchema | | optional
dst_port | DstPortSchema | | optional
status | StatusSchema | | optional
service_tunnel_name | ServiceTunnelNameSchema | | optional
updated_at | UpdatedAtSchema | | optional
order_by | OrderBySchema | | optional
sort | SortSchema | | optional
limit | LimitSchema | | optional
skip | SkipSchema | | optional


# ProtocolSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DstIpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DstPortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServiceTunnelNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UpdatedAtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SkipSchema

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
200 | [ApiResponseFor200](#v2_tunnel_resource_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_tunnel_resource_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v2_tunnel_resource_get.ApiResponseFor500) | Internal Server Error

#### v2_tunnel_resource_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_tunnel_resource_id_get**
<a name="v2_tunnel_resource_id_get"></a>
> v2_tunnel_resource_id_get(id)

 Get details of Tunnel Resource log by id

This end point returns list of service discovery details by id. ID must be service discovery list id which is rawbase64url encoded of dst_ip + _ + dst_port.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import tunnel_resource_api
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
    api_instance = tunnel_resource_api.TunnelResourceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        #  Get details of Tunnel Resource log by id
        api_response = api_instance.v2_tunnel_resource_id_get(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TunnelResourceApi->v2_tunnel_resource_id_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
    }
    query_params = {
        'protocol': "protocol_example",
        'dst_ip': "dst_ip_example",
        'dst_port': "dst_port_example",
        'status': "status_example",
        'service_tunnel_name': "service_tunnel_name_example",
        'user_name': "user_name_example",
        'email': "email_example",
        'device_name': "device_name_example",
        'updated_at': "updated_at_example",
        'order_by': "order_by_example",
        'sort': "sort_example",
        'limit': "limit_example",
        'skip': "skip_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
        'ContentType': "ContentType_example",
    }
    try:
        #  Get details of Tunnel Resource log by id
        api_response = api_instance.v2_tunnel_resource_id_get(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling TunnelResourceApi->v2_tunnel_resource_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
protocol | ProtocolSchema | | optional
dst_ip | DstIpSchema | | optional
dst_port | DstPortSchema | | optional
status | StatusSchema | | optional
service_tunnel_name | ServiceTunnelNameSchema | | optional
user_name | UserNameSchema | | optional
email | EmailSchema | | optional
device_name | DeviceNameSchema | | optional
updated_at | UpdatedAtSchema | | optional
order_by | OrderBySchema | | optional
sort | SortSchema | | optional
limit | LimitSchema | | optional
skip | SkipSchema | | optional


# ProtocolSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DstIpSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DstPortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StatusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServiceTunnelNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UserNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DeviceNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# UpdatedAtSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SkipSchema

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
200 | [ApiResponseFor200](#v2_tunnel_resource_id_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v2_tunnel_resource_id_get.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#v2_tunnel_resource_id_get.ApiResponseFor500) | Internal Server Error

#### v2_tunnel_resource_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_id_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v2_tunnel_resource_id_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

