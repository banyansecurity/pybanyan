<a name="__pageTop"></a>
# openapi_client.apis.tags.audit_log_api.AuditLogApi

All URIs are relative to *https://dev02.console.bnntest.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_audit_logs_get**](#v1_audit_logs_get) | **get** /v1/audit_logs |  Get Audit Logs

# **v1_audit_logs_get**
<a name="v1_audit_logs_get"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} v1_audit_logs_get()

 Get Audit Logs

Banyan records system activity related to your organization to provide an audit trail. This endpoint returns admin audit logs according to your specific filters and parameters.

### Example

* Bearer (JWT) Authentication (bearerAuthToken):
```python
import openapi_client
from openapi_client.apis.tags import audit_log_api
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
    api_instance = audit_log_api.AuditLogApi(api_client)

    # example passing only optional values
    query_params = {
        '&#x60;action&#x60;': "`action`_example",
        '&#x60;admin_email&#x60;': "`admin_email`_example",
        '&#x60;end_time &#x60;': 1,
        '&#x60;limit&#x60;': 1,
        '&#x60;skip&#x60;': 1,
        '&#x60;start_time&#x60;': 1,
        '&#x60;type&#x60;': "`type`_example",
        '&#x60;org_id&#x60;': "`org_id`_example",
        '&#x60;order&#x60;': "`order`_example",
    }
    header_params = {
        'Authorization': "Authorization_example",
    }
    try:
        #  Get Audit Logs
        api_response = api_instance.v1_audit_logs_get(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AuditLogApi->v1_audit_logs_get: %s\n" % e)
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
&#x60;action&#x60; | ActionSchema | | optional
&#x60;admin_email&#x60; | AdminEmailSchema | | optional
&#x60;end_time &#x60; | EndTimeSchema | | optional
&#x60;limit&#x60; | LimitSchema | | optional
&#x60;skip&#x60; | SkipSchema | | optional
&#x60;start_time&#x60; | StartTimeSchema | | optional
&#x60;type&#x60; | TypeSchema | | optional
&#x60;org_id&#x60; | OrgIdSchema | | optional
&#x60;order&#x60; | OrderSchema | | optional


# ActionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AdminEmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EndTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

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

# StartTimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrderSchema

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
200 | [ApiResponseFor200](#v1_audit_logs_get.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#v1_audit_logs_get.ApiResponseFor400) | Bad request
401 | [ApiResponseFor401](#v1_audit_logs_get.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#v1_audit_logs_get.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#v1_audit_logs_get.ApiResponseFor500) | Internal Server Error

#### v1_audit_logs_get.ApiResponseFor200
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
**[auditlogs](#auditlogs)** | list, tuple,  | tuple,  |  | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# auditlogs

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
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**message** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] 
**action** | str,  | str,  |  | [optional] 
**admin_email** | str,  | str,  |  | [optional] 
**[changes_new](#changes_new)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[changes_old](#changes_old)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**token_unique_id** | str,  | str,  |  | [optional] 
**token_iat** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**token_auth_issuer** | str,  | str,  |  | [optional] 
**client_ip_address** | str,  | str,  |  | [optional] 
**client_user_agent** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# changes_new

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[config](#config)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**protocol** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# config

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ClientID** | str,  | str,  |  | [optional] 
**ClientSecret** | str,  | str,  |  | [optional] 
**IssuerURL** | str,  | str,  |  | [optional] 
**RedirectURL** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# changes_old

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[config](#config)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**protocol** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# config

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ClientID** | str,  | str,  |  | [optional] 
**ClientSecret** | str,  | str,  |  | [optional] 
**IssuerURL** | str,  | str,  |  | [optional] 
**RedirectURL** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### v1_audit_logs_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_audit_logs_get.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_audit_logs_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### v1_audit_logs_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[bearerAuthToken](../../../README.md#bearerAuthToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

