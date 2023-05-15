#system import (import de base de python)
from typing import List
#lib import
from fastapi import APIRouter, status, Response, HTTPException
from passlib.context import CryptContext
#local import 
from models.users import User
import internals.database


router=APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def getAllUserInDB() -> List[User]:
    database = internals.database.connect()
    request= database.cursor( dictionary=True )    
    request.execute("SELECT * FROM users")
    users = request.fetchall()
    request.close()
    database.close()
    return users

def get_password_hash(password):
    return pwd_context.hash(password)

@router.get("/users", responses={status.HTTP_204_NO_CONTENT:{}})
async def getAllUser()-> List[User]:
    users= await getAllUserInDB()

    if users== None:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return users


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def createUser(userToCreate:User):
    database = internals.database.connect()
    request= database.cursor( dictionary=True )    
    users= await getAllUserInDB()
    hashedPassword=get_password_hash(userToCreate.password)
 
    for user in users:
       if user["email"]== userToCreate.email:
           raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    
    sql_query=("INSERT INTO users (firstname, lastname, email, phone, password, idStatus, idCompany) VALUES (%s, %s, %s, %s, %s, %s, %s)")
    user_data = (userToCreate.firstname,userToCreate.lastname, userToCreate.email, userToCreate.phone, hashedPassword, userToCreate.idStatus, userToCreate.idCompany)
    request.execute(sql_query, user_data)
    database.commit()
    request.close()
    database.close()
    
    
@router.put("/users/{email}", status_code=status.HTTP_201_CREATED)
async def updateUser(email: str, userToUpdate: User):
   users= await getAllUserInDB()
   database = internals.database.connect()
   request= database.cursor( dictionary=True )   
   for user in users:
       if user['email']==email:
           sql_query = "UPDATE users SET firstname=%s, lastname=%s, email=%s, phone=%s, password=%s, idStatus=%s,idCompany=%s WHERE email=%s"
           user_data = (userToUpdate.firstname,userToUpdate.lastname, userToUpdate.email, userToUpdate.phone, userToUpdate.password, userToUpdate.idStatus, userToUpdate.idCompany, email)
           request.execute(sql_query, user_data)
           database.commit()
           request.close()
           database.close()
           
    
@router.delete("/users/{email}", responses={status.HTTP_204_NO_CONTENT:{}})
async def delete_user(userEmail: str) :
    users= await getAllUserInDB()
    database = internals.database.connect()
    request= database.cursor( dictionary=True )   
    for user in users:
        if user['email']==userEmail:
            sql_query = "DELETE FROM users WHERE email=%s"
            user_data = [userEmail]
            request.execute(sql_query, user_data)
            database.commit()
            request.close()
            database.close()