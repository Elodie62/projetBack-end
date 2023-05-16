#system import 
from datetime import date
#lib import
from pydantic import BaseModel
#local import

class Activities(BaseModel):
    startDate:date
    nameActivity: str
    duration:int 
    idPlanning:int 
    idCompany: int 
    nbInscription : int
    