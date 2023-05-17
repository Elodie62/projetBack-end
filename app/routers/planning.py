#system import (import de base de python)
from typing import List, Annotated
#lib import
from fastapi import APIRouter, Depends, status, Response, HTTPException
#local import 
from models.users import User
from models.planning import Planning
import internals.database
from internals.auth import decode_token


router=APIRouter()
async def getAllPlanningDb() -> List[Planning]:
    database = internals.database.connect()
    request= database.cursor( dictionary=True )    
    request.execute("SELECT * FROM planning ")
    planning = request.fetchall()
    request.close()
    database.close()
    return planning

@router.get("/allPlannings", responses={status.HTTP_204_NO_CONTENT:{}})
async def getAllPlannings(currentUser: Annotated[User, Depends(decode_token)])-> List[Planning]:
     if currentUser.nameStatus == "user":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
     if currentUser.nameStatus == "admin":
          return list(
            filter(lambda planning: planning["idCompany"] == currentUser.idCompany,  await getAllPlanningDb()))
        
     if currentUser.nameStatus == "maintainer":
        return await getAllPlanningDb()


@router.post("/createPlanning", status_code=status.HTTP_201_CREATED)
async def createPlanning(currentUser: Annotated[User, Depends(decode_token)],planningToCreate:Planning):
     if (currentUser.nameStatus == "admin" and currentUser.nameStatus == "user"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        
     if currentUser.nameStatus == "maintainer":
        database = internals.database.connect()
        request= database.cursor( dictionary=True )
        sql_query=("INSERT INTO users (name, idCompany) VALUES (%s, %s)")
        planning_data = (planningToCreate.name, planningToCreate.idCompany)
        request.execute(sql_query, planning_data)
        database.commit()
        request.close()
        database.close()
             
@router.put("/planning/{id}", status_code=status.HTTP_201_CREATED)
async def updatePlanning(currentUser: Annotated[User, Depends(decode_token)], id: int , planningToUpdate: Planning):
    if (currentUser.nameStatus == "admin" and currentUser.nameStatus == "user"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        
    if currentUser.nameStatus == "maintainer":
        database = internals.database.connect()
        request= database.cursor( dictionary=True )
        sql_query=("UPDATE planning SET name=%s,idCompany=%s WHERE id=%s")
        planning_data = (planningToUpdate.name, planningToUpdate.idCompany, id)
        request.execute(sql_query, planning_data)
        database.commit()
        request.close()
        database.close()
        
    
    
    
@router.delete("/planning/{id}", responses={status.HTTP_204_NO_CONTENT:{}})
async def deletePlanning(currentUser: Annotated[User, Depends(decode_token)], id: int ):
    if (currentUser.nameStatus == "admin" and currentUser.nameStatus == "user"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
        
    if currentUser.nameStatus == "maintainer":
        database = internals.database.connect()
        request= database.cursor( dictionary=True )
        sql_query = "DELETE FROM planning WHERE id=%s"
        user_data = [id]
        request.execute(sql_query, user_data)
        database.commit()
        request.close()
        database.close()