from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Козрина')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='O нас')]],
                            resize_keyboard=True,
                            input_field_placeholder='Выберете пункт меню')

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Футболки', callback_data='t-shirt')],
    [InlineKeyboardButton(text='Кроссовки', callback_data='sneakers')],
    [InlineKeyboardButton(text='Кепки', callback_data='cap')]])