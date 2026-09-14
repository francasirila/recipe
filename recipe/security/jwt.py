import os
from datetime import datetime, timedelta, timezone 
from uuid import UUID 
from dotenv import load_dotenv 
from jose import JWTError, jwt 


load_dotenv() 

SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORITHM = os.getenv("ALGORITHM", "HS256") 

ACCESS_TOKEN_EXPIRE_MINUTES = int( 
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30") ) 

MFA_CHALLENGE_EXPIRE_MINUTES = int(
    os.getenv("MFA_CHALLENGE_EXPIRE_MINUTES", "5")
)
    

REFRESH_TOKEN_EXPIRE_DAYS = 7 

if not SECRET_KEY: 
    raise RuntimeError("SECRET_KEY is not configured")

def create_access_token(user_id: UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "type": "access",
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def create_refresh_token(user_id: UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        days=REFRESH_TOKEN_EXPIRE_DAYS
    )

    payload = {
        "sub": str(user_id),
        "type": "refresh",
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def create_mfa_challenge_token(user_id: UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=MFA_CHALLENGE_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "type": "mfa_challenge",
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except JWTError:
        return {}