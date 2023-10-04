.. highlight:: python

=========================
Документация services/tg/core.py
=========================

Этот документ содержит обзор и документацию к `модулю`_, который предоставляет функциональность для взаимодействия с Telegram API.

.. _`модулю`: https://github.com/ILarious/test_tg_channel_parser/blob/main/services/tg/core.py

Класс TelegramAPI
------------------

.. code-block:: python

    class TelegramAPI:
        """
        Класс для взаимодействия с Telegram API.

        Attributes:
            api_id (int): Идентификатор API Telegram.
            api_hash (str): Хеш-код API Telegram.
            string_session (str): Строковая сессия Telegram.
            client (TelegramClient): Клиент Telegram.

        """
        def __init__(self):
            self.api_id: int = tg_settings.TG_API_ID
            self.api_hash: str = tg_settings.TG_API_HASH
            self.string_session: str = tg_settings.TG_STRING_SESSION
            self.client: TelegramClient = TelegramClient(StringSession(self.string_session), self.api_id, self.api_hash)

        async def get_channel_info(self, channel_username: str) -> Optional[ChannelInfoPydantic]:
            """
            Получает информацию о Telegram-канале.

            Args:
                channel_username (str): Имя пользователя (username) канала.

            Returns:
                Optional[ChannelInfoPydantic]: Информация о канале или None, если канал не найден.
            """
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
            """
            Получает последние сообщения из Telegram-канала.

            Args:
                channel_username (str): Имя пользователя (username) канала.
                limit (int): Количество сообщений для получения.

            Returns:
                List[LatestMessagePydantic]: Список последних сообщений.
            """
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


Класс `TelegramAPI` предоставляет функциональность для взаимодействия с Telegram API. В нем определены следующие атрибуты и методы:
    - `api_id` (int): Идентификатор API Telegram.
    - `api_hash` (str): Хеш-код API Telegram.
    - `string_session` (str): Строковая сессия Telegram.
    - `client` (TelegramClient): Клиент Telegram.

Метод `get_channel_info` получает информацию о Telegram-канале по его имени пользователя (username). Он принимает аргумент `channel_username` и возвращает информацию о канале в форме объекта `ChannelInfoPydantic`. Если канал не найден, возвращается `None`.

Метод `get_latest_messages` получает последние сообщения из Telegram-канала. Он принимает аргументы `channel_username` (имя пользователя канала) и `limit` (количество сообщений для получения) и возвращает список последних сообщений в форме объектов `LatestMessagePydantic`.