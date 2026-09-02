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
        user=await get_user(message.chat.username)
    if user["is_admin"]:
        await message.answer("Hello admin",reply_markup=admin_buttons())
    else:
        await message.answer("Hello welcome to our question and answer game",reply_markup=user_keyboard())

@router.message(F.text=="➕ Add question")
async def add_question_handler(message:types.Message,state:FSMContext):
    await state.set_state(AddQuetion.waiting_q)
    await message.answer("Enter the question:")
    

@router.message(AddQuetion.waiting_q)
async def add_q(message:types.Message,state:FSMContext):
    await state.update_data(question=message.text)
    await state.set_state(AddQuetion.waiting_a)
    await message.answer("Enter the answer")

@router.message(AddQuetion.waiting_a)
async def add_a(message:types.Message,state:FSMContext):
    data=await state.get_data()
    question=data["question"]
    answer=message.text
    user=await get_user(message.chat.username)
    await add_question(question=question,answer=answer,user_id=user["id"])
    await state.clear()
    await message.answer("Qestion added")


@router.message(F.text=="Help")
async def help_handler(message:types.Mesaage):
    await message.answer(f"Add question button is for adding a question\nPlay game button is to play the game\nHelp button is to know about our buttons and commands\n list questions is to view all the questions that you have entered")


@router.message(F.text == "📃 List questions")
async def list_questions_handler(message: types.Message):
    user=await get_user(message.chat.username)
    questions = await get_user_quetions(user["id"])
    if not questions:
        await message.answer("You haven't added any questions yet.")
        return
    text = "📃 Your questions:\n\n"
    for question in questions:
        text += f"❓{question['question']}\n"

    await message.answer(text)