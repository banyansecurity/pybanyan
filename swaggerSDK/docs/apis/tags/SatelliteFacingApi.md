<a name="__pageTop"></a>
# openapi_client.apis.tags.satellite_facing_api.SatelliteFacingApi

All URIs are relative to *https://dev02.console.bnntest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_satellite_facing_config_satellite_name_get**](#v2_satellite_facing_config_satellite_name_get) | **get** /v2/satellite_facing/config/{satellite_name} |  Satellite facing Get satellite tunnel config 
[**v2_satellite_facing_satellite_name_iptables_put**](#v2_satellite_facing_satellite_name_iptables_put) | **put** /v2/satellite_facing/{satellite_name}/iptables |  Satellite facing update satellite status
[**v2_satellite_facing_satellite_name_status_put**](#v2_satellite_facing_satellite_name_status_put) | **put** /v2/satellite_facing/{satellite_name}/status |  Satellite facing update satellite status

# **v2_satellite_facing_config_satellite_name_get**
<a name="v2_satellite_facing_config_satellite_name_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_satellite_facing_config_satellite_name_get(satellite_name)

 Satellite facing Get satellite tunnel config 

Used by satellite to retrieve its own satellite tunnel config from restapi.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import satellite_facing_api
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
    api_instance = satellite_facing_api.SatelliteFacingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'satellite_name': "satellite_name_example",
    }
    header_params = {
    }
    try:
        #  Satellite facing Get satellite tunnel config 
        api_response = api_instance.v2_satellite_facing_config_satellite_name_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SatelliteFacingApi->v2_satellite_facing_config_satellite_name_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'satellite_name': "satellite_name_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Satellite facing Get satellite tunnel config 
        api_response = api_instance.v2_satellite_facing_config_satellite_name_get(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SatelliteFacingApi->v2_satellite_facing_config_satellite_name_get: %s\n" % e)
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
satellite_name | SatelliteNameSchema | | 

# SatelliteNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_satellite_facing_config_satellite_name_get.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_satellite_facing_config_satellite_name_get.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_satellite_facing_config_satellite_name_get.ApiResponseFor500) | Internal Server Error

#### v2_satellite_facing_config_satellite_name_get.ApiResponseFor200
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
**name** | str,  | str,  |  | [optional] 
**display_name** | str,  | str,  |  | [optional] 
**tunnel_ip_address** | str,  | str,  |  | [optional] 
**keepalive** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**wireguard_public_key** | str,  | str,  |  | [optional] 
**wireguard_private_key** | str,  | str,  |  | [optional] 
**[cidrs](#cidrs)** | list, tuple,  | tuple,  |  | [optional] 
**[access_tiers](#access_tiers)** | list, tuple,  | tuple,  |  | [optional] 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**api_key_id** | str,  | str,  |  | [optional] 
**ssh_ca_public_key** | str,  | str,  |  | [optional] 
**created_by** | str,  | str,  |  | [optional] 
**updated_by** | str,  | str,  |  | [optional] 
**spec** | str,  | str,  |  | [optional] 
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
**satellite_tunnel_peer_id** | str,  | str,  |  | [optional] 
**access_tier_id** | str,  | str,  |  | [optional] 
**wireguard_public_key** | str,  | str,  |  | [optional] 
**endpoint** | str,  | str,  |  | [optional] 
**allowed_ips** | str,  | str,  |  | [optional] 
**access_tier_name** | str,  | str,  |  | [optional] 
**src_nat_cidr_range** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v2_satellite_facing_config_satellite_name_get.ApiResponseFor401
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

#### v2_satellite_facing_config_satellite_name_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_satellite_facing_satellite_name_iptables_put**
<a name="v2_satellite_facing_satellite_name_iptables_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_satellite_facing_satellite_name_iptables_put(satellite_namebody)

 Satellite facing update satellite status

To update the ip table configuration of the satellite to restapiserver

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import satellite_facing_api
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
    api_instance = satellite_facing_api.SatelliteFacingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'satellite_name': "satellite_name_example",
    }
    header_params = {
    }
    body = "# Generated by iptables-save v1.8.4 on Wed Jan 19 16:23:48 2022 *nat :PREROUTING ACCEPT [0:0] :INPUT ACCEPT [0:0] :OUTPUT ACCEPT [179:10835] :POSTROUTING ACCEPT [179:10835] :BANYAN_CONNECTOR_POST - [0:0] :BANYAN_CONNECTOR_PRE - [0:0] [0:0] -A PREROUTING -j BANYAN_CONNECTOR_PRE [179:10835] -A POSTROUTING -j BANYAN_CONNECTOR_POST [0:0] -A BANYAN_CONNECTOR_POST -s 100.120.0.0/32 -j MASQUERADE COMMIT # Completed on Wed Jan 19 16:23:48 2022"
    try:
        #  Satellite facing update satellite status
        api_response = api_instance.v2_satellite_facing_satellite_name_iptables_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SatelliteFacingApi->v2_satellite_facing_satellite_name_iptables_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'satellite_name': "satellite_name_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = "# Generated by iptables-save v1.8.4 on Wed Jan 19 16:23:48 2022 *nat :PREROUTING ACCEPT [0:0] :INPUT ACCEPT [0:0] :OUTPUT ACCEPT [179:10835] :POSTROUTING ACCEPT [179:10835] :BANYAN_CONNECTOR_POST - [0:0] :BANYAN_CONNECTOR_PRE - [0:0] [0:0] -A PREROUTING -j BANYAN_CONNECTOR_PRE [179:10835] -A POSTROUTING -j BANYAN_CONNECTOR_POST [0:0] -A BANYAN_CONNECTOR_POST -s 100.120.0.0/32 -j MASQUERADE COMMIT # Completed on Wed Jan 19 16:23:48 2022"
    try:
        #  Satellite facing update satellite status
        api_response = api_instance.v2_satellite_facing_satellite_name_iptables_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SatelliteFacingApi->v2_satellite_facing_satellite_name_iptables_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyTextPlain] | required |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'text/plain' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyTextPlain

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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
satellite_name | SatelliteNameSchema | | 

# SatelliteNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_satellite_facing_satellite_name_iptables_put.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_satellite_facing_satellite_name_iptables_put.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_satellite_facing_satellite_name_iptables_put.ApiResponseFor500) | Internal Server Error

#### v2_satellite_facing_satellite_name_iptables_put.ApiResponseFor200
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

#### v2_satellite_facing_satellite_name_iptables_put.ApiResponseFor401
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

#### v2_satellite_facing_satellite_name_iptables_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **v2_satellite_facing_satellite_name_status_put**
<a name="v2_satellite_facing_satellite_name_status_put"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v2_satellite_facing_satellite_name_status_put(satellite_nameany_type)

 Satellite facing update satellite status

To update the status of satellite to restapiserver

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import satellite_facing_api
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
    api_instance = satellite_facing_api.SatelliteFacingApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'satellite_name': "satellite_name_example",
    }
    header_params = {
    }
    body = dict(
        connector_version="connector v1.55.0",
        host_info=dict(
            name="vagrant-11111",
            ip_addresses=[
                "11.0.128.17"
            ],
        ),
        peers=[
            dict(
                healthy=True,
                access_tier_id="209b8219-217b-4bfa-b756-227db4c5eb2d",
                public_key="02TWrPbaIqtjp1KaX1+1hcnNpeXz/Qc5NQMmDaM5jk8=",
                endpoint=":51821",
                allowed_ips="3.0.1.0/32",
                latest_handshake="45 seconds ago",
                transfer="269.83 KiB received, 394.69 KiB sent",
            )
        ],
    )
    try:
        #  Satellite facing update satellite status
        api_response = api_instance.v2_satellite_facing_satellite_name_status_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SatelliteFacingApi->v2_satellite_facing_satellite_name_status_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'satellite_name': "satellite_name_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    body = dict(
        connector_version="connector v1.55.0",
        host_info=dict(
            name="vagrant-11111",
            ip_addresses=[
                "11.0.128.17"
            ],
        ),
        peers=[
            dict(
                healthy=True,
                access_tier_id="209b8219-217b-4bfa-b756-227db4c5eb2d",
                public_key="02TWrPbaIqtjp1KaX1+1hcnNpeXz/Qc5NQMmDaM5jk8=",
                endpoint=":51821",
                allowed_ips="3.0.1.0/32",
                latest_handshake="45 seconds ago",
                transfer="269.83 KiB received, 394.69 KiB sent",
            )
        ],
    )
    try:
        #  Satellite facing update satellite status
        api_response = api_instance.v2_satellite_facing_satellite_name_status_put(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SatelliteFacingApi->v2_satellite_facing_satellite_name_status_put: %s\n" % e)
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
**connector_version** | str,  | str,  |  | [optional] 
**[host_info](#host_info)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[peers](#peers)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# host_info

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**[ip_addresses](#ip_addresses)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ip_addresses

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# peers

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
**healthy** | bool,  | BoolClass,  |  | [optional] 
**access_tier_id** | str,  | str,  |  | [optional] 
**public_key** | str,  | str,  |  | [optional] 
**endpoint** | str,  | str,  |  | [optional] 
**allowed_ips** | str,  | str,  |  | [optional] 
**latest_handshake** | str,  | str,  |  | [optional] 
**transfer** | str,  | str,  |  | [optional] 
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
satellite_name | SatelliteNameSchema | | 

# SatelliteNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#v2_satellite_facing_satellite_name_status_put.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#v2_satellite_facing_satellite_name_status_put.ApiResponseFor401) | Status unauthorized
500 | [ApiResponseFor500](#v2_satellite_facing_satellite_name_status_put.ApiResponseFor500) | Internal Server Error

#### v2_satellite_facing_satellite_name_status_put.ApiResponseFor200
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

#### v2_satellite_facing_satellite_name_status_put.ApiResponseFor401
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

#### v2_satellite_facing_satellite_name_status_put.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

