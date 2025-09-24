# src/afromessage/utils.py
# This file contains utility functions for error handling and request/response logging.
import json
import logging

# Configure basic logging with INFO level.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handle_error(err):
    """Handle API errors by logging details and raising an appropriate exception."""
    if hasattr(err, "response") and err.response is not None:
        logger.error(
            "❌ API Error Details: %s",
            {
                "status": err.response.status_code,
                "data": err.response.text,
                "headers": dict(err.response.headers),
            },
        )
        return Exception(f"API Error: {err.response.status_code} - {err.response.text}")
    logger.error("❌ Network Error: %s", str(err))
    return Exception(f"Network Error: {str(err)}")

def log_request(endpoint, method, payload):
    """Log API request details including method, endpoint, and payload."""
    logger.info("📤 [%s] Request to: %s", method.upper(), endpoint)
    logger.info("   Payload: %s", json.dumps(payload, indent=2))

def log_response(endpoint, response):
    """Log API response details including endpoint and response data."""
    logger.info("📥 Response from: %s", endpoint)
    logger.info("   Data: %s", json.dumps(response, indent=2))