from typing import TypedDict, Dict, Any

class TokenPair(TypedDict):
    access_token: str
    refresh_token: str
    token_type: str
    access_expires_at: str
    refresh_expires_at: str

ClaimsDict = Dict[str, Any]
