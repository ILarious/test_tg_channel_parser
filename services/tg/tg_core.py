from telethon import functions
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

from services.tg.tg_config import tg_settings


class TelegramAPI:
    def __init__(self, ):
        self.api_id = tg_settings.TG_API_ID
        self.api_hash = tg_settings.TG_API_HASH
        self.string_session = tg_settings.TG_STRING_SESSION
        self.client = TelegramClient(StringSession(self.string_session), self.api_id, self.api_hash)

    async def get_channel_info(self, channel_username):
        async with self.client:
            channel_entity = await self.client.get_entity(channel_username)
            chat_entity = await self.client(functions.channels.GetFullChannelRequest(channel=channel_entity))

            result = {
                'id': chat_entity.full_chat.id,
                'title': channel_entity.title,
                'username': channel_entity.username,
                'description': chat_entity.full_chat.about,
                'member_count': chat_entity.full_chat.participants_count,
                'link': f'https://t.me/{channel_entity.username}'
            }

            return result

    async def get_latest_messages(self, channel_username, limit):
        async with self.client:
            channel_entity = await self.client.get_entity(channel_username)
            get_messages = await self.client.get_messages(channel_entity, limit=limit)

            result = []

            for message in get_messages:
                result.append({
                    'id': message.id,
                    'channel_id': channel_entity.id,
                    'views': message.views,
                    'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'forwards': message.forwards,
                    'url': f"https://t.me/{channel_username}/{message.id}",
                    'reactions': message.reactions.to_dict() if message.reactions else None,
                    'message text': message.text
                })

            return result
