from pydantic import BaseModel,Field,validator,EmailStr
from typing import Optional
class UserCreate(BaseModel):
    name:str=Field(min_length=4,max_length=20)
    email:EmailStr

    @validator("name")
    def name_must_be_capital(cls,value):
        if " " in value:
            raise ValueError("Space not allowed")
        if not value.isalpha():
            raise ValueError("Name must contain only letters")
        return value.title()
        
        # return value.title()


class UserUpdate(BaseModel):
    name:str|None=Field(None,min_length=4,max_length=20)
    email:EmailStr|None=None
    @validator("name")
    def name_must_be_capital(cls,value):
        if value is None:          # 🔥 MOST IMPORTANT
            return value

        if " " in value:
            raise ValueError("Space not allowed")
        if not value.isalpha():
            raise ValueError("Name must contain only letters")
        return value.title()
