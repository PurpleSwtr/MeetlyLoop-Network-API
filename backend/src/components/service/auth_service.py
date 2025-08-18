from authx import AuthX, AuthXConfig
from src.core.config import settings
from fastapi import Response
config = AuthXConfig()
config.JWT_SECRET_KEY = settings.JWT_KEY
config.JWT_ACCESS_COOKIE_NAME = settings.JWT_ACCESS_COOKIE
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)
def create_token(user_id:int, response: Response,remember_me:bool)-> dict:
    max_age = 604800 if remember_me else None
        
    token = security.create_access_token(uid=str(user_id))
    response.set_cookie(    
        key=config.JWT_ACCESS_COOKIE_NAME,
        value=token,
        max_age=max_age,
        httponly=True)   
    return {
        "token":token}