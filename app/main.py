#system import 
#lib import

from fastapi import FastAPI, status
#local import
from internals import auth
from routers import users
from routers import activities
app = FastAPI()


app.include_router(users.router, tags=["users"])
app.include_router(auth.router, tags=["auth"])
app.include_router(activities.router, tags=["activities"])