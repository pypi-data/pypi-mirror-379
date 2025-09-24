# src/afromessage/client.py
# This file defines the main AfroMessage client class, handling API session management and request routing.
import requests
from .sms import SMS
from .otp import OTP
from .utils import handle_error, log_request, log_response

class AfroMessage:
    def __init__(self, token, base_url="https://api.afromessage.com/api/"):
        # Validate that a token is provided, raising an error if absent.
        if not token:
            raise ValueError("AfroMessage token is required")

        self.token = token
        self.base_url = base_url

        # Create a session with default headers for API authentication and content type.
        self.session = requests.Session()
        self.session.headers.update(
            {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        )
        self.session.timeout = 120  # Set timeout to 120 seconds

        # Initialize API modules for SMS and OTP functionality.
        self.sms = SMS(self)
        self.otp = OTP(self)

    def request(self, method, endpoint, **kwargs):
        # Construct the full URL and perform the HTTP request, raising an exception for status errors.
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response

    def get(self, endpoint, **kwargs):
        # Convenience method for making GET requests.
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        # Convenience method for making POST requests.
        return self.request("POST", endpoint, **kwargs)