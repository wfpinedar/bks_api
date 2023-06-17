from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from conn.db import conn 
from models.user import User
from utils.utils import user_is_valid
from utils.function_jwt import write_token, validate_token

route = APIRouter()


@route.post("/login")
def login(user: User):
    if user_is_valid(user.dict()):
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, 
                            status_code=404)

@route.post("/verify_token")
def verify_token(Authorization: str = Header(None)):
    if Authorization:
        token = Authorization.split(" ")[1]
        return validate_token(token, output=True)
    else:
        return JSONResponse(content={"message": "Forbidden"}, 
                            status_code=403)      
