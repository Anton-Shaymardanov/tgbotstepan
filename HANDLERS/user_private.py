from aiogram import  types, Router
from aiogram.filters import CommandStart, Command
from info import txt1

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Напишите "/menu" для того чтобы узнать о функционале бота😉')


@user_private_router.message(Command('menu'))
async def as_cmd(message: types.Message):
    await message.answer(txt1)

@user_private_router.message(Command('иницт'))
async def vf_cmd(message: types.Message):
    await message.answer('ицвильнихт')