import os
import logging
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from saverbot.app.handlers import router


logging.basicConfig(
        level=logging.DEBUG,
        filemode=f'{__name__}.log',
        format='%(asctime)s %(levelname)s %(message)s',
        )


load_dotenv()
token = os.getenv('BOT_TOKEN')

bot = Bot(token=token)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
