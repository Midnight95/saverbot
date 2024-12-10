import os
import logging
import asyncio
from dotenv import load_dotenv
from typing import Any, Dict, Optional, Union
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


logging.basicConfig(
        level=logging.INFO,
        filemode=f'{__name__}.log',
        format='%(asctime)s %(levelname)s %(message)s',
        )


load_dotenv()
token = os.getenv('BOT_TOKEN')

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('OHAYO')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
