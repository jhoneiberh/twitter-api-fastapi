# python
from typing import Optional
from uuid import UUID
from datetime import date
from datetime import datetime

# pydantic
from pydantic import Field
from pydantic import BaseModel
from pydantic import EmailStr


class BaseUser(BaseModel):
    user_id: UUID = Field()
    email: EmailStr = Field(example='example@gmail.com')

class User(BaseUser):
    first_name: str = Field(min_length=1, max_length=50, example='Juan')
    last_name: str = Field(min_length=1, max_length=50, example='Gonzalez')
    birth_date: Optional[date] = Field(default=None)

class PaswordUser(BaseModel):
    password: str = Field(min_length=8, max_length=64)

class UserLogin(PaswordUser, BaseUser):
    ...

class UserRegister(PaswordUser, User):
    ...

class Tweet(BaseModel):
    tweet_id: UUID = Field()
    content: str = Field(min_length=1, max_length=256)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field()