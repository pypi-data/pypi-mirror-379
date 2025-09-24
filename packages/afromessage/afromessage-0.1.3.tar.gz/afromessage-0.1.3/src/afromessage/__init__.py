# src/afromessage/__init__.py
from .client import AfroMessage
from .sms import SMS
from .otp import OTP

__version__ = "1.0.0"
__all__ = ["AfroMessage", "SMS", "OTP"]