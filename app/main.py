#system import 
#lib import
from fastapi import FastAPI, status
#local import
import internals.database
from routers import users
app = FastAPI()


app.include_router(users.router, tags=["users"])


