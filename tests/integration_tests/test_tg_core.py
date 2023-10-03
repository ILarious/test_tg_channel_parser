from api.schemas.message import LatestMessagePydantic
from services.tg.core import TelegramAPI


async def test_telegram_client_connect(telegram_client: TelegramAPI):
    assert telegram_client.client.is_user_authorized()


async def test_get_channel_info(telegram_client: TelegramAPI):
    channel_username = "python2day"

    channel_info = await telegram_client.get_channel_info(channel_username)

    assert channel_info is not None
    assert channel_info.username == channel_username


async def test_get_latest_messages(telegram_client: TelegramAPI):
    channel_username = "python2day"
    limit = 10

    latest_messages = await telegram_client.get_latest_messages(channel_username, limit=limit)

    assert latest_messages is not None
    assert len(latest_messages) == limit
    assert all(isinstance(message, LatestMessagePydantic) for message in latest_messages)
