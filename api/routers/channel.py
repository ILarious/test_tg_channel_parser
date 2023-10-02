from asyncpg.exceptions import UniqueViolationError
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from telethon.errors import UsernameNotOccupiedError

from services.db.crud.channel import crud_post_channel, crud_get_channel
from services.db.db_core import get_async_session
from api.schemas.channel import ChannelInfo
from services.tg.tg_utils import get_tg_channel_info, get_tg_latest_messages

router = APIRouter(
    prefix="/channels",
    tags=["channels"],
)


@router.post("/post/{channel_username}/")
async def post_channel(
        channel_username: str,
        limit_latest_messages: int = 10,
        db: AsyncSession = Depends(get_async_session)):
    try:
        channel_info = await get_tg_channel_info(channel_username)
        messages_info = await get_tg_latest_messages(channel_username, limit_latest_messages)
        post_channel = await crud_post_channel(channel_info, messages_info, db)

        return post_channel

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
async def get_channel_info(channel_name: str, db: AsyncSession = Depends(get_async_session)):
    get_channel = await crud_get_channel(channel_name, db)

    if not get_channel:
        raise HTTPException(
            status_code=404,
            detail='Channel not found'
        )

    return get_channel
