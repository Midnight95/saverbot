from aiogram import Router
from aiogram.filters import Command, Filter
from aiogram.types import Message
from saverbot.parser import parse_url

router = Router()


class UrlFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        url = await parse_url(message.text)

        return url is not None


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('OHAYO')


@router.message(UrlFilter())
async def instagram(message: Message):
    await message.answer('instagram')
