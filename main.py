# python
from typing import List
from uuid import uuid4
from uuid import UUID
import json

# pydantic



# fastapi
from fastapi import FastAPI
from fastapi import status
from fastapi import Body
from fastapi import Path
from fastapi import HTTPException


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
def signup(user: UserRegister = Body()):
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
    with open('users.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())

        user_dict = user.dict()
        # user_dict['user_id'] = str(user_dict['user_id'])
        user_dict['user_id'] = str(uuid4())
        user_dict['birth_date'] = str(user_dict['birth_date'])
        
        results.append(user_dict) # añadir el usuario al json
        f.seek(0) # moverse al inicio del archivo
        f.write(json.dumps(results)) # escribir en el json, conviertiendo el dict en json

        return user

    

### Login a user
@app.post('/login', response_model=UserLogin, status_code=status.HTTP_200_OK, summary='Login a User', tags=['Users'])
def login():
    return

### Show all users
@app.get('/users', response_model=List[User], status_code=status.HTTP_200_OK, summary='Show all users', tags=['Users'])
def show_all_users():
    """
    Show all Users

    This path operations show all users in the app

    Parameters:
    - Nothing

    Returns: A json list with all users in the app, with the following keys: 
    - user_id: UUID.
    - email: EmailStr.
    - first_name: str.  
    - last_name: str.
    - birth_date: date.
    - password: str

    """

    with open('users.json', 'r', encoding='utf-8') as f:
        results = json.loads(f.read())

        return results

### Show a user
@app.get('/users/{user_id}', response_model=User, status_code=status.HTTP_200_OK, summary='Show a User', tags=['Users'])
def show_a_user(user_id: str = Path(example='635a3d76-3fa8-4a52-b2a7-1dad4c7f71fd')):
    
    with open('users.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())
        
    for index, item in enumerate(results):
        if item['user_id'] == user_id:  
            print('Hola')
            return item
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'This user doesn\'t exist {user_id}')

### Delete a user
@app.delete('/users/{user_id}/delete', response_model=UserRegister, status_code=status.HTTP_200_OK, summary='Delete a User', tags=['Users'])
def delete_a_user(user_id: str = Path(example='4ed4a8f9-7d60-40aa-b5ff-c8fd79025f8d')):
    
    with open('users.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())

        for index, item in enumerate(results):
            if item['user_id'] == user_id:
                results.remove(item)
                with open('users.json', 'w', encoding='utf-8') as f:
                    f.seek(0)
                    f.write(json.dumps(results))
                return item
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='This user doesn\'t exist')

### Update a user
@app.put('/users/{user_id}/update', response_model=User, status_code=status.HTTP_200_OK, summary='Update a User', tags=['Users'])
def update_a_user():
    return
    
    
    

## Tweets

### Show all tweets
@app.get('/', response_model=List[Tweet], status_code=status.HTTP_200_OK, summary='Show all tweets', tags=['Tweets'])
def home():
    """
    Show all Tweets

    This path operations show all tweets in the app

    Parameters:
    - Nothing

    Returns: A json list with all tweets in the app, with the following keys: 
    - tweet_id: UUID.
    - content: str.
    - created_at: datetime.  
    - updated_at: Optional[datetime].
    - by: User.

    """

    with open('tweets.json', 'r', encoding='utf-8') as f:
        results = json.loads(f.read())

        return results

### Post a tweet
@app.post('/post/', response_model=Tweet, status_code=status.HTTP_201_CREATED, summary='Post a Tweet', tags=['Tweets'])
def post(tweet: Tweet = Body()):
    """
    Post a Tweet

    This path operations post a tweet in the app

    Parameters:
        - Request body parameter:
            - tweet: Tweet

    Returns: A json with the basic user information: \n
        - tweet_id: UUID.
        - content: str.
        - created_at: datetime.  
        - updated_at: Optional[datetime].
        - by: User.
    """
    with open('tweets.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())

        tweet_dict = tweet.dict()
        # tweet_dict['tweet_id'] = str(tweet_dict['tweet_id'])
        tweet_dict['tweet_id'] = str(uuid4())
        # tweet_dict['by'] = str(tweet_dict['by'])
        tweet_dict['created_at'] = str(tweet_dict['created_at'])
        if tweet_dict['updated_at']:
            tweet_dict['updated_at'] = str(tweet_dict['updated_at'])

        
        tweet_dict['by']['user_id'] = str(tweet_dict['by']['user_id'])
        tweet_dict['by']['birth_date'] = str(tweet_dict['by']['birth_date'])
        
        results.append(tweet_dict) # añadir el tweet al json
        f.seek(0) # moverse al inicio del archivo
        f.write(json.dumps(results)) # escribir en el json, conviertiendo el dict en json

        return tweet

### Show a tweet
@app.get('/tweets/{tweet_id}', response_model=Tweet, status_code=status.HTTP_200_OK, summary='Show a Tweet', tags=['Tweets'])
def show_a_tweet(tweet_id: str = Path(example='3fa85f64-5717-4562-b3fc-2c963f66afa6')):
     
    with open('tweets.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())

        for item in results:
            if item['tweet_id'] == tweet_id:
                return item
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='This tweet doesn\'t exist')


       

### Show a tweet
@app.delete('/tweets/{tweet_id}/delete', response_model=Tweet, status_code=status.HTTP_200_OK, summary='Delete a Tweet', tags=['Tweets'])
def delete_a_tweet(tweet_id: str = Path(example='e4f79aa6-1a1c-4615-83ca-5f6a33324409')):
    with open('tweets.json', 'r+', encoding='utf-8') as f:
        results = json.loads(f.read())

        for index, item in enumerate(results):
            if item['tweet_id'] == tweet_id:
                results.remove(item)
                with open('tweets.json', 'w', encoding='utf-8') as f:
                    f.seek(0)
                    f.write(json.dumps(results))
                return item
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='This tweet doesn\'t exist')

### Delete a tweet
@app.put('/tweets/{tweet_id}/update', response_model=Tweet, status_code=status.HTTP_200_OK, summary='Update a Tweet', tags=['Tweets'])
def update_a_tweet():
    return