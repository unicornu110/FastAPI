import pydantic as _pydantic
from typing import List

class _AddressBase(_pydantic.BaseModel):
    country : str
    address : str
    state: str
    city: str
    pincode: int

class Addess_create(_AddressBase):
    pass

class Address(_AddressBase):
    id : int
    owner_id : int

    class Config:
        orm_mode = True

class _UserBase(_pydantic.BaseModel):
    email : str

class User_create(_UserBase):
    password : str

class User(_UserBase):
    id : int
    is_active :  bool
    add : List[Address] = []
    class Config:
        orm_mode = True

