from telegram import Update
from telegram.ext import CallbackContext
from telegram_bot.utils.message import send_message_to_telegram
from bigbang.monitor.node_monitor import run_monitoring, stop_monitoring


async def start_alerts(update: Update, context: CallbackContext):
    try:
        await send_message_to_telegram(update, context, "Starting monitoring...")
        run_monitoring(update, context)

    except Exception as e:
        await send_message_to_telegram(update, context, f"{e}")


async def stop_alerts(update: Update, context: CallbackContext):
    try:
        await send_message_to_telegram(update, context, "Stopping monitoring...")
        stop_monitoring(update, context)
    except Exception as e:

        await send_message_to_telegram(update, context, f"{e}")
