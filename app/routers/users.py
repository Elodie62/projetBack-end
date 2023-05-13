#system import (import de base de python)
#lib import
from fastapi import APIRouter, status, Response, HTTPException
#local import 

import internals.database

router=APIRouter()


@router.get("/users", responses={status.HTTP_204_NO_CONTENT:{}})
async def getAllUser():
    database = internals.database.connect()
    request= database.cursor( dictionary=True )    
    request.execute("SELECT * FROM users")
    users = request.fetchall()
    print (users)

    if len(users)==0:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    return users

