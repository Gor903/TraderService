import asyncio
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import sys, os
from dotenv import load_dotenv


load_dotenv()
USER_ID = os.getenv("USER_ID")
TEXT = sys.argv[1:] if len(sys.argv) > 1 else exit()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    async with Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    ) as bot:
        await bot.send_message(chat_id=USER_ID, text=" ".join(TEXT))


asyncio.run(main())
