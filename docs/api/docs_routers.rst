.. highlight:: python

=====================
Документация api/routers/channel.py
=====================

Этот документ содержит обзор и документацию к API, созданному с использованием FastAPI.

`Модуль`_ содержит две функции для обработки API-запросов: post_channel, которая отправляет информацию о Telegram-канале в базу данных, и get_channel_info, которая получает информацию о канале из базы данных.

.. _`Модуль`: https://github.com/ILarious/test_tg_channel_parser/blob/main/api/routers/channel.py

Функция post_channel
------------

.. code-block:: python

    @router.post("/post/{channel_username}/", response_model=ChannelInfo)
    async def post_channel(
            channel_username: str,
            limit_latest_messages: int = 10,
            db: AsyncSession = Depends(get_async_session)
    ) -> ChannelInfo:
        """
        Отправляет информацию о канале в Telegram в базу данных.
        
        Args:
            channel_username (str): Имя пользователя Telegram-канала.
            limit_latest_messages (int, optional): Количество последних сообщений для получения. По умолчанию 10.
            db (AsyncSession, optional): Асинхронная сессия базы данных. По умолчанию Depends(get_async_session).
        
        Returns:
            ChannelInfo: Информация о созданном канале.
        
        Raises:
            HTTPException: Вызывается в случае ошибок. 404, если канал не найден, или 409, если канал уже существует.
        """
        try:
            channel_info: ChannelInfoPydantic = await get_tg_channel_info(channel_username)
            latest_messages: List[LatestMessagePydantic] = await get_tg_latest_messages(channel_username, limit_latest_messages)
            messages_info: List[Dict[Any, Any]] = [message.dict() for message in latest_messages]
            response: ChannelInfo = await crud_post_channel(channel_info, messages_info, db)

            return response

        except (UniqueViolationError, IntegrityError):
            raise HTTPException(
                status_code=409,
                detail='Channel already exists'
            )

        except (UsernameNotOccupiedError, ValueError):
            raise HTTPException(
                status_code=404,
                detail='The channel with the provided username was not found or it may be private.'
            )


Функция get_channel_info
------------

.. code-block:: python

    @router.get("/get/{channel_username}/", response_model=ChannelInfo)
    async def get_channel_info(
            channel_username: str,
            db: AsyncSession = Depends(get_async_session)
    ) -> ChannelInfo:
        """
        Получает информацию о канале Telegram из базы данных.
        
        Args:
        channel_username (str): Имя пользователя Telegram-канала.
        db (AsyncSession, optional): Асинхронная сессия базы данных. По умолчанию Depends(get_async_session).
        
        Returns:
        ChannelInfo: Информация о запрошенном канале.
        
        Raises:
        HTTPException: Вызывается, если канал не найден (status_code=404).
        """
        response: ChannelInfo = await crud_get_channel(channel_username, db)

        if not response:
            raise HTTPException(
                status_code=404,
                detail='Channel not found'
            )

        return response

- В данном примере представлены два эндпоинта, `post_channel` и `get_channel_info`.
- `post_channel` позволяет создавать новые каналы и получать информацию о последних сообщениях в канале.
- `get_channel_info` позволяет получать информацию о существующих каналах.
- Обработчики ошибок `HTTPException` предоставляют информацию о статусе запроса и причине ошибки.

Обратите внимание, что для работы этого кода необходимы внешние зависимости, такие как база данных и библиотека Telethon. Убедитесь, что все необходимые зависимости установлены и сконфигурированы корректно.
