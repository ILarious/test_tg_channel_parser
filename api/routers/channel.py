from typing import List, Dict, Any

from asyncpg.exceptions import UniqueViolationError
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from telethon.errors import UsernameNotOccupiedError

from api.schemas.message import LatestMessagePydantic
from services.db.crud.channel import crud_post_channel, crud_get_channel
from services.db.core import get_async_session
from api.schemas.channel import ChannelInfo, ChannelInfoPydantic
from services.tg.utils import get_tg_channel_info, get_tg_latest_messages

router: APIRouter = APIRouter(
    prefix="/channels",
    tags=["channels"],
)


# Определение API-маршрута для отправки информации о канале в Telegram.
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
        # Получение информации о канале из Telegram и последних сообщений.
        channel_info: ChannelInfoPydantic = await get_tg_channel_info(channel_username)
        latest_messages: List[LatestMessagePydantic] = await get_tg_latest_messages(channel_username,
                                                                                    limit_latest_messages)
        messages_info: List[Dict[Any, Any]] = [message.dict() for message in latest_messages]

        # Отправка информации о канале в базу данных.
        response: ChannelInfo = await crud_post_channel(channel_info, messages_info, db)

        return response

    except (UniqueViolationError, IntegrityError):
        raise HTTPException(
            status_code=409,
            detail='Канал уже существует'
        )

    except (UsernameNotOccupiedError, ValueError):
        raise HTTPException(
            status_code=404,
            detail='Channel with the provided username was not found or it may be private.'
        )


# Определение API-маршрута для получения информации о канале в Telegram.
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
