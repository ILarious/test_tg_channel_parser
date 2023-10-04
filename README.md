# Тестовое задание

Разработать приложение для парсинга и сохранения информации и последних сообщений из Telegram-каналов/групп, с возможностью запроса через API и предоставления данных в формате JSON.

## Требования

- Docker
- Python версии 3.7 и выше 
- Зависимости перечисленны в файле `requirements.txt`

---

## Документация

https://github.com/ILarious/test_tg_channel_parser/tree/main/docs

---

## Структура проекта
```
project/
    ├── api/
    │   ├── routers/
    │   │   └── channel.py
    │   └── schemas/
    │       ├── channel.py
    │       ├── message.py
    │       └── reactions.py
    │
    ├── services/
    │   ├── db/
    │   │   ├── crud/
    │   │   │   └── channel.py
    │   │   ├── migrations/
    │   │   │   ├── versions/
    │   │   │   ├── env.py
    │   │   │   └── ...
    │   │   ├── config.py
    │   │   ├── core.py
    │   │   ├── mmodels.py
    │   │   └── alembic.ini 
    │   └── tg/
    │       ├── config.py
    │       ├── core.py
    │       └── utils.py 
    │
    ├── tests/
    │   ├── integration_tests/
    │   │   ├── conftest.py
    │   │   ├── test_crud.py
    │   │   └── test_tg_core.py 
    │   ├── unit_tests/
    │   │   └── test_routers.py
    │   └── conftest.py
    │
    ├── .env
    ├── .env.example
    ├── .gitignore
    ├── docker-compose.yml
    ├── README.md
    ├── main.py
    ├── Dockerfile
    ├── pyproject.toml
    └── requirements.txt
```
---

## Установка

1. **Клонировать репозиторий:**

   ```bash
   git clone https://github.com/ILarious/test_tg_channel_parser.git
   ```
2. **Переменные окружения**

- Создать файл .env и добавить переменные окружения согласно .env.example

Как создать Telegram app, получть api_id и api_hash:
   https://core.telegram.org/api/obtaining_api_id#obtaining-api-id


Как получить StringSession:
   https://docs.telethon.dev/en/stable/concepts/sessions.html#string-sessions
     
   


4. **Создание Docker контейнеров с FastAPI и PostgreSQL**

- Убедитесь, что Docker установлен и запущен на вашей машине.

- Перейдите в корневой каталог вашего проекта, где находится файл `docker-compose.yml`.

- Запустите Docker контейнер с PostgreSQL с помощью следующей команды:

   ```bash
   docker-compose up -d
   ```
   Это команда запустит PostgreSQL и FastAPI-приложение в контейнерах.



- Подождите, пока Docker Compose завершит сборку и запуск контейнеров. Вы увидите вывод в консоли, указывающий на успешное выполнение.


   Чтобы остановить контейнеры, выполните команду:

   ```bash
   docker-compose down
   ```
---

## Использование
- Приложение доступно по адресу http://localhost:8000. Откройте этот URL в вашем веб-браузере.
- В качестве канала для теста: Cutecats08
- Кол-во последних постов: 1
  
### Делаем запрос информации о канале Telegram и сохраняет ее в базу данных используя Swagger UI.


![image](https://github.com/ILarious/test_tg_channel_parser/assets/98268609/b752cc48-f172-45fc-a4ae-40266a0173e4)

Получаем статус код 200 и информация о созданном канале, если успешно
![image](https://github.com/ILarious/test_tg_channel_parser/assets/98268609/057e2d7a-d5a3-40a8-afa2-f871793708dd)

Иначе статус код - 404, если канал не найден или имеет закрытый доступ
![image](https://github.com/ILarious/test_tg_channel_parser/assets/98268609/2d3cacf7-f36e-4b51-9968-2a10c1ccb7a2)

Или статус код - 409, если канал уже добавлен в базу данных
![image](https://github.com/ILarious/test_tg_channel_parser/assets/98268609/41281635-10b6-4d4a-aef5-8e61b86390a9)

### Делаем запрос информации о канале в базу данных используя Swagger UI.

Получаем статус код 200 и информация о созданном канале, если успешно
![image](https://github.com/ILarious/test_tg_channel_parser/assets/98268609/66d4fa37-4108-4fb7-a9f4-6598df3d21ab)

Иначе статус код - 404, если канал не найден
![image](https://github.com/ILarious/test_tg_channel_parser/assets/98268609/2d3cacf7-f36e-4b51-9968-2a10c1ccb7a2)


---
## Тестирование с помощью pytest

Если вам нужно запустить тесты, следуйте этим инструкциям:

1. Убедитесь, что вы находитесь в корневой директории проекта.
   
2. Убедитесь, что обе эти команды были выполнены:

   ```bash
    docker-compose up -d --build
   ```

   ```bash
    docker-compose -f docker-compose.test.yml up -d --build
   ```

4. Для запуска тестов, выполните следующую команду:

   ```bash
   docker exec -it my_fastapi pytest
   ```

5. Результаты тестов будут выведены в вашей консоли.

6. Чтобы отсановить контейнеры для тестов, выполните команду:

   ```bash
    docker-compose -f docker-compose.test.yml down
   ```

## Дополнительная информация

### Управление миграциями базы данных

Для управления миграциями базы данных используется Alembic. Вы можете применить миграции, выполнив следующую команду:

```shell
docker-compose exec fastapi_app alembic upgrade head
```

Эта команда применяет все доступные миграции к вашей базе данных PostgreSQL.

### Пересборка контейнеров после изменений в коде

Если вам необходимо пересобрать контейнеры после внесения изменений в код приложения, выполните следующие команды:

1. Остановите и удалите существующие контейнеры:

```shell
docker-compose down
```

2. Затем пересоберите и запустите контейнеры снова, включая пересборку образов:

```shell
docker-compose up -d --build
```

Эти команды пересоздадут контейнеры с последними изменениями в коде вашего приложения.
