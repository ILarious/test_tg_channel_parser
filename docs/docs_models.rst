.. highlight:: python

=================================
Документация services/db/models.py
=================================

Этот документ содержит обзор и документацию к `модулю`_, который содержит описания моделей SQLAlchemy для базы данных.

.. _`модулю`: https://github.com/ILarious/test_tg_channel_parser/blob/main/services/db/models.py

Модель ChannelInfo
------------------

.. code-block:: python

    class ChannelInfo(Base):
        """
        Модель данных для описания информации о Telegram-канале.

        Attributes:
            id (int): Уникальный идентификатор канала (первичный ключ).
            username (str): Имя пользователя канала (уникальное поле, индексированное).
            title (str): Название канала.
            description (Optional[str], optional): Описание канала (может быть None).
            member_count (int): Количество участников канала.
            link (str): Ссылка на канал.
            messages (Optional[dict], optional): Информация о сообщениях канала (может быть None).

        """
        __tablename__ = 'channel_info'

        id: int = Column(Integer, primary_key=True, index=True)
        username: str = Column(String, unique=True, index=True)
        title: str = Column(String)
        description: Optional[str] = Column(Text)
        member_count: int = Column(Integer)
        link: str = Column(String)
        messages: Optional[dict] = Column(JSONB)

Модель `ChannelInfo` представляет информацию о Telegram-канале. Она содержит следующие атрибуты:
- `id` (int): Уникальный идентификатор канала (первичный ключ).
- `username` (str): Имя пользователя канала (уникальное поле, индексированное).
- `title` (str): Название канала.
- `description` (Optional[str], optional): Описание канала (может быть None).
- `member_count` (int): Количество участников канала.
- `link` (str): Ссылка на канал.
- `messages` (Optional[dict], optional): Информация о сообщениях канала (может быть None).

Модель описана в классе `ChannelInfo`, который наследуется от базового класса `Base`. Метаданные (`metadata`) берутся из базового класса.

