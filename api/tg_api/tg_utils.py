from config.tg_config import tg_settings
from core.tg_core import TelegramAPI

api_id = tg_settings.TG_API_ID
api_hash = tg_settings.TG_API_HASH
session_string = tg_settings.TG_STRING_SESSION


async def get_tg_channel_info(channel_username):
    telegram = TelegramAPI(api_id, api_hash, session_string)
    await telegram.connect()
    channel_info = await telegram.get_channel_info(channel_username)
    await telegram.disconnect()
    return channel_info


async def get_tg_latest_messages(channel_username, limit=10):
    telegram = TelegramAPI(api_id, api_hash, session_string)
    await telegram.connect()
    latest_messages = await telegram.get_latest_messages(channel_username, limit=limit)
    await telegram.disconnect()
    return latest_messages