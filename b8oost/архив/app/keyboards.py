from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

WEBSITE_URL='C:\Users\Пользователь\Desktop\b8oost\index.html'

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Войти')],
                                     [KeyboardButton(text='O нас')]],
                            resize_keyboard=True,
                            input_field_placeholder='Выберете пункт меню')

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Зарегистрироваться', callback_data='sign up', url=WEBSITE_URL)]])