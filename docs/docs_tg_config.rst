.. highlight:: python

=======================
Документация tg_settings
=======================

Этот документ содержит обзор и документацию к `модулю`_, который представляет настройки для взаимодействия с Telegram API.

.. _`модулю`: https://github.com/ILarious/test_tg_channel_parser/blob/main/services/tg/config.py

Класс TelegramSettings
-----------------------

.. code-block:: python

    class TelegramSettings(BaseSettings):
        """
        Класс для настройки параметров Telegram API.

        Attributes:
            TG_API_ID (int): Идентификатор API Telegram.
            TG_API_HASH (str): Хеш-код API Telegram.
            TG_STRING_SESSION (str): Строковая сессия Telegram.

        model_config: SettingsConfigDict = SettingsConfigDict(env_file=".env", extra='ignore')

        """
        TG_API_ID: int
        TG_API_HASH: str
        TG_STRING_SESSION: str

        model_config: SettingsConfigDict = SettingsConfigDict(env_file=".env", extra='ignore')

`TelegramSettings` представляет настройки параметров Telegram API. В нем определены атрибуты для идентификатора API Telegram (`TG_API_ID`), хеш-кода API Telegram (`TG_API_HASH`) и строки сессии Telegram (`TG_STRING_SESSION`).

Параметр `model_config` используется для конфигурации настроек модели с использованием файла `.env` и указывает игнорировать дополнительные настройки.
