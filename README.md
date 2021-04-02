# DealCloud API Wrapper

This package provides a simple wrapper for interacting with the DealCloud REST API. 

## Installation

The package can be installed through `pip`:
```
pip install dealcloud-api-wrapper
```

The package depends on `requests`, `requests_oauthlib`, and `oauthlib`.

## Example

Using the package is simple:

```python
from dealcloud_api_wrapper import dc_client

# Initialize Client object
dc = dc_client.Client(hostname='your hostname here', client_id='your client id', client_secret='your client secret')

# Call schema/data methods (more examples in dc_schema and dc_data classes)
dc_schema_result = dc.schema_get_entrytypes()
dc_data_result = dc.data_get_row_entry(entryTypeId, query={'your query'}, params={'your params'})
```


