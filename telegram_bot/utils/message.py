from telegram import Update
from telegram.ext import CallbackContext


async def send_message_to_telegram(
    update: Update, context: CallbackContext, message: str
):
    try:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{e}")
