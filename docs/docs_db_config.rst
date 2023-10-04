.. highlight:: python

============================
Документация services/db/config.py
============================

Этот документ содержит обзор и документацию к `модулю`_, который предоставляет функциональность для управления настройками приложения с использованием Pydantic.

.. _`Модулю`: https://github.com/ILarious/test_tg_channel_parser/blob/main/services/db/config.py

Класс DatabaseSettings
----------------------

.. code-block:: python

    class DatabaseSettings(BaseSettings):
        """
        Класс для настройки параметров базы данных.

        Attributes:
            DB_HOST (str): Хост базы данных.
            DB_PORT (int): Порт базы данных.
            DB_USER (str): Имя пользователя базы данных.
            DB_PASS (str): Пароль пользователя базы данных.
            DB_NAME (str): Имя базы данных.

            DB_HOST_TEST (str): Хост тестовой базы данных.
            DB_PORT_TEST (int): Порт тестовой базы данных.
            DB_USER_TEST (str): Имя пользователя тестовой базы данных.
            DB_PASS_TEST (str): Пароль пользователя тестовой базы данных.
            DB_NAME_TEST (str): Имя тестовой базы данных.

        Methods:
            db_url_asyncpg: Возвращает URL-ссылку для асинхронного подключения к базе данных.
            test_db_url_asyncpg: Возвращает URL-ссылку для асинхронного подключения к тестовой базе данных.

        """
        DB_HOST: str
        DB_PORT: int
        DB_USER: str
        DB_PASS: str
        DB_NAME: str

        DB_HOST_TEST: str
        DB_PORT_TEST: int
        DB_USER_TEST: str
        DB_PASS_TEST: str
        DB_NAME_TEST: str

        def db_url_asyncpg(self) -> str:
            """
            Возвращает URL-ссылку для асинхронного подключения к базе данных.

            Returns:
                str: URL-ссылка для асинхронного подключения к базе данных.
            """
            pass

        def test_db_url_asyncpg(self) -> str:
            """
            Возвращает URL-ссылку для асинхронного подключения к тестовой базе данных.

            Returns:
                str: URL-ссылка для асинхронного подключения к тестовой базе данных.
            """
            pass

        model_config: SettingsConfigDict = SettingsConfigDict(env_file=".env", extra='ignore')

    db_settings: DatabaseSettings = DatabaseSettings()

Класс `DatabaseSettings` представляет настройки параметров базы данных. В нем определены атрибуты для хоста, порта, имени пользователя, пароля и имени базы данных как для основной, так и для тестовой базы данных. Класс также содержит методы `db_url_asyncpg` и `test_db_url_asyncpg`, которые возвращают URL-ссылки для асинхронного подключения к базе данных и тестовой базе данных соответственно.

Параметры `model_config` и `db_settings` используются для конфигурации настроек модели с помощью файла `.env` и создания экземпляра класса `DatabaseSettings` для доступа к настройкам базы данных.
