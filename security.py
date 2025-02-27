from pydantic import BaseModel
import time
from uuid import uuid4
import jwt


class AccessToken(BaseModel):
    iss: str
    sub: int
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str


class JWTToken(BaseModel):
    access_token: AccessToken


def sign_jwt(user_id: int) -> JWTToken:
    now = time.time()
    payload = {
        "iss": "curso-fastapi.com.br",
        "sub": user_id,
        "aud": "curso-fastapi",
        "exp": now * (60 * 30), # 30 min         
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)