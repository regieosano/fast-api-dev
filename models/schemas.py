from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class UserBase(BaseModel):
    email: EmailStr
    password: str


class VoteBase(BaseModel):
    post_id: int
    dir: conint(le=1)


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class UserCreate(UserBase):
    pass


class UserLogin(UserBase):
    pass


class VoteCreate(VoteBase):
    pass


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class PostUpdateResponse(PostBase):
    pass        


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        from_attributes = True

class PostVotesResponse(BaseModel):
    Post: PostResponse
    votes: int


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
