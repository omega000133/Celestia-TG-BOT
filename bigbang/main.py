import asyncio
from telegram_bot.main import run_bot


def run():
    asyncio.create_task(run_bot())
