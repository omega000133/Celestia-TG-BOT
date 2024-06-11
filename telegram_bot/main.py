from telegram.ext import ApplicationBuilder
from telegram_bot.bot.handlers import setup_handlers
from telegram_bot.config.settings import TOKEN


def run_bot():
    application = ApplicationBuilder().token(TOKEN).concurrent_updates(True).build()
    setup_handlers(application)

    application.run_polling()
