import asyncio
import logging
import sys
import os
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import FSMI18nMiddleware
from dotenv import load_dotenv
from Bot.handler.main_handler import *

load_dotenv('.env')
TOKEN = os.getenv('BOT_TOKEN')


async def main() -> None:
    i18n = I18n(path="locales", default_locale="en", domain="messages")
    dp.update.middleware(FSMI18nMiddleware(i18n))
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
