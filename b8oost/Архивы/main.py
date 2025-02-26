import asyncio
from aiogram import Bot, Dispatcher, MagicFilter
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

bot = Bot(token='7681784605:AAHeUTuHogYwUTjCnkCve838BGD1-4vAUlg')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.reply('Как дела?')

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот отключен')