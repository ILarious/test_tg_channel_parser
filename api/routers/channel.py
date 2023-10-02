from asyncpg.exceptions import UniqueViolationError
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from telethon.errors import UsernameNotOccupiedError

from services.db.crud.channel import crud_post_channel, crud_get_channel, crud_update_channel, crud_delete_channel
from services.db.db_core import get_async_session
from api.schemas.channel import ChannelInfo

router = APIRouter(
    prefix="/channels",
    tags=["channels"],
)


@router.post("/{channel_username}/", response_model=ChannelInfo)
async def post_channel(channel_name: str, db: AsyncSession = Depends(get_async_session)):
    try:
        post_channel = await crud_post_channel(channel_name, db)
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


@router.get("/{channel_username}/", response_model=ChannelInfo)
async def get_channel_info(channel_name: str, db: AsyncSession = Depends(get_async_session)):
    get_channel = await crud_get_channel(channel_name, db)
    if not get_channel:
        raise HTTPException(
            status_code=404,
            detail='Channel not found'
        )
    return get_channel


@router.put("/{channel_username}/", response_model=ChannelInfo)
async def update_channel(channel_username: str, db: AsyncSession = Depends(get_async_session)):
    updated_channel = await crud_update_channel(db, channel_username)
    if updated_channel is None:
        raise HTTPException(status_code=404, detail="Channel not found")
    return updated_channel


@router.delete("/{channel_username}/", response_model=ChannelInfo)
async def delete_channel(channel_username: str, db: AsyncSession = Depends(get_async_session)):
    deleted_channel = await crud_delete_channel(db, channel_username)
    if deleted_channel is None:
        raise HTTPException(status_code=404, detail="Channel not found")
    return deleted_channel
