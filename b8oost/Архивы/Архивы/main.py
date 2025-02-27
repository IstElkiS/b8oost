import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

async def main():
    bot = Bot(token='7681784605:AAHeUTuHogYwUTjCnkCve838BGD1-4vAUlg')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот отключен')