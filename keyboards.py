from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
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

def alphabet_keyboard():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyboard = []
    row = []

    for letter in letters:
        row.append(InlineKeyboardButton(text=letter,callback_data=f"letter_{letter}"))

        if len(row) == 5:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)