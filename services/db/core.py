from typing import Annotated, AsyncGenerator, Dict

from sqlalchemy import String
from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession,
                                    async_sessionmaker, create_async_engine)
from sqlalchemy.orm import DeclarativeBase

from services.db.config import db_settings

str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    """
    Базовый класс для описания моделей SQLAlchemy.

    Содержит маппинг типов данных на колонки таблицы.
    """
    type_annotation_map: Dict[str, str] = {
        str_256: String(256)
    }


# Создание асинхронного движка SQLAlchemy для работы с базой данных
engine: AsyncEngine = create_async_engine(
    url=db_settings.db_url_asyncpg,
    echo=True,
)

# Создание асинхронной фабрики сессий для работы с базой данных
async_session_maker: async_sessionmaker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Функция для получения асинхронной сессии базы данных.

    Returns:
        AsyncGenerator[AsyncSession, None]: Генератор асинхронных сессий.
    """
    async with async_session_maker() as session:
        yield session
