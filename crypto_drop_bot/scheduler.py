from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.fetch_airdrops import get_airdrop_text
from config import REF_LINK

async def post_airdrop(bot: Bot):
    text = get_airdrop_text()
    text += f"\n👉 [Перейти за бонусом]({REF_LINK})"
    await bot.send_message(chat_id='@your_channel_or_user_id', text=text, parse_mode='Markdown')

scheduler = AsyncIOScheduler()

async def start_scheduler(bot: Bot):
    scheduler.add_job(post_airdrop, 'interval', hours=24, args=[bot])
    scheduler.start()
