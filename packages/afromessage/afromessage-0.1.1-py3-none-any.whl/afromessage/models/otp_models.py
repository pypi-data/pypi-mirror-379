# src/afromessage/models/otp_models.py
# This file defines Pydantic models for OTP-related requests, ensuring data validation and type safety.
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional

# Model for initiating an OTP challenge request.
class SendOTPRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    to: str = Field(..., description="Recipient phone number")
    pr: Optional[str] = Field(None, description="Primary route")
    ps: Optional[str] = Field(None, description="Primary sender")
    callback: Optional[str] = Field(None, description="Callback URL")
    sb: Optional[str] = Field(None, description="Secondary brand")
    sa: Optional[str] = Field(None, description="Secondary alias")
    ttl: Optional[int] = Field(None, ge=60, le=3600, description="Time to live in seconds")
    len_: Optional[int] = Field(None, ge=4, le=8, alias="len", description="OTP length")
    t: Optional[str] = Field(None, description="Template")
    from_: Optional[str] = Field(None, alias="from", description="Sender ID")
    sender: Optional[str] = Field(None, description="Sender name")

    # Validate the 'to' field to ensure it follows E.164 format or contains only digits.
    @field_validator("to")
    @classmethod
    def validate_to(cls, v):
        cleaned_phone = v.replace(" ", "")
        if not cleaned_phone.startswith("+") and not cleaned_phone.isdigit():
            raise ValueError("Phone number must be in E.164 format or valid digits")
        return v

    @field_validator("from_", "sender", "pr", "ps", "sb", "sa")
    @classmethod
    def validate_strings(cls, v):
        if v and len(v) > 36:
            raise ValueError("Sender-related fields must be 36 characters or less")
        return v

    # Validate the 't' (template) field to ensure it does not exceed 100 characters.
    @field_validator("t")
    @classmethod
    def validate_template(cls, v):
        if v and len(v) > 100:
            raise ValueError("Template must be 100 characters or less")
        return v

# Model for verifying an OTP code.
class VerifyOTPRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    to: str = Field(..., description="Recipient phone number")
    code: str = Field(..., min_length=4, max_length=8, description="OTP code")

    # Validate the 'to' field to ensure it follows E.164 format or contains only digits.
    @field_validator("to")
    @classmethod
    def validate_to(cls, v):
        cleaned_phone = v.replace(" ", "")
        if not cleaned_phone.startswith("+") and not cleaned_phone.isdigit():
            raise ValueError("Phone number must be in E.164 format or valid digits")
        return v

    # Validate the 'code' field to ensure it contains only numeric characters.
    @field_validator("code")
    @classmethod
    def validate_code(cls, v):
        if not v.isdigit():
            raise ValueError("OTP code must be numeric")
        return v
