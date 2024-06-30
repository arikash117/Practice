import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher

from settings.config import settings
from routers import router as main_router

dp = Dispatcher()
dp.include_router(main_router)


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=settings.bot_token,
    )
    await dp.start_polling(bot)


if __name__ == '__name__':
    asyncio.run(main())