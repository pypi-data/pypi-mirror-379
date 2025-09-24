# tests/test_send_sms.py
import pytest
import requests_mock
from afromessage import AfroMessage
from afromessage.models.sms_models import SendSMSRequest, BulkSMSRequest

def test_send_sms():
    """Test sending an SMS"""
    client = AfroMessage(token="test_token")
    
    with requests_mock.Mocker() as m:
        # Mock the API response
        mock_response = {
            "acknowledge": "success",
            "response": {
                "code": "202",
                "message": "SMS is queued for delivery"
            }
        }
        
        m.post("https://api.afromessage.com/api/send", json=mock_response)
        
        # Test the method with a shorter from_ (e.g., 10 characters)
        request = SendSMSRequest(
            to="+251911500681",
            message="Test message",
            from_="testSender",
            sender="TestSender"
        )
        response = client.sms.send(request)
        
        # Verify the request was made correctly
        assert m.called
        assert m.last_request.method == "POST"
        assert "to" in m.last_request.json()
        assert m.last_request.json()["to"] == "+251911500681"
        
        # Verify the response
        assert response["acknowledge"] == "success"
def test_send_sms_get():
    """Test sending an SMS via GET"""
    client = AfroMessage(token="test_token")
    
    with requests_mock.Mocker() as m:
        mock_response = {
            "acknowledge": "success",
            "response": {
                "code": "202",
                "message": "SMS is queued for delivery"
            }
        }
        
        m.get("https://api.afromessage.com/api/send", json=mock_response)
        
        request = SendSMSRequest(
            to="+251911500681",
            message="Test message",
            from_="testSender",
            sender="TestSender"
        )
        response = client.sms.send_get(request)
        
        assert m.called
        assert m.last_request.method == "GET"
        assert "to" in m.last_request.qs
        assert m.last_request.qs["to"][0] == "+251911500681"
        
        assert response["acknowledge"] == "success"

def test_bulk_send_sms():
    """Test sending bulk SMS"""
    client = AfroMessage(token="test_token")
    
    with requests_mock.Mocker() as m:
        # Mock the API response
        mock_response = {
            "acknowledge": "success",
            "response": {
                "code": "202",
                "message": "SMS is queued for delivery"
            }
        }
        
        m.post("https://api.afromessage.com/api/bulk_send", json=mock_response)
        
        # Test the method with a shorter from_ (e.g., 10 characters)
        request = BulkSMSRequest(
            to=["+251911500681"],
            message="Test message",
            from_="testSender",
            sender="TestSender",
            campaign="TestCampaign"
        )
        response = client.sms.bulk_send(request)
        
        # Verify the request was made correctly
        assert m.called
        assert m.last_request.method == "POST"
        assert "to" in m.last_request.json()
        assert m.last_request.json()["to"] == ["+251911500681"]
        
        # Verify the response
        assert response["acknowledge"] == "success"