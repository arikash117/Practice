import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher

from bot.routers import router as main_router

dp = Dispatcher()
dp.include_router(main_router)


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token='7198230486:AAEuSM07Pu2tJt1luZoKERbdAuVOUJPs81E',
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
