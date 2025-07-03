from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import get_config

config = get_config()
Base = declarative_base()


async_engine = create_async_engine(
    f"mysql+aiomysql://{config.mysql_db_user}:{config.mysql_db_pwd}@{config.mysql_db_host}:{config.mysql_db_port}/mydatabase"
)

async_session = async_sessionmaker(
    engine=async_engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session():
    async with async_session() as session:
        yield session
