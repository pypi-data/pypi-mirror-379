from pydantic import BaseModel, EmailStr
from typing import Optional

class LoginPayload(BaseModel):
    """
    Payload for login requests.

    Attributes:
        sub: User identifier (email or ID, as per EV_SUB_POLICY).
        email: User's email (optional).
    """
    sub: str
    email: Optional[EmailStr] = None

class LoginPayloadWithPassword(LoginPayload):
    """
    Payload for login requests that includes a password.

    Attributes:
        password: The user's password.
    """
    password: str
