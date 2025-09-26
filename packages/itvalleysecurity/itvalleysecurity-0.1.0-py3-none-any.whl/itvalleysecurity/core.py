from datetime import timedelta
from typing import Optional, Dict, Any
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from .config import SETTINGS
from .utils import now_utc, EMAIL_RX, UUID_RX
from .typing import TokenPair
from .exceptions import InvalidToken

def _validate_sub(sub: str):
    if not sub:
        raise ValueError("sub is required.")
    if SETTINGS.EV_SUB_POLICY == "email" and not EMAIL_RX.match(sub):
        raise ValueError("Invalid sub: email expected (EV_SUB_POLICY=email).")
    if SETTINGS.EV_SUB_POLICY == "uuid" and not UUID_RX.match(sub):
        raise ValueError("Invalid sub: UUID expected (EV_SUB_POLICY=uuid).")

def _encode(payload: dict) -> str:
    return jwt.encode(payload, SETTINGS.JWT_SECRET_KEY, algorithm=SETTINGS.JWT_ALGORITHM)

def _exp(minutes: Optional[int]=None, days: Optional[int]=None):
    if days is not None:
        return now_utc() + timedelta(days=days)
    return now_utc() + timedelta(minutes=minutes or SETTINGS.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)

def issue_pair(sub: str, email: Optional[str]=None, **extra) -> TokenPair:
    """
    Generates a JWT token pair (access and refresh).

    Args:
        sub: User identifier (email or ID).
        email: User's email (optional).
        **extra: Additional claims to include in the token.

    Returns:
        TokenPair: A dictionary with access_token, refresh_token, and metadata.
    """
    _validate_sub(sub)
    aexp = _exp(minutes=SETTINGS.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    rexp = _exp(days=SETTINGS.JWT_REFRESH_TOKEN_EXPIRE_DAYS)

    access_payload = {
        "sub": sub, "email": email, "type": "access", "iss": SETTINGS.JWT_ISSUER,
        "iat": now_utc(), "nbf": now_utc(), "exp": aexp,
    } | extra
    refresh_payload = {
        "sub": sub, "type": "refresh", "iss": SETTINGS.JWT_ISSUER,
        "iat": now_utc(), "nbf": now_utc(), "exp": rexp,
    } | {k: v for k, v in extra.items() if k != "email"}

    return {
        "access_token": _encode(access_payload),
        "refresh_token": _encode(refresh_payload),
        "token_type": "bearer",
        "access_expires_at": aexp.isoformat(),
        "refresh_expires_at": rexp.isoformat(),
    }

def _verify(token: str) -> dict:
    return jwt.decode(
        token,
        SETTINGS.JWT_SECRET_KEY,
        algorithms=[SETTINGS.JWT_ALGORITHM],
        options={"require": ["exp","iat","nbf"], "verify_signature": True,
                 "verify_exp": True, "verify_iat": True, "verify_nbf": True}
    )

def verify_access(token: str) -> dict:
    """
    Verifies and decodes an access token.

    Args:
        token: The JWT access token.

    Returns:
        dict: The decoded token claims.

    Raises:
        InvalidToken: If the token is invalid or expired.
    """
    try:
        payload = _verify(token)
        if payload.get("type") != "access": 
            raise InvalidToken("Incorrect token type.")
        if payload.get("iss") != SETTINGS.JWT_ISSUER: 
            raise InvalidToken("Invalid issuer.")
        if not payload.get("sub"): 
            raise InvalidToken("sub is missing.")
        return payload
    except (ExpiredSignatureError, InvalidTokenError) as e:
        raise InvalidToken(str(e))

def verify_refresh(token: str) -> dict:
    """
    Verifies and decodes a refresh token.

    Args:
        token: The JWT refresh token.

    Returns:
        dict: The decoded token claims.

    Raises:
        InvalidToken: If the token is invalid or expired.
    """
    try:
        payload = _verify(token)
        if payload.get("type") != "refresh": 
            raise InvalidToken("Incorrect token type.")
        if payload.get("iss") != SETTINGS.JWT_ISSUER: 
            raise InvalidToken("Invalid issuer.")
        if not payload.get("sub"): 
            raise InvalidToken("sub is missing.")
        return payload
    except (ExpiredSignatureError, InvalidTokenError) as e:
        raise InvalidToken(str(e))
