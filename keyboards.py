from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,CallbackQuery
def admin_buttons():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="➕ Add question"),
                KeyboardButton(text="✏️ Edit question")
            ],
            [
                KeyboardButton(text="🗑️ Delete question"),
                KeyboardButton(text="📃 List questions")
            ]
        ],
        resize_keyboard=True
    )

def user_keyboard():
        return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="➕ Add question"),
                KeyboardButton(text="▶️ Play game")
            ],
            [
                KeyboardButton(text="Help"),
                KeyboardButton(text="📃 List questions")
            ]
        ],
        resize_keyboard=True
    )
