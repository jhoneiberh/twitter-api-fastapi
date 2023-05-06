# python
from typing import List

# pydantic


# fastapi
from fastapi import FastAPI
from fastapi import status

# Models

from models import UserLogin
from models import User
from models import BaseUser



app = FastAPI()

# Path Operations

@app.get('/', tags=['Home'])
def home():
    return {
        'TwitterAPI': 'Working'
    }

## Users

@app.post('/signup', response_model=User, status_code=status.HTTP_201_CREATED, summary='Register a User', tags=['Users'])
def signup():
    return

@app.post('/login', response_model=UserLogin, status_code=status.HTTP_200_OK, summary='Login a User', tags=['Users'])
def login():
    return

@app.get('/users', response_model=List[User], status_code=status.HTTP_200_OK, summary='Show all users', tags=['Users'])
def show_all_users():
    return

@app.get('/users/{user_id}', response_model=User, status_code=status.HTTP_200_OK, summary='Show a User', tags=['Users'])
def show_a_user():
    return

@app.delete('/users/{user_id}/delete', response_model=User, status_code=status.HTTP_200_OK, summary='Delete a User', tags=['Users'])
def delete_a_user():
    return

@app.put('/users/{user_id}/update', response_model=User, status_code=status.HTTP_200_OK, summary='Update a User', tags=['Users'])
def update_a_user():
    return

    

## Tweets