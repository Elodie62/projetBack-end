#system import 
#lib import
from pydantic import BaseModel
#local import


class User(BaseModel):
   
    firstname: str
    lastname: str
    email: str
    phone: str
    password: str
    idStatus: int
    idCompany: int
   
    
    