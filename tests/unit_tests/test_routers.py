from tests.conftest import client


async def test_post_channel():
    # Подготавливаем данные для запроса
    channel_username = "python2day"
    # Отправляем POST запрос на создание канала
    response = client.post(f"/channels/post/{channel_username}/")

    # Проверяем статус код ответа
    assert response.status_code == 200

    # Проверяем содержимое ответа, например, ожидаем JSON с информацией о канале
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'username' in response.json()
    assert 'description' in response.json()
    assert 'member_count' in response.json()
    assert 'link' in response.json()
    assert 'messages' in response.json()


async def test_get_channel_info():
    # Подготавливаем данные для запроса
    channel_username = "python2day"

    # Отправляем GET запрос на получение информации о канале
    response = client.get(f"/channels/get/{channel_username}/")

    # Проверяем статус код ответа
    assert response.status_code == 200

    # Проверяем содержимое ответа, например, ожидаем JSON с информацией о канале
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'username' in response.json()
    assert 'description' in response.json()
    assert 'member_count' in response.json()
    assert 'link' in response.json()
    assert 'messages' in response.json()
