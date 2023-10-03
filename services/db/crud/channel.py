from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.channel import ChannelInfoPydantic, ChannelInfo
from services.db import models
from typing import List, Union, Dict, Any


async def crud_post_channel(
        channel_info: ChannelInfoPydantic,
        messages_info: List[Dict[Any, Any]],
        db: AsyncSession) -> ChannelInfo:

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
    query = (
        select(models.ChannelInfo)
        .where(models.ChannelInfo.username == channel_username)
    )
    response = await db.scalars(query)
    return response.first()
