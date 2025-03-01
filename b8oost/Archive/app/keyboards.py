from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

WEBSITE_URL = 'https://comforting-lamington-bb982e.netlify.app/'

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Войти')],
        [KeyboardButton(text='O нас')],
        [KeyboardButton(text='Открыть сайт')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберете пункт меню'
)
website_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Открыть сайт", url=WEBSITE_URL)]
    ])