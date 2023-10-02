from services.tg.tg_core import TelegramAPI


async def get_tg_channel_info(channel_username):
    telegram = TelegramAPI()
    channel_info = await telegram.get_channel_info(channel_username)
    return channel_info


async def get_tg_latest_messages(channel_username, limit):
    telegram = TelegramAPI()
    latest_messages = await telegram.get_latest_messages(channel_username, limit=limit)
    return latest_messages
