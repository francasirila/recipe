from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    username: Optional[str] = None
    email: EmailStr
    password: str = Field(...,min_length=8,max_length=128)



class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"



class MFARequiredResponse(BaseModel):
    mfa_required: bool = True
    challenge_token: str
    token_type: str = "bearer"