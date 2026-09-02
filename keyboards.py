from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,CallbackQuery
def admin_buttons():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="➕ Add question",CallbackQuery="add_quetion"),
                KeyboardButton(text="✏️ Edit question",CallbackQuery="edit_quetion")
            ],
            [
                KeyboardButton(text="🗑️ Delete question",CallbackQuery="delete_quetion"),
                KeyboardButton(text="📃 List questions")
            ]
        ],
        resize_keyboard=True
    )

def user_keyboard():
        return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="➕ Add question",CallbackQuery="add_quetion"),
                KeyboardButton(text="▶️ Play game",CallbackQuery="play_game")
            ],
            [
                KeyboardButton(text="Help"),
                KeyboardButton(text="📃 List questions")
            ]
        ],
        resize_keyboard=True
    )
