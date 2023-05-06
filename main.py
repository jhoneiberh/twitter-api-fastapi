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
from models import UserRegister
from models import Tweet



app = FastAPI()

# Path Operations


## Users

### Register a user
@app.post('/signup', response_model=User, status_code=status.HTTP_201_CREATED, summary='Register a User', tags=['Users'])
def signup():
    """
    Signup a user

    This path operations register a user in the app

    Parameters:
        - Request body parameter:
            - user: UserRegister

    Returns: A json with the basic user information: \n
        - user_id: UUID.
        - email: EmailStr.
        - first_name: str.  
        - last_name: str.
        - birth_date: date.
        - password: str
    """
    

### Login a user
@app.post('/login', response_model=UserLogin, status_code=status.HTTP_200_OK, summary='Login a User', tags=['Users'])
def login():
    return

### Show all users
@app.get('/users', response_model=List[User], status_code=status.HTTP_200_OK, summary='Show all users', tags=['Users'])
def show_all_users():
    return

### Show a user
@app.get('/users/{user_id}', response_model=User, status_code=status.HTTP_200_OK, summary='Show a User', tags=['Users'])
def show_a_user():
    return

### Delete a user
@app.delete('/users/{user_id}/delete', response_model=User, status_code=status.HTTP_200_OK, summary='Delete a User', tags=['Users'])
def delete_a_user():
    return

### Delete a user
@app.put('/users/{user_id}/update', response_model=User, status_code=status.HTTP_200_OK, summary='Update a User', tags=['Users'])
def update_a_user():
    return

    

## Tweets

### Show all tweets
@app.get('/', response_model=List[Tweet], status_code=status.HTTP_200_OK, summary='Show all tweets', tags=['Tweets'])
def home():
    return {
        'TwitterAPI': 'Working'
    }

### Post a tweet
@app.post('/post/', response_model=Tweet, status_code=status.HTTP_201_CREATED, summary='Post a Tweet', tags=['Tweets'])
def post():
    return

### Show a tweet
@app.get('/tweets/{tweet_id}', response_model=Tweet, status_code=status.HTTP_200_OK, summary='Show a Tweet', tags=['Tweets'])
def show_a_tweet():
    return

### Show a tweet
@app.delete('/tweets/{tweet_id}/delete', response_model=Tweet, status_code=status.HTTP_200_OK, summary='Delete a Tweet', tags=['Tweets'])
def delete_a_tweet():
    return

### Delete a tweet
@app.put('/tweets/{tweet_id}/update', response_model=Tweet, status_code=status.HTTP_200_OK, summary='Update a Tweet', tags=['Tweets'])
def update_a_tweet():
    return