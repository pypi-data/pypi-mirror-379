# src/afromessage/otp.py
from .utils import handle_error, log_request, log_response
from .models.otp_models import SendOTPRequest, VerifyOTPRequest

class OTP:
    def __init__(self, client):
        self.client = client

    def send(self, request: SendOTPRequest):
        """Initiate an OTP challenge using a request model"""
        try:
            # Custom serialization to handle from field properly
            params = request.model_dump(by_alias=True, exclude_none=True)
            # Ensure 'from' field is included even if empty
            if request.from_ is not None and "from" not in params:
                params["from"] = request.from_
            
            log_request("challenge", "get", params)

            response = self.client.get("challenge", params=params)
            response_data = response.json()

            log_response("otp", response_data)
            return response_data
        except Exception as err:
            raise handle_error(err)

    def verify(self, request: VerifyOTPRequest):
        """Verify an OTP code using a request model"""
        try:
            params = request.model_dump(by_alias=True, exclude_none=True)
            log_request("verify", "get", params)

            response = self.client.get("verify", params=params)
            response_data = response.json()

            log_response("verify", response_data)
            return response_data
        except Exception as err:
            raise handle_error(err)
