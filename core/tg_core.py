from telethon import functions
from telethon.sync import TelegramClient
from telethon.sessions import StringSession


class TelegramAPI:
    def __init__(self, api_id, api_hash, session_string):
        self.api_id = api_id
        self.api_hash = api_hash
        self.session_string = session_string
        self.client = None

    async def connect(self):
        self.client = TelegramClient(StringSession(self.session_string), self.api_id, self.api_hash)
        await self.client.start()

    async def disconnect(self):
        if self.client:
            await self.client.disconnect()

    async def get_channel_info(self, channel_username):
        channel_entity = await self.client.get_entity(channel_username)
        chat_entity = await self.client(functions.channels.GetFullChannelRequest(channel=channel_entity))
        return {
            'id': channel_entity.id,
            'title': channel_entity.title,
            'username': channel_entity.username,
            'description': chat_entity.full_chat.about,
            'member_count': chat_entity.full_chat.participants_count,
            'link': f'https://t.me/{channel_entity.username}'
        }

    async def get_latest_messages(self, channel_username, limit):
        channel_entity = await self.client.get_entity(channel_username)
        messages = await self.client.get_messages(channel_entity, limit=limit)
        result = []
        for message in messages:
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