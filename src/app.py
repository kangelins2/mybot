import asyncio
import os
from asyncio import TaskGroup
from typing import Callable, Awaitable

import anyio
import uvicorn
from aiogram import Dispatcher, Bot
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.credentails import settings
from src.db.database import engine
from src.db.models import Base
from src.routers.start import router
from src.endpoints.emails import router as emails_router
dp = Dispatcher()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


dp.include_router(router)

app.include_router(emails_router)



async def start_server(tg: TaskGroup, server: Callable[[], Awaitable]):
    await server()
    tg.cancel_scope.cancel()


async def start_bot(tg: TaskGroup):
    bot = Bot(token=settings.TG_BOT_TOKEN)
    await dp.start_polling(bot)
    tg.cancel_scope.cancel()


async def main():
    config = (uvicorn.Config(
        "src.app:app", "0.0.0.0", log_level=4, workers=1, reload=False,
    ))

    async with engine.begin() as session:
        await session.run_sync(Base.metadata.create_all)
    # запуск сервера и бота
    server = uvicorn.Server(config)
    async with anyio.create_task_group() as tg:
        tg.start_soon(start_server, tg, server.serve)
        tg.start_soon(start_bot, tg)
        # tg.start_soon(run_migration)


