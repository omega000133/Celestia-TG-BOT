from telegram import Update
from telegram.ext import CallbackContext
from telegram_bot.utils.message import send_message_to_telegram


async def start_alerts(update: Update, context: CallbackContext):
    try:
        await send_message_to_telegram(update, context, "start alert")
    except Exception as e:
        await send_message_to_telegram(update, context, f"{e}")
