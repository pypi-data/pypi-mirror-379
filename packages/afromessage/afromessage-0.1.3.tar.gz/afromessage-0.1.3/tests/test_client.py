import pytest
import requests_mock
from afromessage import AfroMessage
from afromessage.models.sms_models import SendSMSRequest, BulkSMSRequest
from afromessage.models.otp_models import SendOTPRequest

def test_client_initialization():
    """Test that client initializes correctly with token"""
    # Should work with token
    client = AfroMessage(token="test_token")
    assert client.token == "test_token"
    
    # Should fail without token
    with pytest.raises(ValueError):
        AfroMessage(token=None)

def test_client_headers():
    """Test that client sets correct headers"""
    client = AfroMessage(token="test_token")
    assert "Authorization" in client.session.headers
    assert client.session.headers["Authorization"] == "Bearer test_token"