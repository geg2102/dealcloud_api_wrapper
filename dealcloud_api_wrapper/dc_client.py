import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from dealcloud_api_wrapper import dc_schema
from dealcloud_api_wrapper import dc_data
from datetime import datetime, timedelta
import time


_RETRY_STATUSES = set([500, 503, 504])


class Client(dc_schema.Schema, dc_data.Data):
    """ Performs requests to the DealCloud API """


    def __init__(self, hostname, client_id, client_secret, scope=None, retry_timeout=60, **kwargs):
        """
        :param hostname: The hostname of your site. For example, "https://{your-company-name}.dealcloud.com"
        :type client_id: string

        :param client_id: Your client ID.
        :type client_id: integer or string

        :param client_secret: Your client secret. 
        :type client_secret: string

        :param scope: Scope of use for authorization. Must be provided when creating authorization token. 
            Defaults to ['api', 'data'] endpoints.
        :type scope: list or string. 

        :param retry_timeout: Timeout for retry requests (seconds)
        :type retry_timeout: integer.
        """
        if not scope:
            # Default to api and data scopes if not specified.
            self.scope = ["api", "data"]
        else:
            self.scope = scope
        # DealCloud supports client_credentials grant type
        client = BackendApplicationClient(client_id=client_id)
        self.session = OAuth2Session(
            client = client, 
            **kwargs
        )
        self._base_url = hostname
        self._token_url = self._base_url.rstrip('/') + "/api/rest/v1/oauth/token"
        self.client_id = client_id
        self.client_secret = client_secret
        self._get_token(scope=self.scope)
        self.retry_timeout = timedelta(seconds=retry_timeout)


    def _get_token(self, **kwargs):
        """
        Helper function to get initial authorization token.

        :returns: Token dictionary.
        """
        if 'scope' not in kwargs:
            kwargs.update(scope=self.scope)
        return self.session.fetch_token(self._token_url, client_id=self.client_id, client_secret=self.client_secret, **kwargs)


    def _get_response(self, method, endpoint, params=None, json=None, first_request_time= None, retry_counter=0):
        """
        Helper method that extends requests to handle authorization and handle errors.

        :param method: Type of http method being executed. 
        :type method: string

        :param endpoint: DealCloud API endpoint.
        :type endpoint: string

        :param params: Optional parameters in different endpoints. List of Json dictionaries.
        :type params: list.

        :param json: json body for post/put/patch/delete. Could be list of json objects.
        :type json: list or dictionary. 

        :param first_request_time: Time of first request (None if no retries)
        :param first_request_time: datetime.datetime

        :param retry_counter: The number of the current retry. 0 for first attempt.
        :type retry_counter: integer. 

        :returns: response from http request.

        :raises GenericError: When there is an error in the response that hasn't been handled.
        :raises Timeout: When request timed out.
        """
        self._get_token() # Don't need refresh tokens for client_credentials, just get new token on request
        url = f"{self._base_url}{endpoint}"
        
        if not first_request_time:
            first_request_time = datetime.now()

        elapsed = datetime.now() - first_request_time
        if elapsed > self.retry_timeout:
            raise Timeout

        if retry_counter > 0:
            # Delays by 1.5x per iteration, starting at 0.5 when retry_counter=0.
            delay_seconds = 0.5 * 1.5 ** (retry_counter - 1)
            time.sleep(delay_seconds)
        response = getattr(self.session, method)(url, params=params, json=json)

        if response.status_code != requests.codes.ok:
            # 5 retries for server errors
            if response.status_code in _RETRY_STATUSES and retry_counter < 5:
                return self._get_response(method, endpoint, params, json, first_request_time, retry_counter + 1)
            raise GenericError(
                f"There is an error on the API call: {response.json()} \n If the problem persists, try reinitializing client."
            )
        return response


class GenericError(Exception):
    pass


class Timeout(Exception):
    pass
