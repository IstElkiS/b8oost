from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
'''from aiogram.fsm.context import FSMContext'''


import app.keyboards as kb

router = Router()

class Register(StatesGroup):
    name = State()
    status = State()
    password = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)
    await message.reply('Как дела?')

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')

@router.callback_query(F.data == 'log in')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы вошли')
    await callback.message.answer('Вы вошли')

@router.message(F.text == 'Открыть сайт')
async def open_website(message: Message):
    await message.answer("Нажмите кнопку ниже, чтобы открыть сайт:", reply_markup=kb.website_keyboard)

'''
@router.message(Command('sign up'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ваше имя')

@router.message(Register.name)
async def register_name(message:Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer()'''    