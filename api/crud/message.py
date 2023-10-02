import json
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from api.tg_api.tg_utils import get_tg_latest_messages
from models import models


async def crud_post_messages(channel_username: str, message_data: dict, db: AsyncSession):
    message = models.LatestMessages(
        id=message_data['id'],
        channel_username=channel_username,
        date=datetime.strptime(message_data['date'], "%Y-%m-%d %H:%M:%S"),
        forwards=message_data['forwards'],
        url=message_data['url'],
        reactions=json.dumps(message_data['reactions']),
        text=message_data['message text']
    )

    db.add(message)

    try:
        await db.commit()
        await db.refresh(message)
        return f'Message {message.id} added successfully'
    except IntegrityError:
        await db.rollback()
        return None


async def crud_get_messages(channel_username: str, limit: int, db: AsyncSession):
    query = (
        select(models.LatestMessages)
        .filter(models.LatestMessages.channel_username == channel_username)
        .order_by(models.LatestMessages.date.desc())
        .limit(limit)
    )
    messages = await db.execute(query)
    messages_info = messages.scalars().all()

    return messages_info


async def crud_get_message_by_id(message_id: int, db: AsyncSession):
    query = (
        select(models.LatestMessages)
        .filter(models.LatestMessages.id == message_id)
    )
    response = await db.scalars(query)
    response = response.first()
    return response


async def crud_update_messages(channel_username: str, db: AsyncSession):
    new_messages = await get_tg_latest_messages(channel_username)

    query = (
        select(models.LatestMessages)
        .filter(models.LatestMessages.channel_username == channel_username)
    )
    existing_messages = await db.execute(query)

    for existing_message in existing_messages.scalars().all():
        for new_message_data in new_messages:
            if existing_message.id == new_message_data['id']:
                existing_message.date = datetime.strptime(new_message_data['date'], "%Y-%m-%d %H:%M:%S")
                existing_message.forwards = new_message_data['forwards']
                existing_message.url = new_message_data['url']
                existing_message.reactions = json.dumps(new_message_data['reactions'])
                existing_message.text = new_message_data['message text']

    await db.commit()


async def crud_delete_message_by_id(message_id: int, db: AsyncSession):
    query = (
        select(models.LatestMessages)
        .filter(models.LatestMessages.id == message_id)
    )
    message = await db.execute(query)
    message_record = message.scalar_one_or_none()

    if not message_record:
        return None

    await db.delete(message_record)
    await db.commit()
    return {"message": "Message deleted successfully"}


async def crud_delete_messages_by_channel(channel_username: str, db: AsyncSession):
    query = (
        select(models.LatestMessages)
        .filter(models.LatestMessages.channel_username == channel_username)
    )
    messages = await db.execute(query)
    messages = messages.scalars().all()

    if not messages:
        return None

    for message in messages:
        await db.delete(message)

    await db.commit()

    return {"message": "All messages for channel deleted successfully"}
