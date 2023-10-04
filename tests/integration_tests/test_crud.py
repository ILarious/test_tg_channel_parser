from typing import Any, Dict, List

from api.schemas.channel import ChannelInfoPydantic
from api.schemas.message import LatestMessagePydantic
from api.schemas.reactions import ReactionPydantic
from services.db.crud.channel import crud_get_channel, crud_post_channel
from tests.conftest import async_session_maker, client


async def test_integration_crud_post_channel():
    channel_info: ChannelInfoPydantic = ChannelInfoPydantic(
        id=1,
        username="test_channel",
        title="Test Channel",
        description="This is a test channel",
        member_count=100,
        link="https://t.me/test_channel",
    )

    latest_messages: List[LatestMessagePydantic] = [
        LatestMessagePydantic(
            id=1,
            channel_id=1,
            views=1,
            date="2023-10-03 10:09:24",
            forwards=1,
            url="https://t.me/test_channel/1",
            reactions=[ReactionPydantic(
                emoticon="👍",
                count=1
            )],
            message_text="string"
        )
    ]

    messages_info: List[Dict[Any, Any]] = [message.dict() for message in latest_messages]

    async with async_session_maker() as session:
        db_channel = await crud_post_channel(channel_info, messages_info, session)

        response = client.get(f"/channels/get/test_channel/")

        assert response.status_code == 200

        assert response.json() == {
            'id': db_channel.id,
            'username': db_channel.username,
            'title': db_channel.title,
            'description': db_channel.description,
            'member_count': db_channel.member_count,
            'link': db_channel.link,
            'messages': db_channel.messages
        }, "Channel not found"


async def test_integration_crud_get_channel():
    async with async_session_maker() as session:
        db_channel = await crud_get_channel("test_channel", session)

        assert db_channel is not None, "Channel not found"
