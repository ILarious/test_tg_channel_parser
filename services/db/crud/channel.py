from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.channel import ChannelInfoPydantic, ChannelInfo
from services.db import models
from typing import List, Union, Dict, Any


async def crud_post_channel(
        channel_info: ChannelInfoPydantic,
        messages_info: List[Dict[Any, Any]],
        db: AsyncSession) -> ChannelInfo:
    """
    Создает новую запись о канале в базе данных.

    Args:
        channel_info (ChannelInfoPydantic): Информация о канале для сохранения.
        messages_info (List[Dict[Any, Any]]): Информация о последних сообщениях канала.
        db (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        ChannelInfo: Запись о созданном канале в базе данных.
    """
    channel_full = {
        'id': channel_info.id,
        'username': channel_info.username,
        'title': channel_info.title,
        'description': channel_info.description,
        'member_count': channel_info.member_count,
        'link': str(channel_info.link),
        'messages': messages_info
    }

    db_channel_info = models.ChannelInfo(**channel_full)
    db.add(db_channel_info)
    await db.commit()
    await db.refresh(db_channel_info)

    return db_channel_info


async def crud_get_channel(channel_username: str, db: AsyncSession) -> Union[models.ChannelInfo, None]:
    """
    Извлекает информацию о канале из базы данных по его имени пользователя (username).

    Args:
        channel_username (str): Имя пользователя (username) канала.
        db (AsyncSession): Асинхронная сессия базы данных.

    Returns:
        Union[models.ChannelInfo, None]: Информация о канале или None, если канал не найден.
    """
    query = (
        select(models.ChannelInfo)
        .where(models.ChannelInfo.username == channel_username)
    )
    response = await db.scalars(query)
    return response.first()
