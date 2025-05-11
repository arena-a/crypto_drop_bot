from aiogram import types, Dispatcher
from config import REF_LINK

async def start_command(message: types.Message):
    await message.answer(
        "👋 Привет! Я CryptoDropBot.\n\nПолучай дропы, новости и бонусы каждый день!",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("🚀 Перейти за бонусом", url=REF_LINK)
        )
    )

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
