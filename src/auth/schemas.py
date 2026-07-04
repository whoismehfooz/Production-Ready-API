from pydantic import BaseModel, ConfigDict
from typing import List


class TokenSchema(BaseModel):
    access_token: str
    token_type: str

    model_config = ConfigDict(from_attributes=True)


class LoginSchema(BaseModel):
    username: str
    password: str

    model_config = ConfigDict(from_attributes=True)



