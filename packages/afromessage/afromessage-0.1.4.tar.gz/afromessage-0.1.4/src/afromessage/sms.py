# src/afromessage/sms.py
from .utils import handle_error, log_request, log_response
from .models.sms_models import SendSMSRequest, BulkSMSRequest

class SMS:
    def __init__(self, client):
        self.client = client

    def send(self, request: SendSMSRequest):
        """Send a single SMS using a request model via POST"""
        try:
            # Custom serialization to handle from field properly
            body = request.model_dump(by_alias=True, exclude_none=True)
            # Ensure 'from' field is included even if empty
            if request.from_ is not None and "from" not in body:
                body["from"] = request.from_
            
            log_request("send", "post", body)

            response = self.client.post("send", json=body)
            response_data = response.json()

            log_response("send", response_data)
            return response_data
        except Exception as err:
            raise handle_error(err)

    def send_get(self, request: SendSMSRequest):
        """Send a single SMS using a request model via GET"""
        try:
            # Custom serialization to handle from field properly
            params = request.model_dump(by_alias=True, exclude_none=True)
            # Ensure 'from' field is included even if empty
            if request.from_ is not None and "from" not in params:
                params["from"] = request.from_
            
            log_request("send", "get", params)

            response = self.client.get("send", params=params)
            response_data = response.json()

            log_response("send", response_data)
            return response_data
        except Exception as err:
            raise handle_error(err)

    def bulk_send(self, request: BulkSMSRequest):
        """Send bulk SMS using a request model"""
        try:
            # Custom serialization to handle from field properly
            body = request.model_dump(by_alias=True, exclude_none=True)
            # Ensure 'from' field is included even if empty (required for bulk)
            if request.from_ is not None and "from" not in body:
                body["from"] = request.from_
            
            log_request("bulk_send", "post", body)

            response = self.client.post("bulk_send", json=body)
            response_data = response.json()

            log_response("bulk_send", response_data)
            return response_data
        except Exception as err:
            raise handle_error(err)
