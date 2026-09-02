from aiogram import Router,Dispatcher,Bot
from aiogram.filters import CommandStart
from connections import init_tables
from dotenv import load_dotenv
import handlers
import asyncio
import os

load_dotenv()

bot=Bot(os.getenv("API_KEY"))

dp=Dispatcher()

async def main():
    await init_tables()
    dp.include_router(handlers.router)
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
