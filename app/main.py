#system import 
#lib import

from fastapi import FastAPI, status
#local import
from internals import auth
from routers import users
from routers import activities
from routers import companies
from routers import planning
app = FastAPI()


app.include_router(users.router, tags=["users"])
app.include_router(auth.router, tags=["auth"])
app.include_router(activities.router, tags=["activities"])
app.include_router(planning.router, tags=["planning"])
app.include_router(companies.router, tags=["companies"])