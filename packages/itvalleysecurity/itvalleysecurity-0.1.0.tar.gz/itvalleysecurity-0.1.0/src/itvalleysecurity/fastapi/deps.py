from typing import Optional
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from ..config import SETTINGS
from ..core import verify_access

security = HTTPBearer(auto_error=False)

def _extract_token(request: Request, credentials: Optional[HTTPAuthorizationCredentials]) -> Optional[str]:
    """
    Extracts the access token from the Authorization header or a cookie, based on configuration.

    Args:
        request: The FastAPI Request object.
        credentials: The HTTPBearer credentials.

    Returns:
        str | None: The extracted token, or None if not found.
    """
    if SETTINGS.EV_TOKEN_SOURCE in {"auto","bearer"} and credentials and credentials.credentials:
        return credentials.credentials
    if SETTINGS.EV_TOKEN_SOURCE in {"auto","cookie"}:
        return request.cookies.get(SETTINGS.EV_COOKIE_ACCESS)
    return None

async def require_access(
    request: Request,
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
):
    """
    A FastAPI dependency that requires a valid access token.

    Args:
        request: The FastAPI Request object.
        credentials: The HTTPBearer credentials.

    Returns:
        dict: Information about the authenticated user.

    Raises:
        HTTPException: If the token is not provided, is invalid, or has expired.
    """
    token = _extract_token(request, credentials)
    if not token:
        raise HTTPException(
            status_code=401, 
            detail="Access token not provided",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    try:
        payload = verify_access(token)
        return {
            "sub": payload["sub"],
            "email": payload.get("email"),
            "claims": {k: v for k, v in payload.items()
                       if k not in {"sub","email","type","iss","jti","iat","nbf","exp"}},
        }
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401, 
            detail="Your token has expired. Please log in again.",
            headers={"WWW-Authenticate": "Bearer"}
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=401, 
            detail=f"Invalid token. Access denied. ({e})",
            headers={"WWW-Authenticate": "Bearer"}
        )
