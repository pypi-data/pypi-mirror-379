from typing import Any, Callable, List, Dict, Text, Optional, Tuple, Union, Awaitable, TypeVar, Type
from datetime import date, datetime, timedelta
from fastapi.responses import JSONResponse
from ewoxcore.client.status_code import StatusCode
from ewoxcore.utils.json_util import JsonUtil
from ewoxservicefastapi.models.request_model import RequestModel
from ewoxservicefastapi.models.response_model import ResponseModel
from ewoxservicefastapi.request_serializer import RequestSerializer
from ewoxservicefastapi.response_serializer import ResponseSerializer

T = TypeVar("T")

class APIFactory:
    @staticmethod
    def create_empty_response_model(
        code: int = int(StatusCode.Ok),
        message: str = "",
        use_compression: bool = True,
        correlation_id: str = ""
    ) -> ResponseModel:
        """ Create an empty ResponseModel. """
        data:str = ""
        response = ResponseModel(
            data,
            code,
            message,
            use_compression,
            correlation_id
        )
        return response


    @staticmethod
    def create_empty_response(
        code: int = int(StatusCode.Ok),
        message: str = "",
        use_compression: bool = True,
        correlation_id: str = "",
        serialize: bool = False
    ) -> Union[str, JSONResponse]:
        """ Create an empty ResponseModel. """
        response:ResponseModel = APIFactory.create_empty_response_model(
            code=code,
            message=message,
            use_compression=use_compression,
            correlation_id=correlation_id
        )

        if (serialize):
            json_data = JsonUtil.serialize(response)
            return json_data
        else:
            json_res:JSONResponse = JSONResponse(content=vars(response))
            return json_res


    @staticmethod
    def create_response_model(
        model: Optional[T],
        code: int = int(StatusCode.Ok),
        message: str = "",
        use_compression: bool = True,
        correlation_id: str = ""
    ) -> ResponseModel:
        """ Create a ResponseModel from a model object. """
        data:str = ""
        if (model is not None):
            data = ResponseSerializer.serialize(model, use_compression)
        else:
            use_compression = False

        response = ResponseModel(
            data,
            code,
            message,
            use_compression,
            correlation_id
        )

        return response

        
    @staticmethod
    def create_response(
        model: Optional[T],
        code: int = int(StatusCode.Ok),
        message: str = "",
        use_compression: bool = True,
        correlation_id: str = "",
        serialize: bool = False
    ) -> Union[str, JSONResponse]:
        """ Create a ResponseModel from a model object. """
        response:ResponseModel = APIFactory.create_response_model(
            model=model,
            code=code,
            message=message,
            use_compression=use_compression,
            correlation_id=correlation_id
        )

        if (serialize):
            json_data = JsonUtil.serialize(response)
            return json_data
        else:
            json_res:JSONResponse = JSONResponse(content=vars(response))
            return json_res

    @staticmethod
    def create_request(
        model: Optional[T],
        use_compression: bool = True,
        correlation_id: str = ""
    ) -> RequestModel:
        """ Create a RequestModel from a model object. """
        response: RequestModel
        if (model is not None):
            response = RequestSerializer.serialize(model, use_compression)
        else:
            data = bytes()
            use_compression = False
        
            response = RequestModel(data, use_compression, correlation_id)

        return response
    

    @staticmethod
    def convert_to_request_model(
        item: dict) -> RequestModel:
        """ Convert a dictionary item to a RequestModel. """
        model:RequestModel = RequestModel(data=item.get("data", b""),
                                          iscompressed=item.get("iscompressed", False),
                                          correlationid=item.get("correlationid", ""))
        return model
    
