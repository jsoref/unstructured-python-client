"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from typing import Any, List, Optional
from unstructured_client import utils
from unstructured_client.models import errors, operations, shared
from unstructured_client.utils._human_utils import suggest_defining_url_if_401  # human code

class General:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    @suggest_defining_url_if_401  # human code
    def partition(self, request: Optional[shared.PartitionParameters], retries: Optional[utils.RetryConfig] = None) -> operations.PartitionResponse:
        r"""Pipeline 1"""
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/general/v0/general'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, Optional[shared.PartitionParameters], "request", False, True, 'multipart')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 900000), True)

        def do_request():
            return client.request('POST', url, data=data, files=form, headers=headers)

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '5xx'
        ]))
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.PartitionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[List[Any]])
                res.elements = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
