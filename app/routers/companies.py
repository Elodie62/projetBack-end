#system import (import de base de python)
from typing import List, Annotated
#lib import
from fastapi import APIRouter, Depends, status, Response, HTTPException
#local import 
from models.users import User
from models.companies import Company
import internals.database
from internals.auth import decode_token


router=APIRouter()
async def getAllCompany() -> List[Company]:
    database = internals.database.connect()
    request= database.cursor( dictionary=True )    
    request.execute("SELECT * FROM company")
    companies = request.fetchall()
    request.close()
    database.close()
    return companies


@router.get("/allCompanies", responses={status.HTTP_204_NO_CONTENT:{}})
async def getAllCompanies(currentUser: Annotated[User, Depends(decode_token)])-> List[Company]:
     if (currentUser.nameStatus == "admin" and currentUser.nameStatus == "user"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        
     if currentUser.nameStatus == "maintainer":
        return await getAllCompany()


@router.post("/createCompany", status_code=status.HTTP_201_CREATED)
async def createCompany(currentUser: Annotated[User, Depends(decode_token)],companyToCreate:Company):
     if (currentUser.nameStatus == "admin" and currentUser.nameStatus == "user"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        
     if currentUser.nameStatus == "maintainer":
        database = internals.database.connect()
        request= database.cursor( dictionary=True )
        sql_query=("INSERT INTO users (nameCompany) VALUES (%s)")
        company_data = (companyToCreate)
        request.execute(sql_query, company_data)
        database.commit()
        request.close()
        database.close()
             
@router.put("/company/{id}", status_code=status.HTTP_201_CREATED)
async def updatePlanning(currentUser: Annotated[User, Depends(decode_token)], id: int , companyToUpdate: Company):
    if (currentUser.nameStatus == "admin" and currentUser.nameStatus == "user"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        
    if currentUser.nameStatus == "maintainer":
        database = internals.database.connect()
        request= database.cursor( dictionary=True )
        sql_query=("UPDATE planning SET nameCompany=%s WHERE id=%s")
        planning_data = (companyToUpdate, id)
        request.execute(sql_query, planning_data)
        database.commit()
        request.close()
        database.close()
        
    
    
    
@router.delete("/company/{id}", responses={status.HTTP_204_NO_CONTENT:{}})
async def deleteCompany(currentUser: Annotated[User, Depends(decode_token)], id: int ):
    if (currentUser.nameStatus == "admin" and currentUser.nameStatus == "user"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        
    if currentUser.nameStatus == "maintainer":
        database = internals.database.connect()
        request= database.cursor( dictionary=True )
        sql_query = "DELETE FROM company WHERE id=%s"
        user_data = [id]
        request.execute(sql_query, user_data)
        database.commit()
        request.close()
        database.close()