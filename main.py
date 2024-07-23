import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from dotenv import load_dotenv
# Если откомментировать эту строчку, то тогда в консоле выведется print из файла config_token.py
# Вопрос, почему print не выводится без импорта?
# И почему тогда он выводится, даже если мы не используем переменную telegram_api_token?
# from config_token import telegram_api_token


logging.basicConfig(level=logging.INFO)
load_dotenv()
bot = Bot(os.getenv('TELEGRAM_API_TOKEN'))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Beautiful!"),
            types.KeyboardButton(text="So sad!")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Choose your mood"
    )
    await message.answer("What is your mood today?", reply_markup=keyboard)


@dp.message(F.text.lower() == "beautiful!")
async def with_puree(message: types.Message):
    await message.reply("Great, I knew you were fine.")


@dp.message(F.text.lower() == "so sad!")
async def without_puree(message: types.Message):
    await message.reply("This is very bad! What happened?")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())