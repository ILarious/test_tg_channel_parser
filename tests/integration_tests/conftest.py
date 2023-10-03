from typing import AsyncGenerator

import pytest

from services.tg.core import TelegramAPI

@pytest.fixture(scope="session")
async def telegram_client() -> AsyncGenerator[TelegramAPI, None]:
    client = TelegramAPI()
    yield client