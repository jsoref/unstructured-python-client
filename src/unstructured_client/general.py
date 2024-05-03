"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from typing import List, Optional
from unstructured_client import utils
from unstructured_client._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext, HookContext
from unstructured_client.models import errors, operations, shared

class General:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def partition(self, request: operations.PartitionRequest, retries: Optional[utils.RetryConfig] = None) -> operations.PartitionResponse:
        r"""Summary
        Description
        """
        hook_ctx = HookContext(operation_id='partition', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/general/v0/general'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, operations.PartitionRequest, "partition_parameters", False, False, 'multipart')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        global_retry_config = self.sdk_configuration.retry_config
        retry_config = retries
        if retry_config is None:
            if global_retry_config:
                retry_config = global_retry_config
            else:
                retry_config = utils.RetryConfig('backoff', utils.BackoffStrategy(500, 60000, 1.5, 900000), True)

        req = None
        def do_request():
            nonlocal req
            try:
                req = client.prepare_request(requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers))
                req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
                http_res = client.send(req)
            except Exception as e:
                _, err = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
                if err is not None:
                    raise err from e
                raise e

            if utils.match_status_codes(['422','4XX','5XX'], http_res.status_code):
                result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
                if e is not None:
                    raise e
                if result is not None:
                    http_res = result
                else:
                    raise errors.SDKError('Unexpected error occurred', -1, '', None)
            else:
                http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)

            return http_res

        http_res = utils.retry(do_request, utils.Retries(retry_config, [
            '5xx'
        ]))
        
        
        res = operations.PartitionResponse(status_code=http_res.status_code, content_type=http_res.headers.get('Content-Type') or '', raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[List[shared.Element]])
                res.response_partition_parameters = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 422:
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, errors.HTTPValidationError)
                raise out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    

