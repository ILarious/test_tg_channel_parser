from api.schemas.channel import ChannelInfoPydantic
from api.schemas.message import LatestMessagePydantic
from services.tg.core import TelegramAPI
from typing import List, Optional


async def get_tg_channel_info(channel_username: str) -> Optional[ChannelInfoPydantic]:
    telegram = TelegramAPI()
    channel_info = await telegram.get_channel_info(channel_username)
    return channel_info


async def get_tg_latest_messages(channel_username: str, limit: int) -> List[LatestMessagePydantic]:
    telegram = TelegramAPI()
    latest_messages = await telegram.get_latest_messages(channel_username, limit=limit)
    return latest_messages
