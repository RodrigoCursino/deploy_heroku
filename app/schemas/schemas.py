from pydantic import BaseModel
from typing   import Optional, List
from sqlalchemy.sql import roles

class User(BaseModel):

    id         : Optional[int] = None
    username   : str
    picture    : str
    stars      : int
    cellphone  : str
    password   : str

    class Config():
        orm_mode = True

class UserLogin(BaseModel):
    
    cellphone  : str
    password   : str