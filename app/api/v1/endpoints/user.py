from fastapi import APIRouter
from fastapi.responses import JSONResponse


route = APIRouter(prefix="/user")


@route.get("/user")
async def create_user():
    return JSONResponse(content={"name": "Lei Wen Peng"})
