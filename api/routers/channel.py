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


@router.post("/post/{channel_username}/", response_model=ChannelInfo)
async def post_channel(
        channel_username: str,
        limit_latest_messages: int = 10,
        db: AsyncSession = Depends(get_async_session)
) -> ChannelInfo:
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


@router.get("/get/{channel_username}/", response_model=ChannelInfo)
async def get_channel_info(
        channel_username: str,
        db: AsyncSession = Depends(get_async_session)
) -> ChannelInfo:
    response: ChannelInfo = await crud_get_channel(channel_username, db)

    if not response:
        raise HTTPException(
            status_code=404,
            detail='Channel not found'
        )

    return response
