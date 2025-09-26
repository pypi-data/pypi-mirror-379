import os
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from typing import Final
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER: Final[str] = os.getenv("POSTGRES_USER", "")
POSTGRES_PASSWORD: Final[str] = os.getenv("POSTGRES_PASSWORD", "")
POSTGRES_DB: Final[str] = os.getenv("POSTGRES_DB", "")
POSTGRES_HOST: Final[str] = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT: Final[int] = int(os.getenv("POSTGRES_PORT", "5432"))

DATABASE_URL: Final[str] = (
    f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)
