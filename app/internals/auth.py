#system import 
import hashlib
from typing import Annotated, List
#lib import
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
from passlib.context import CryptContext
#local import

from models.users import User, UserLogin
import internals.database



router=APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def getAllUserInDB() -> List[User]:
    database = internals.database.connect()
    request= database.cursor( dictionary=True )    
    request.execute("SELECT * FROM users INNER JOIN company ON users.idCompany=company.id INNER JOIN status ON users.idStatus= status.id")
    users = request.fetchall()
    request.close()
    database.close()
    return users


JWT_KEY = "jdqskjlsqkdsjrtkDDNKkelcnyluzaq"

async def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        decoded_data = jwt.decode(token, JWT_KEY, algorithms=['HS256'])
        return UserLogin(firstname= decoded_data.get("firstname"), lastname= decoded_data.get("lastname"), email= decoded_data.get("email"),nameCompany= decoded_data.get("company"), nameStatus= decoded_data.get("status"), )
    except JWTError:
        return credentials_exception


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    users= await getAllUserInDB()
    for user in users:
        
        if user["email"] == form_data.username and verify_password(form_data.password, user["password"]):
            data = dict()
            data["email"] = form_data.username
            data["firstname"]=user["firstname"]
            data["lastname"]= user["lastname"]
            data["company"]= user["nameCompany"]
            data["status"]=user["nameStatus"]
            jwt_token = jwt.encode(data, JWT_KEY, algorithm="HS256")
            return {"access_token": jwt_token, "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")
    
