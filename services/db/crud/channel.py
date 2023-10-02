from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from services.db import models


async def crud_post_channel(channel_info, messages_info, db: AsyncSession):
    channel_full = {
        'id': channel_info['id'],
        'username': channel_info['username'],
        'title': channel_info['title'],
        'description': channel_info['description'],
        'member_count': channel_info['member_count'],
        'link': channel_info['link'],
        'messages': messages_info
    }

    db_channel_info = models.ChannelInfo(**channel_full)
    db.add(db_channel_info)
    await db.commit()
    await db.refresh(db_channel_info)

    return 'Channel added successfully'


async def crud_get_channel(channel_username, db: AsyncSession):
    query = (
        select(models.ChannelInfo)
        .where(models.ChannelInfo.username == channel_username)
    )
    response = await db.scalars(query)
    return response.first()
