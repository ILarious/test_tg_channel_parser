.. highlight:: python

======================
Документация services/tg/utils.py
======================

Этот документ содержит обзор и документацию к `модулю`_, который предоставляет функции для взаимодействия с Telegram API и получения информации о каналах и последних сообщениях.

.. _`модулю`: https://github.com/ILarious/test_tg_channel_parser/blob/main/services/tg/utils.py

Функция get_tg_channel_info
---------------------------

.. code-block:: python

    async def get_tg_channel_info(channel_username: str) -> Optional[ChannelInfoPydantic]:
        """
        Получает информацию о Telegram-канале.

        Args:
            channel_username (str): Имя пользователя (username) канала.

        Returns:
            Optional[ChannelInfoPydantic]: Информация о канале или None, если канал не найден.
        """

        telegram = TelegramAPI()
        channel_info = await telegram.get_channel_info(channel_username)
        return channel_info

Функция `get_tg_channel_info` предназначена для получения информации о Telegram-канале по его имени пользователя (username). Она принимает аргумент `channel_username` (имя пользователя канала) и возвращает информацию о канале в форме объекта `ChannelInfoPydantic`. Если канал не найден, возвращается `None`.

Функция get_tg_latest_messages
-------------------------------

.. code-block:: python

    async def get_tg_latest_messages(channel_username: str, limit: int) -> List[LatestMessagePydantic]:
        """
        Получает последние сообщения из Telegram-канала.

        Args:
            channel_username (str): Имя пользователя (username) канала.
            limit (int): Количество сообщений для получения.

        Returns:
            List[LatestMessagePydantic]: Список последних сообщений.
        """

        telegram = TelegramAPI()
        latest_messages = await telegram.get_latest_messages(channel_username, limit=limit)
        return latest_messages

Функция `get_tg_latest_messages` предназначена для получения последних сообщений из Telegram-канала. Она принимает аргументы `channel_username` (имя пользователя канала) и `limit` (количество сообщений для получения) и возвращает список последних сообщений в форме объектов `LatestMessagePydantic`.