from aiogram.fsm.state import StatesGroup,State

class AddQuetion(StatesGroup):
    waiting_q=State()
    waiting_a=State()

class PlayGame(StatesGroup):
    playing = State()

class EditQuestion(StatesGroup):
    waiting_question = State()
    waiting_answer = State()