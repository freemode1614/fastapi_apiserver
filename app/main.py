from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints.user import route as user_route
from app.core.config import get_config
from app.db.session import Base, async_engine
from app.utils.logger import get_scoped_logger

config = get_config()
log = get_scoped_logger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield
    # log.info("Database initialization start")
    # async with async_engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    # log.info("Database initialization end")
    # yield
    # await async_engine.dispose()
    # log.info("Database engine disposed")


app = FastAPI(title=config.app_name, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(router=user_route)


config = get_config()

if __name__ == "__main__":
    log.info("Server started")
    uvicorn.run(
        "main:app",
        #
        host="0.0.0.0",
        port=8000,
        workers=1,
        reload=True,
    )
