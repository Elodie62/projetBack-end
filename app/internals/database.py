#system import 
#lib import
from fastapi import FastAPI, APIRouter, status, Response, HTTPException
import mysql.connector
#local import 

app = FastAPI()


def connect():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="plannings",
            port="8889"
        )
        print("Connected to the database")
        return mydb
    except mysql.connector.Error as error:
        print("Failed to connect to the database: {}".format(error))


