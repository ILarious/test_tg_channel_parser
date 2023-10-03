import uvicorn
import asyncio
from fastapi import FastAPI

# Импорт роутеров, определенных в других файлах
from api.routers.channel import router as router_channels

# Создание экземпляра FastAPI приложения
app: FastAPI = FastAPI(
    title="final_course_project",  # Название вашего приложения
)

# Включение роутеров для обработки маршрутов API
app.include_router(router_channels)


# Определение функции main для запуска сервера
async def main():
    # Создание конфигурации сервера с указанием приложения, порта, уровня логирования и режима перезагрузки
    config: uvicorn.Config = uvicorn.Config("main:app", port=8000, log_level="info", reload=True)

    # Создание объекта сервера с указанной конфигурацией
    server: uvicorn.Server = uvicorn.Server(config)

    # Запуск сервера
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
