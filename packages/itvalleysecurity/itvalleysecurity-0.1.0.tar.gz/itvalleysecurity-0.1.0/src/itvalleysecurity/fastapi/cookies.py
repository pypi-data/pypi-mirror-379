from fastapi import Response
from ..config import SETTINGS

def set_auth_cookies(resp: Response, access: str, refresh: str, *, access_max_age: int, refresh_max_age: int):
    """
    Sets authentication cookies in the HTTP response.

    Args:
        resp: The FastAPI Response object.
        access: The access token.
        refresh: The refresh token.
        access_max_age: The max-age for the access token cookie in seconds.
        refresh_max_age: The max-age for the refresh token cookie in seconds.
    """
    resp.set_cookie(
        SETTINGS.EV_COOKIE_ACCESS, 
        access, 
        httponly=True, 
        secure=True, 
        samesite="strict", 
        max_age=access_max_age
    )
    resp.set_cookie(
        SETTINGS.EV_COOKIE_REFRESH, 
        refresh, 
        httponly=True, 
        secure=True, 
        samesite="strict", 
        path="/refresh", 
        max_age=refresh_max_age
    )
