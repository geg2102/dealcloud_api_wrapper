from requests.utils import requote_uri


class Data():
    """ Methods for calling the Data endpoint """
    def data_get_entries(self, entryTypeId):
        """
        Get Record Ids for a given entry type

        :param entryTypeId: entryListID or entry apiName. Required.
        :returns: json response
        """
        endpoint = f"/api/rest/v4/data/entrydata/{entryTypeId}/entries"
        response = self._get_response(method='get', endpoint=endpoint)
        return response.json()


    def data_get_row_entry(self, entryTypeId, query={}, params=None):
        """
        Returns records with attributes as properties, can specify attributes to return.

        :param entryTypeId: entryListID or entry apiName. Required.
        :type entryTypeId: Str or int.

        :param query: Optional. Query to pass to endpoint.
        :type query: Dict. Example: {"STRCode": 4463}

        :param params: Optional. Parameters include:
            fields (array)
            limit (integer)
            skip (integer)
            resolveReferenceUrls (boolean)
            fillExtendedData (boolean)
        :returns: json response.
        """
        endpoint = f"/api/rest/v4/data/entrydata/rows/{entryTypeId}?"
        if query != {}:
            endpoint = endpoint + requote_uri(f"query= {query}")
        response = self._get_response(method='get', endpoint=endpoint, params=params)
        return response.json()


    def data_get_entry_history(self, entryTypeId, modifiedSince):
        """
        Get Record Ids for entries that were modified or deleted. 

        :param entryTypeId: entryListID or entry apiName. Required.

        :param modifiedSince: Date since modified
        :type modifiedSince: datetime.

        :returns: response.json
        """
        modifiedSince = requote_uri(modifiedSince)
        endpoint = f"/api/rest/v4/data/entrydata/{entryTypeId}/entries/history?modifiedSince={modifiedSince}"
        response = self._get_response(method='get', endpoint=endpoint)
        return response.json()


    def data_get_entry_fields(self, entryId, fieldId):
        """
        Gets specified field of given entry. 

        :param entryId: Record Id for a given entry. 
        :type entryId: int.
        :param fieldId: Field to get data about.
        :returns: json response
        """
        endpoint = f"/api/rest/v4/data/entryfiles/{entryId}/fields/{fieldId}"
        response = self._get_response(method='get', endpoint=endpoint)
        return response.json()


    def data_get_row_view(self, query={}, params=None):
        """
        Returns views of rows

        :param query: Optional. Query to pass to endpoint.
        :type query: Dict. Example: {"STRCode": 4463}

        :param params: Optional. Parameters include:
            isPrivate (boolean)
            limit (integer)
            skip (integer)
        :returns: json response.
        """
        endpoint = f"/api/rest/v4/data/rows/view"
        if query != {}:
            endpoint = endpoint + requote_uri(f"query= {query}")
        response = self._get_response(method='get', endpoint=endpoint, params=params)
        return response.json()


    def data_post_entrytype_filter(self, entryTypeId, filters=[]):
        """
        Takes an array of filterOperations, returns Record Ids using advanced filter.
        This method supports filters returned by the /filterOperations endpoint from Schema.

        :param entryTypeId: entryListID or entry apiName.
        :type entryTypeId: String or int.
        :param filters: Filter parameter of post method. Required. Example format:
            [
                {
                    "fieldId": 14984
                    "value": 20529, 
                    "valueTo": {}, 
                    "currencyCode": "string", 
                    "filterOperation": 0
                }
            ]
        :type filters: list of json dictionaries.
        :returns: json response
        """
        endpoint = f"/api/rest/v4/data/entrydata/{entryTypeId}/filter"
        response = self._get_response(method='post', endpoint=endpoint, json=filters)
        return response.json()


    def data_post_row_entry(self, entryTypeId, rows=[]):
        """
        Creates new record

        :param entryTypeId: entryListID or entry apiName. Required.
        :param rows: Json body of update. Required. Example:
        [
          {
            "entryId": 0,
            "errors": [
              {
                "field": "string",
                "code": 0,
                "description": "string"
              }
            ],
            "comparer": {},
            "count": 0,
            "keys": [
              "string"
            ],
            "values": [
              {}
            ]
          }
        ]
        :type rows: list of dictionaries.
        :returns: json response.
        """
        endpoint = f"/api/rest/v4/data/entrydata/rows/{entryTypeId}"
        response = self._get_response(method='post', endpoint=endpoint, json=rows)
        return response.json()


    def data_patch_row_entry(self, entryTypeId, rows=[]):
        """
        Updates existing record

        :param entryTypeId: entryListID or entry apiName. Required.
        :param rows: Json body of update. Required. Example:
        [
          {
            "entryId": 0,
            "errors": [
              {
                "field": "string",
                "code": 0,
                "description": "string"
              }
            ],
            "comparer": {},
            "count": 0,
            "keys": [
              "string"
            ],
            "values": [
              {}
            ]
          }
        ]
        :returns: json response.
        """        
        endpoint = f"/api/rest/v4/data/entrydata/rows/{entryTypeId}"
        response = self._get_response(method='patch', endpoint=endpoint, json=rows)
        return response.json()


    def data_delete_entry(self, entryTypeId, idsToDelete: list, confirm=True):
        """
        Method for deleting record(s).

        :param entryTypeId: entryListID or entry apiName. Required.
        :param idsToDelete: list of IDs to delete. Required.
        :param confirm: boolean. If true, prompts user if they are sure they want to delete.
        :returns: response.json()
        """
        user_check = ""
        if confirm:
            user_check = input(f"Are you sure you want to delete the {len(idsToDelete)} entries? \n")
        if user_check not in ["Yes", "yes", "y", "Y"]:
            return 
        endpoint = f"/api/rest/v4/data/entrydata/{entryTypeId}"
        response = self._get_response(method='delete', endpoint=endpoint, json=idsToDelete)
        return response.json()
