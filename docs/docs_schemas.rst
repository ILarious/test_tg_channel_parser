.. highlight:: python

=====================
Документация api/schemas
=====================

Этот документ содержит обзор и документацию к API, созданному с использованием FastAPI.

`Модуль`_ содержит четыре класса ChannelInfo, ChannelInfoPydantic, LatestMessagePydantic и ReactionPydantic, которые представляют собой модели данных для описания информации о Telegram-каналах, последних сообщениях в каналах и реакциях на сообщения.

.. _`Модуль`: https://github.com/ILarious/test_tg_channel_parser/tree/main/api/schemas


Класс ChannelInfo
------------

.. code-block:: python

    class ChannelInfo(BaseModel):
        """
        Модель данных для представления информации о Telegram-канале.

        Attributes:
            id (int): Уникальный идентификатор канала.
            title (str): Название канала.
            username (str): Имя пользователя канала.
            description (Optional[str], optional): Описание канала (может быть None).
            member_count (int): Количество участников канала.
            link (HttpUrl): Ссылка на канал в формате HTTP URL.
            messages (Optional[List[LatestMessagePydantic]], optional): Список последних сообщений (может быть None).

        """

        id: int
        title: str
        username: str
        description: Optional[str] = None
        member_count: int
        link: HttpUrl
        messages: Optional[List[LatestMessagePydantic]]

Класс ChannelInfoPydantic
------------

.. code-block:: python

    class ChannelInfoPydantic(BaseModel):
        """
        Модель данных Pydantic для представления информации о Telegram-канале без списка сообщений.

        Attributes:
            id (int): Уникальный идентификатор канала.
            title (str): Название канала.
            username (str): Имя пользователя канала.
            description (Optional[str], optional): Описание канала (может быть None).
            member_count (int): Количество участников канала.
            link (HttpUrl): Ссылка на канал в формате HTTP URL.

        """

        id: int
        title: str
        username: str
        description: Optional[str] = None
        member_count: int
        link: HttpUrl

Класс LatestMessagePydantic
------------

.. code-block:: python

    class LatestMessagePydantic(BaseModel):
        """
        Модель данных Pydantic для представления информации о последнем сообщении в Telegram-канале.

        Attributes:
            id (int): Уникальный идентификатор сообщения.
            channel_id (int): Уникальный идентификатор канала, к которому относится сообщение.
            views (int): Количество просмотров сообщения.
            date (str): Дата и время отправки сообщения.
            forwards (int): Количество пересылок сообщения.
            url (str): URL-ссылка на сообщение.
            reactions (Optional[List[ReactionPydantic]], optional): Список реакций на сообщение (может быть None).
            message_text (str): Текст сообщения.

        """
        id: int
        channel_id: int
        views: int
        date: str
        forwards: int
        url: str
        reactions: Optional[List[ReactionPydantic]]
        message_text: str

Класс ReactionPydantic
------------

.. code-block:: python

    class ReactionPydantic(BaseModel):
        """
        Модель данных Pydantic для представления реакции на сообщение в Telegram-канале.

        Attributes:
            emoticon (str): Эмотикон, представляющий реакцию.
            count (int): Количество этой реакции на сообщение.

        """
        emoticon: str
        count: int
