from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class MFAVerification(BaseModel):
    code: str = Field(..., min_length=6, max_length=6)


class MFASetup(BaseModel):
    provisioning_uri: str
    secret: str


class MFAChallengeRequest(BaseModel):
    challenge_token:str
    code:str=Field(...,min_length=6, max_length=6)


class MFALoginRequiredResponse(BaseModel):
    mfa_required:bool
    challenge_token:str
    access_token:str
    refresh_token:str
    token_type:str