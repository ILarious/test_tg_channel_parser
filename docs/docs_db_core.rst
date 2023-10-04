.. highlight:: python

=========================
Документация services/db/core.py
=========================

Этот документ содержит обзор и документацию к `модулю`_, который предоставляет базовые функции для работы с базой данных SQLAlchemy.

.. _`Модулю`: https://github.com/ILarious/test_tg_channel_parser/blob/main/services/db/core.py

Класс Base
----------

.. code-block:: python

    class Base(DeclarativeBase):
        """
        Базовый класс для описания моделей SQLAlchemy.

        Содержит маппинг типов данных на колонки таблицы.
        """
        type_annotation_map: Dict[str, str] = {
            str_256: String(256)
        }

Класс `Base` представляет базовый класс для описания моделей SQLAlchemy. Он содержит маппинг типов данных на колонки таблицы.

Создание асинхронного двига SQLAlchemy
----------------------------------------

.. code-block:: python

    engine: AsyncEngine = create_async_engine(
        url=db_settings.db_url_asyncpg,
        echo=True,
    )

Асинхронный двигатель SQLAlchemy создается с использованием функции `create_async_engine`. Он использует URL-ссылку из настроек базы данных `db_settings.db_url_asyncpg` и включает режим эха для вывода SQL-запросов.

Создание асинхронной фабрики сессий SQLAlchemy
------------------------------------------------

.. code-block:: python

    async_session_maker: async_sessionmaker = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

Асинхронная фабрика сессий SQLAlchemy создается с использованием функции `async_sessionmaker`. Она использует асинхронный двигатель `engine`, класс `AsyncSession` и отключает автоматическое истечение срока действия сессии после коммита.

Функция get_async_session
------------------------

.. code-block:: python

    async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
        """
        Функция для получения асинхронной сессии базы данных.

        Returns:
            AsyncGenerator[AsyncSession, None]: Генератор асинхронных сессий.
        """

Функция `get_async_session` предоставляет асинхронную сессию базы данных при вызове. Она использует асинхронную фабрику сессий `async_session_maker` и возвращает генератор асинхронных сессий.
