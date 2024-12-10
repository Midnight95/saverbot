from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('OHAYO')


@router.message(F.text == 'help')
async def help(message: Message):
    await message.answer('nope')
