import json
import asyncio
import logging
import time
from typing import List, Dict, Any
from functools import wraps
from opencensus.ext.azure.log_exporter import AzureLogHandler
from Osdental.InternalHttp.Request import CustomRequest
from Osdental.InternalHttp.Response import CustomResponse
from Osdental.Encryptor.Rsa import RSAEncryptor
from Osdental.Exception.ControlledException import OSDException, RSAEncryptException, AESEncryptException
from Osdental.Encryptor.Aes import AES
from Osdental.Shared.Utils.TextProcessor import TextProcessor
from Osdental.Shared.Logger import logger
from Osdental.Models.Legacy import Legacy
from Osdental.Grpc.Client.PortalClient import PortalClient
from Osdental.Shared.Enums.Code import Code
from Osdental.Shared.Config import Config

portal_client = PortalClient()
aes = AES()

logger = logging.getLogger('graphql')
logger.setLevel(logging.INFO)

if not logger.handlers:  # evitar múltiples handlers si se recarga la app
    logger.addHandler(AzureLogHandler(
        connection_string=f'InstrumentationKey={Config.INSTRUMENTATION_KEY}'
    ))

def split_into_batches(data: List[Any], batch:int = 250):
    for i in range(0, len(data), batch):
        yield data[i:i + batch]

def try_decrypt_or_return_raw(data: str, private_key_rsa: str, aes_key: str) -> str:
    try:
        return RSAEncryptor.decrypt(data, private_key_rsa, silent=True)
    except RSAEncryptException:
        try:
            return aes.decrypt(aes_key, data, silent=True)
        except AESEncryptException:
            return data

def enqueue_response(data: Any, batch: int, headers: Dict[str,str], msg_info: str = None):
    if data and isinstance(data, list):
        if batch > 0 and len(data) > batch:
            batches = split_into_batches(data, batch)
            for idx, data_batch in enumerate(batches, start=1):
                custom_response = CustomResponse(content=json.dumps(data_batch), headers=headers, batch=idx)
                _ = asyncio.create_task(custom_response.send_to_service_bus())
        else:
            custom_response = CustomResponse(content=json.dumps(data), headers=headers)
            _ = asyncio.create_task(custom_response.send_to_service_bus())
    else:
        content = json.dumps(data) if isinstance(data, dict) else msg_info
        custom_response = CustomResponse(content=content, headers=headers)
        _ = asyncio.create_task(custom_response.send_to_service_bus())

def handle_audit_and_exception(batch: int = 0):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                start_time = time.time()
                headers = {}

                res = await portal_client.get_legacy()
                data = json.loads(res.data)
                legacy = Legacy.from_db(data) if res.status == Code.PROCESS_SUCCESS_CODE else None

                _, info = args[:2] 
                request = info.context.get('request')
                headers = info.context.get('headers') or {}
                operation_name = 'UnknownOperation'
                if request:
                    body = await request.body()
                    try:
                        body_data = json.loads(body.decode("utf-8"))
                        operation_name = body_data.get('operationName', 'UnknownOperation')
                    except Exception:
                        pass

                    custom_request = CustomRequest(request)
                    await custom_request.send_to_service_bus()

                response = await func(*args, **kwargs)
                msg_info = TextProcessor.concatenate(response.get('status'), '-', response.get('message'))
                raw_data = response.get('data')
                data = None
                if raw_data:
                    data = try_decrypt_or_return_raw(raw_data, legacy.private_key2, legacy.aes_key_auth)

                enqueue_response(data, batch, headers, msg_info)
                duration = (time.time() - start_time) * 1000

                logger.info('GraphQL request completed', extra={
                    'custom_dimensions': {
                        'operationName': operation_name,
                        'status': response.get('status'),
                        'message': response.get('message'),
                        'duration_ms': duration
                    }
                })

                return response

            except OSDException as ex:
                logger.warning('Controlled server error', extra={
                    'custom_dimensions': {
                        'error': str(ex.error),
                        'operationName': operation_name
                    }
                })
                ex.headers = headers
                _ = asyncio.create_task(ex.send_to_service_bus())
                return ex.get_response()
            
            except Exception as e:
                logger.error('Unexpected server error', extra={
                    'custom_dimensions': {
                        'error': str(e),
                        'operationName': operation_name
                    }
                })                
                ex = OSDException(error=str(e), headers=headers)
                _ = asyncio.create_task(ex.send_to_service_bus())
                return ex.get_response()

        return wrapper
    return decorator