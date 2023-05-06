# python


# pydantic


# fastapi
from fastapi import FastAPI

# Models

from models import UseLogin
from models import User
from models import BaseUser



app = FastAPI()



@app.get('/')
def home():
    return {
        'TwitterAPI': 'Working'
    }
    