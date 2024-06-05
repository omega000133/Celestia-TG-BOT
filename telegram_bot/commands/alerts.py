from telegram import Update
from telegram.ext import CallbackContext


async def start_alerts(update: Update, context: CallbackContext):
    try:
        print("start alerts")
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="start alert"
        )
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{e}")
