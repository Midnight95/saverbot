from aiogram import Router
from aiogram.filters import Command, Filter
from aiogram.types import Message
from saverbot.parser import filter_url

router = Router()


class UrlFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        url = await filter_url(message.text)
        return url


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('OHAYO')


@router.message(UrlFilter())
async def instagram(message: Message):
    await message.answer('instagram')
