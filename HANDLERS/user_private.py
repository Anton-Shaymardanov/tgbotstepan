from aiogram import  types, Router
from aiogram.filters import CommandStart, Command
from info import иницт, bmk, start, bmz

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(start)


@user_private_router.message(Command('БМЗ'))
async def men_cmd(message: types.Message):
    await message.answer(bmz)

@user_private_router.message(Command('иницт'))
async def mf_cmd(message: types.Message):
    await message.answer(иницт)

@user_private_router.message(Command('БМК'))
async def bmk_cmd(message: types.Message):
    await message.answer(bmk)