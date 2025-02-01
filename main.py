import asyncio
import logging
import sys
import wikipedia

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

wikipedia.set_lang('uz')

API_TOKEN = "5851858948:AAFq9Xg_lMjhZOmED4ztZgomUOhKph9n7dE"

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()

async def main() -> None:
    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)

@dp.message(CommandStart())
async def command_start(message: types.Message) -> None:
    await message.answer(f"Hello, {message.from_user.username}")

@dp.message()
async def send_wiki(message: types.Message):
    try:
        response = wikipedia.summary(message.text)
        await message.answer(response)
    except Exception as e:
        await message.answer("Bu mavzuga oid maqola topilmadi!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
