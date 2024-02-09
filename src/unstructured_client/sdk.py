"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .general import General
from .sdkconfiguration import SDKConfiguration
from typing import Callable, Dict, Union
from unstructured_client import utils
from unstructured_client.models import shared
from unstructured_client.utils._human_utils import clean_server_url  # human code

class UnstructuredClient:
    r"""Unstructured Pipeline API: Partition documents with the Unstructured library"""
    general: General

    sdk_configuration: SDKConfiguration

    @clean_server_url  # human code
    def __init__(self,
                 api_key_auth: Union[str, Callable[[], str]],
                 server: str = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param api_key_auth: The api_key_auth required for authentication
        :type api_key_auth: Union[str, Callable[[], str]]
        :param server: The server by name to use for all operations
        :type server: str
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        if callable(api_key_auth):
            def security():
                return shared.Security(api_key_auth = api_key_auth())
        else:
            security = shared.Security(api_key_auth = api_key_auth)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security, server_url, server, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.general = General(self.sdk_configuration)
    
