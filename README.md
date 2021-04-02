# DealCloud API Wrapper

This package provides a simple wrapper for interacting with the DealCloud REST API. 

## Installation

The package can be installed through `pip`:
```
pip install dealcloud_api_wrapper
```

The package depends on `requests`, `requests_oauthlib`, and `oauthlib`.

## Example

Using the package is simple:

```python
import dealcloud_api_wrapper 

dc = dealcloud_api_wrapper.Client(hostname='your hostname here', client_id='your client id', client_secret='your client secret')
dc_schema_result = dc.schema_get_entrytypes()
dc_data_result = dc.data_get_row_entry(entryTypeId, query={'your query'}, params={'your params'})
```


