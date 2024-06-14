import datetime
from typing import Union
from pydantic import BaseModel, Field


class UserRegister(BaseModel):
    login : str
    password : str
    
    
class UserModel(BaseModel):
    name : str = Field(default=None)
    surname : str = Field(default=None)
    birthday : datetime.date = Field(default=None)
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
    

class Post(BaseModel):
    title : str
    content : str


class FullInfoPost(BaseModel):
    post_id : int
    user_id : int
    title : str
    content : str
    created_at : datetime.datetime
    edited_at : datetime.datetime