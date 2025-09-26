import os
import re
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=False)

@dataclass(frozen=True)
class Settings:
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "15"))
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS", "7"))
    JWT_ISSUER: str = os.getenv("JWT_ISSUER", "ITValley")
    EV_TOKEN_SOURCE: str = os.getenv("EV_TOKEN_SOURCE", "auto")   # auto|bearer|cookie
    EV_COOKIE_ACCESS: str = os.getenv("EV_COOKIE_ACCESS", "access_token")
    EV_COOKIE_REFRESH: str = os.getenv("EV_COOKIE_REFRESH", "refresh_token")
    EV_SUB_POLICY: str = os.getenv("EV_SUB_POLICY", "any")        # email|uuid|any

SETTINGS = Settings()

if len(SETTINGS.JWT_SECRET_KEY) < 32:
    raise ValueError("JWT_SECRET_KEY deve ter pelo menos 32 caracteres.")
if SETTINGS.EV_TOKEN_SOURCE not in {"auto","bearer","cookie"}:
    raise ValueError("EV_TOKEN_SOURCE deve ser auto|bearer|cookie.")
if SETTINGS.EV_SUB_POLICY not in {"email","uuid","any"}:
    raise ValueError("EV_SUB_POLICY deve ser email|uuid|any.")
