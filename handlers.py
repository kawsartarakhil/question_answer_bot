from aiogram import Router,F,types,Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart,Command
from keyboards import *
from services import *
from state import *

router=Router()

@router.message(CommandStart())
async def start_handler(message:types.Message):
    user=await get_user(username=message.from_user.username)
    if not user:
        await register(username=message.chat.username,tg_id=message.from_user.id)
        if user["is_admin"]:
            await message.answer("Hello admin",reply_keyboard=admin_buttons())
        else:
            await message.answer("Hello welcome to our question and answer game",reply_keyboard=user_keyboard())


