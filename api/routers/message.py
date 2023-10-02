from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.crud.message import crud_post_messages, crud_get_messages, crud_update_messages, crud_delete_message_by_id, \
    crud_delete_messages_by_channel, crud_get_message_by_id
from api.tg_api.tg_utils import get_tg_latest_messages
from core.db_core import get_async_session

router = APIRouter(
    prefix="/messages",
    tags=["messages"],
)


@router.post("/{channel_username}/")
async def post_messages_info(channel_username: str, limit: int = 10, db: AsyncSession = Depends(get_async_session)):
    try:
        messages_info = await get_tg_latest_messages(channel_username, limit)

        saved_messages = []
        for message_data in messages_info:
            message = await crud_post_messages(channel_username, message_data, db)
            if message:
                saved_messages.append(message)

        if not saved_messages:
            raise HTTPException(status_code=409, detail="Channel already exists")

        return saved_messages

    except ValueError:
        raise HTTPException(
            status_code=404,
            detail='Channel not found in Telegram'
        )


@router.get("/{channel_username}/")
async def get_messages_info(channel_username: str, limit: int = 10, db: AsyncSession = Depends(get_async_session)):
    messages_info = await crud_get_messages(channel_username, limit, db)
    if not messages_info:
        raise HTTPException(status_code=404, detail="Channel not found")

    return messages_info


@router.get("/{message_id}")
async def get_message_by_id(message_id: int, db: AsyncSession = Depends(get_async_session)):
    message = await crud_get_message_by_id(message_id, db)
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return message


@router.put("/{channel_username}/")
async def update_messages(channel_username: str, db: AsyncSession = Depends(get_async_session)):
    try:
        await crud_update_messages(channel_username, db)
        return {"message": "Messages updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/message/{message_id}/")
async def delete_message_by_id(message_id: int, db: AsyncSession = Depends(get_async_session)):
    result = await crud_delete_message_by_id(message_id, db)
    if not result:
        raise HTTPException(status_code=404, detail="Message not found")
    return result


@router.delete("/channel/{channel_username}/")
async def delete_messages_by_channel(channel_username: str, db: AsyncSession = Depends(get_async_session)):
    result = await crud_delete_messages_by_channel(channel_username, db)
    if not result:
        raise HTTPException(status_code=404, detail="No messages found for the channel")
    return result
