from typing import Optional
from app.core.base_schema import BaseSchema

class Token(BaseSchema):
    access_token: str
    token_type: str

class TokenPayload(BaseSchema):
    sub: Optional[int] = None

class Msg(BaseSchema):
    msg: str
