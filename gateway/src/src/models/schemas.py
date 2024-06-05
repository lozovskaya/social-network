import datetime
from typing import Union
from pydantic import BaseModel, Field


class UserRegister(BaseModel):
    login : str
    password : str
    
    
class UserModel(BaseModel):
    name : str = Field(default=None)
    surname : str = Field(default=None)
    birthday : datetime.datetime = Field(default=None)
    email : str = Field(default=None)
    phone_number : str = Field(default=None)
    
    
class CredentialsModel(BaseModel):
    login : str
    password_hash : str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None