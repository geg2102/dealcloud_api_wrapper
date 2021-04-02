class Schema():
    """ Methods for calling the Schema endpoint """

    def schema_get_allfields(self):
        """
        Get all fields on all lists from site.

        :returns: json response
        """
        endpoint = "/api/rest/v4/schema/allfields"
        response = self._get_response(method='get', endpoint=endpoint)
        return response.json()


    def schema_get_onefield(self, fieldId):
        """
        Get information for one field. 

        :param fieldId: Field Id. 
        :type fieldId: integer

        :returns: json response
        """
        endpoint = f"/api/rest/v4/schema/fields/{fieldId}"
        response = self._get_response(method='get', endpoint=endpoint)
        return response.json()


    def schema_get_entrytypes(self):
        """
        Get a list of entry types (Contacts, Companies, etc.)

        :returns: json response.
        """
        endpoint = f"/api/rest/v4/schema/entrytypes"
        response = self._get_response(method='get', endpoint=endpoint)
        return response.json()


    def schema_get_fieldtypes(self):
        """
        Get field types supported by DealCloud (user fields)

        :returns: json response.
        """
        endpoint = f"/api/rest/v4/schema/fieldtypes"
        response = self._get_response(method='get', endpoint=endpoint)
        return response.json()


    def schema_get_fields(self, fields: list):
        """
        Get information on a list of fields.

        :param fields: List of fieldIds to get information on.
        :returns: json response.
        """
        fields = '&fieldIds='.join([str(item) for item in fields])
        endpoint = f"/api/rest/v4/schema/fields?fieldIds={fields}"
        response = self._get_response(method='get', endpoint=endpoint)
        return response.json()


    def schema_get_systemfields(self):
        """
        Get types of system fields.

        :returns: json response.
        """
        endpoint = "/api/rest/v4/schema/systemfieldtypes"
        response = self._get_response(method='get', endpoint=endpoint)
        return response.json()


    def schema_get_entrytype_fields(self, entryTypeId):
        """
        Get fields for an entry type.

        :param entryTypeId: entryListID or entry apiName. Required.
        :returns: json response.
        """
        endpoint = f"/api/rest/v4/schema/entrytypes/{entryTypeId}/fields"
        response = self._get_response(method='get', endpoint=endpoint)
        return response.json()


    def schema_get_entrytype_info(self, entryTypeId):
        """
        Get information for one entry type


        :param entryTypeId: entryListID or entry apiName. Required.
        :returns: json response.
        """
        endpoint = f"/api/rest/v4/schema/entrytypes/{entryTypeId}"
        response = self._get_response(method = 'get', endpoint=endpoint)
        return response.json()


    def schema_get_filteroperations(self):
        """
        Get list of filter operations supported by the DealCloud column API

        :returns: json response.
        """
        endpoint = f"/api/rest/v4/schema/filteroperations"
        response = self._get_response(method = 'get', endpoint=endpoint)
        return response.json()


    def schema_post_choicefieldvalues(self, fieldId, choiceValuesToAppend):
        """
        Add values to choice fields.

        :param fieldId: Id of the existing choice field.
        :type fieldId: int.

        :param choiceValuesToAppend: Values which will be appended to choice values of field.
        :type choiceValuesToAppend: list.

        :returns: json response
        """
        endpoint = f"/api/rest/v4/schema/choiceFieldValues/{fieldId}"
        response = self._get_response(method='post', endpoint=endpoint, json=choiceValuesToAppend)
        return response.json()
