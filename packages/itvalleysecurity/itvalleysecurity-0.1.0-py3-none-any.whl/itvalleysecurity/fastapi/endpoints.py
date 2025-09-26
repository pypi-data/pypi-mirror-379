from fastapi import Response
from ..core import issue_pair
from ..config import SETTINGS

def login_response(resp: Response, *, sub: str, email: str | None = None, set_cookies: bool = True):
    """
    Generates a login response with JWT tokens and optionally sets cookies.

    Args:
        resp: The FastAPI Response object.
        sub: The user identifier.
        email: The user's email (optional).
        set_cookies: Whether to set HttpOnly cookies (default: True).

    Returns:
        dict: A dictionary with tokens and metadata.
    """
    pair = issue_pair(sub=sub, email=email)
    
    if set_cookies:
        access_secs  = SETTINGS.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60
        refresh_secs = SETTINGS.JWT_REFRESH_TOKEN_EXPIRE_DAYS * 86400
        
        resp.set_cookie(
            SETTINGS.EV_COOKIE_ACCESS, 
            pair["access_token"],
            httponly=True, 
            secure=True, 
            samesite="strict", 
            max_age=access_secs
        )
        resp.set_cookie(
            SETTINGS.EV_COOKIE_REFRESH, 
            pair["refresh_token"],
            httponly=True, 
            secure=True, 
            samesite="strict", 
            path="/refresh", 
            max_age=refresh_secs
        )
    
    return pair
