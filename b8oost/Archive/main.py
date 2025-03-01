import os
import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

BOT_TOKEN=os.environ.get('BOT_TOKEN')

if not BOT_TOKEN:
    exit("Error: no token provided")

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот отключен')