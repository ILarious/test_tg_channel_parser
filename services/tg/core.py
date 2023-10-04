from typing import List, Optional

from telethon import functions
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from api.schemas.channel import ChannelInfoPydantic
from api.schemas.message import LatestMessagePydantic
from api.schemas.reactions import ReactionPydantic
from services.tg.config import tg_settings


class TelegramAPI:
    def __init__(self):
        self.api_id: int = tg_settings.TG_API_ID
        self.api_hash: str = tg_settings.TG_API_HASH
        self.string_session: str = tg_settings.TG_STRING_SESSION
        self.client: TelegramClient = TelegramClient(StringSession(self.string_session), self.api_id, self.api_hash)

    async def get_channel_info(self, channel_username: str) -> Optional[ChannelInfoPydantic]:
        async with self.client:
            channel_entity = await self.client.get_entity(channel_username)
            chat_entity = await self.client(functions.channels.GetFullChannelRequest(channel=channel_entity))

            channel_info_pydantic = ChannelInfoPydantic(
                id=chat_entity.full_chat.id,
                title=channel_entity.title,
                username=channel_entity.username,
                description=chat_entity.full_chat.about,
                member_count=chat_entity.full_chat.participants_count,
                link=f'https://t.me/{channel_entity.username}'
            )

            return channel_info_pydantic

    async def get_latest_messages(self, channel_username: str, limit: int) -> List[LatestMessagePydantic]:
        async with self.client:
            channel_entity = await self.client.get_entity(channel_username)
            get_messages = await self.client.get_messages(channel_entity, limit=limit)

            result = []

            for message in get_messages:
                reactions = message.reactions
                reactions_data = []

                if reactions:
                    for reaction_count in reactions.results:
                        reaction_data = ReactionPydantic(
                            emoticon=reaction_count.reaction.emoticon,
                            count=reaction_count.count
                        )
                        reactions_data.append(reaction_data)

                message_pydantic = LatestMessagePydantic(
                    id=message.id,
                    channel_id=channel_entity.id,
                    views=message.views,
                    date=message.date.strftime('%Y-%m-%d %H:%M:%S'),
                    forwards=message.forwards,
                    url=f"https://t.me/{channel_username}/{message.id}",
                    reactions=reactions_data if reactions_data else None,
                    message_text=message.text,
                )

                result.append(message_pydantic)

            return result
