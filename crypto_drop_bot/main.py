from aiogram import Bot, Dispatcher
from aiogram.utils.executor import start_polling
from config import BOT_TOKEN
from handlers import register_handlers
from scheduler import start_scheduler

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

async def on_startup(dp):
    await start_scheduler(bot)

if __name__ == '__main__':
    start_polling(dp, skip_updates=True, on_startup=on_startup)
