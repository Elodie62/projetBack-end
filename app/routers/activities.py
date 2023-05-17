#system import (import de base de python)
from typing import List, Annotated
#lib import
from fastapi import APIRouter, Depends, status, Response, HTTPException
#local import 
from models.activities import Activities
from models.users import User
import internals.database
from internals.auth import decode_token

router=APIRouter()

async def getAllActivitiesDB() -> List[Activities]:
    database = internals.database.connect()
    request= database.cursor( dictionary=True )    
    request.execute("SELECT * FROM activities INNER JOIN company ON activities.idCompany=company.id INNER JOIN planning ON activities.idPlanning= planning.id")
    activities = request.fetchall()
    request.close()
    database.close()
    return activities

async def getAllUserInDB() -> List[User]:
    database = internals.database.connect()
    request= database.cursor( dictionary=True )    
    request.execute("SELECT * FROM users INNER JOIN company ON users.idCompany=company.id INNER JOIN status ON users.idStatus= status.id")
    users = request.fetchall()
    request.close()
    database.close()
    return users



@router.get("/allActivitiesInCompany", responses={status.HTTP_204_NO_CONTENT:{}})
async def getAllActivities(currentUser: Annotated[User, Depends(decode_token)])-> List[Activities]:
    if currentUser.nameStatus == "maintainer":
        return await getAllActivitiesDB()
        
    else:
        activities = list(filter(lambda activity: activity["nameCompany"] == currentUser.nameCompany,  await getAllActivitiesDB()))
        if len(activities) == 0:
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else: 
            return activities
    

@router.post("/createActivity", status_code=status.HTTP_201_CREATED)
async def createActivity(currentUser: Annotated[User, Depends(decode_token)], createActivity: Activities):
   
    if currentUser.idCompany != createActivity.idCompany:
         raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden")

    database = internals.database.connect()
    request= database.cursor( dictionary=True )    
   
    sql_query=("INSERT INTO activities (nameActivity, startDate, duration, idPlanning, idCompany, nbInscription, owner) VALUES (%s, %s, %s, %s, %s, %s, %s)")
    activity_data = (createActivity.nameActivity,createActivity.startDate, createActivity.duration, createActivity.idPlanning, createActivity.idCompany, createActivity.nbInscription, createActivity.ownerEmail)
    request.execute(sql_query, activity_data)
    database.commit()
    request.close()
    database.close()
    
    

@router.put("/activity/{nameActivity}", status_code=status.HTTP_201_CREATED)
async def updateActivity(currentUser: Annotated[User, Depends(decode_token)], nameActivity: str, activityToUpdate: Activities):
    database = internals.database.connect()
    request= database.cursor( dictionary=True )  
    if currentUser.nameStatus == "user" :
        if currentUser.email != activityToUpdate.ownerEmail:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden")
            
        sql_query = "UPDATE activities SET nameActivity=%s, startDate=%s, duration=%s, idPlanning=%s, idCompany=%s, nbInscription=%s WHERE nameActivity=%s AND ownerEmail=%s"
        activity_data = (activityToUpdate.nameActivity,activityToUpdate.startDate, activityToUpdate.duration, activityToUpdate.idPlanning, activityToUpdate.idCompany, activityToUpdate.nbInscription,nameActivity,activityToUpdate.ownerEmail )
        request.execute(sql_query, activity_data)
        database.commit()
        request.close()
        database.close()
    
    elif currentUser.nameStatus == "admin":
        if currentUser.idCompany!=activityToUpdate.idCompany:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden")
        else : 
            sql_query = "UPDATE activities SET nameActivity=%s, startDate=%s, duration=%s, idPlanning=%s, idCompany=%s, nbInscription=%s WHERE nameActivity=%s AND ownerEmail=%s"
            activity_data = (activityToUpdate.nameActivity,activityToUpdate.startDate, activityToUpdate.duration, activityToUpdate.idPlanning, activityToUpdate.idCompany, activityToUpdate.nbInscription,nameActivity,activityToUpdate.ownerEmail )
            request.execute(sql_query, activity_data)
            database.commit()
            request.close()
            database.close()
    else: 
        sql_query = "UPDATE activities SET nameActivity=%s, startDate=%s, duration=%s, idPlanning=%s, idCompany=%s, nbInscription=%s WHERE nameActivity=%s "
        activity_data = (activityToUpdate.nameActivity,activityToUpdate.startDate, activityToUpdate.duration, activityToUpdate.idPlanning, activityToUpdate.idCompany, activityToUpdate.nbInscription,nameActivity )
        request.execute(sql_query, activity_data)
        database.commit()
        request.close()
        database.close()
        
            

@router.delete("/activity/{nameActivity}", responses={status.HTTP_204_NO_CONTENT:{}})
async def delete_activity(currentUser: Annotated[User, Depends(decode_token)],nameActivity: str) :
    database = internals.database.connect()
    request= database.cursor( dictionary=True )  
    sql_query = "SELECT * FROM activities WHERE nameActivity=%s"
    activity_data = [nameActivity]
    request.execute(sql_query, activity_data)
    activity = request.fetchall()
    
    
    if currentUser.nameStatus == "user" :
        if currentUser.email != activity.ownerEmail:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden")
        
        sql_query = "DELETE FROM activities WHERE nameActivity=%s AND ownerEmail=%s"
        activity_data = [nameActivity, currentUser.email]
        request.execute(sql_query, activity_data)
        database.commit()
        request.close()
        database.close()
        
    elif currentUser.nameStatus == "admin":
        if currentUser.idCompany!=activity.idCompany:
            raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden")
        else :
            sql_query = "DELETE FROM activities WHERE nameActivity=%s AND idCompany=%s"
            activity_data = [nameActivity, currentUser.idCompany]
            request.execute(sql_query, activity_data)
            database.commit()
            request.close()
            database.close()
    else : 
         sql_query = "DELETE FROM activities WHERE nameActivity=%s"
         activity_data = [nameActivity]
         request.execute(sql_query, activity_data)
         database.commit()
         request.close()
         database.close()
        