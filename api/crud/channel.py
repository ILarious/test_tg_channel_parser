from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from models import models
from api.tg_api.tg_utils import get_tg_channel_info


async def crud_post_channel(channel_username: str, db: AsyncSession):
    channel_info = await get_tg_channel_info(channel_username)
    db_channel_info = models.ChannelInfo(**channel_info)
    db.add(db_channel_info)
    await db.commit()
    await db.refresh(db_channel_info)
    query = (
        select(models.ChannelInfo)
        .where(models.ChannelInfo.id == db_channel_info.id)
    )
    response = await db.scalars(query)
    return response.first()


async def crud_get_channel(channel_username, db: AsyncSession):
    query = (
        select(models.ChannelInfo)
        .where(models.ChannelInfo.username == channel_username)
    )
    response = await db.scalars(query)
    return response.first()


async def crud_update_channel(db: AsyncSession, channel_username: str):
    query = (
        select(models.ChannelInfo)
        .where(models.ChannelInfo.username == channel_username)
    )
    db_channel_info = await db.scalars(query)
    db_channel_info = db_channel_info.first()

    channel_info = await get_tg_channel_info(channel_username)

    if db_channel_info:
        for attr, value in channel_info.items():
            setattr(db_channel_info, attr, value)
        await db.commit()
        await db.refresh(db_channel_info)
    return db_channel_info


async def crud_delete_channel(db: AsyncSession, channel_username: str):
    query = (
        select(models.ChannelInfo)
        .where(models.ChannelInfo.username == channel_username)
    )
    db_channel_info = await db.scalars(query)
    db_channel_info = db_channel_info.first()
    if db_channel_info:
        await db.delete(db_channel_info)
        await db.commit()
    return db_channel_info