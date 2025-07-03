from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=512, description="")


class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=512, description="Create user")
