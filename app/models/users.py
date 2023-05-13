#system import 
#lib import
from pydantic import BaseModel
#local import


class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    phone: str
    password: str
    idStatus: int
    idCompany: int
   
    
    