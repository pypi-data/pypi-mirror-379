# src/afromessage/models/sms_models.py
# This file defines Pydantic models for SMS-related requests, ensuring data validation and type safety.
from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, Union, List


# Model for sending a single SMS request.
class SendSMSRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    to: Union[str, List[str]] = Field(..., description="Recipient phone number(s)")
    message: str = Field(
        ..., min_length=1, max_length=1600, description="Message content"
    )
    callback: Optional[str] = Field(None, description="Callback URL")
    from_: Optional[str] = Field(None, alias="from", description="Sender ID")
    sender: Optional[str] = Field(None, description="Sender name")
    template: Optional[int] = Field(0, ge=0, description="Template ID")

    # Validate the 'to' field to ensure it follows E.164 format or contains only digits for single or multiple recipients.
    @field_validator("to")
    @classmethod
    def validate_to(cls, v):
        if isinstance(v, str):
            if not v.startswith("+") and not v.replace(" ", "").isdigit():
                raise ValueError("Phone number must be in E.164 format or valid digits")
        elif isinstance(v, list):
            for phone in v:
                cleaned_phone = phone.replace(" ", "")
                if not cleaned_phone.startswith("+") and not cleaned_phone.isdigit():
                    raise ValueError(
                        "All phone numbers must be in E.164 format or valid digits"
                    )
        else:
            raise ValueError("to must be a string or list of strings")
        return v

    # Validate sender-related fields to ensure they do not exceed 11 characters.
    @field_validator("from_", "sender")
    @classmethod
    def validate_sender(cls, v):
        if v and len(v) > 36:
            raise ValueError("Sender ID or name must be 36 characters or less")
        return v


# Model for a single recipient with a personalized message in a bulk campaign.
class BulkRecipient(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    to: str = Field(..., description="Recipient phone number")
    message: str = Field(
        ..., min_length=1, max_length=1600, description="Personalized message content"
    )

    # Validate the 'to' field to ensure it follows E.164 format or contains only digits.
    @field_validator("to")
    @classmethod
    def validate_to(cls, v):
        cleaned_phone = v.replace(" ", "")
        if not cleaned_phone.startswith("+") and not cleaned_phone.isdigit():
            raise ValueError("Phone number must be in E.164 format or valid digits")
        return v


# Model for sending bulk SMS requests, supporting both personalized and uniform messages.
class BulkSMSRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    to: Union[List[str], List[BulkRecipient]] = Field(
        ..., description="List of recipient phone numbers or recipient-message pairs"
    )
    message: Optional[str] = Field(
        None,
        min_length=1,
        max_length=1600,
        description="Uniform message content for all recipients",
    )
    from_: Optional[str] = Field(None, alias="from", description="Sender ID")
    sender: Optional[str] = Field(None, description="Sender name")
    campaign: Optional[str] = Field(None, max_length=100, description="Campaign name")
    createCallback: Optional[str] = Field(
        None, description="Callback URL for campaign action"
    )
    statusCallback: Optional[str] = Field(
        None, description="Callback URL for message status"
    )

    # Validate the 'to' field based on its type (list of strings or list of BulkRecipient).
    @field_validator("to")
    @classmethod
    def validate_to(cls, v):
        if isinstance(v, list):
            if all(isinstance(item, str) for item in v):
                for phone in v:
                    cleaned_phone = phone.replace(" ", "")
                    if (
                        not cleaned_phone.startswith("+")
                        and not cleaned_phone.isdigit()
                    ):
                        raise ValueError(
                            "All phone numbers must be in E.164 format or valid digits"
                        )
            elif all(isinstance(item, BulkRecipient) for item in v):
                for recipient in v:
                    cleaned_phone = recipient.to.replace(" ", "")
                    if (
                        not cleaned_phone.startswith("+")
                        and not cleaned_phone.isdigit()
                    ):
                        raise ValueError(
                            "All phone numbers in recipient list must be in E.164 format or valid digits"
                        )
            else:
                raise ValueError(
                    "to must be a list of strings or a list of BulkRecipient objects"
                )
        return v

    # Validate sender-related fields to ensure they do not exceed 11 characters.
    @field_validator("from_", "sender")
    @classmethod
    def validate_sender(cls, v):
        if v and len(v) > 36:
            raise ValueError("Sender ID or name must be 36 characters or less")
        return v

    @field_validator("message")
    @classmethod
    def validate_message(cls, v, values):
        to_value = values.data.get("to")
        if not v and to_value and all(isinstance(item, str) for item in to_value):
            raise ValueError("Message is required when sending uniform bulk SMS")
        return v
