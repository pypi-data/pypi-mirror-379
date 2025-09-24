# tests/test_challenge_otp.py
import pytest
import requests_mock
from afromessage import AfroMessage
from afromessage.models.otp_models import SendOTPRequest, VerifyOTPRequest

def test_challenge_otp():
    """Test initiating an OTP challenge"""
    client = AfroMessage(token="test_token")
    
    with requests_mock.Mocker() as m:
        # Mock the API response
        mock_response = {
            "acknowledge": "success",
            "response": {
                "code": "202",
                "to": "+251911500681",
                "request": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
            }
        }
        
        m.get("https://api.afromessage.com/api/challenge", json=mock_response)
        
        # Test the method with a shorter pr (e.g., 10 characters)
        request = SendOTPRequest(to="+251911500681", pr="Your code", len_=6)
        response = client.otp.send(request)
        
        # Verify the request was made correctly
        assert m.called
        assert m.last_request.method == "GET"
        assert "to" in m.last_request.qs
        assert m.last_request.qs["to"][0] == "+251911500681"
        
        # Verify the response
        assert response["acknowledge"] == "success"