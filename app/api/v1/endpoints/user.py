from fastapi import APIRouter
from app.api.v1.schemas.user import UserCreate

route = APIRouter(prefix="/users")


@route.post("/user")
async def create_user(user: UserCreate):
    pass
