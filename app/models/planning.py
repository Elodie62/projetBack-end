#system import 
#lib import
from pydantic import BaseModel
#local import


class Planning(BaseModel):
    id: int
    name:str
    idCompany: int
   