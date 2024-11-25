from pydantic import BaseModel, EmailStr, field_validator
from datetime import date

class UserSchema(BaseModel):
    """
    Schema to validate user data using Pydantic.
    Ensures data consistency and type validation.
    """
    first_name: str
    last_name: str
    dob: date
    gender: str
    address: str
    email: EmailStr
    phone_number: str

    # Custom validator for phone number
    @field_validator("phone_number")
    def validate_phone_number(cls, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be exactly 10 digits.")
        
        return value