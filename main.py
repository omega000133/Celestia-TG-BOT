# main.py
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram_bot.bot.handlers import setup_handlers
from telegram_bot.config.settings import TOKEN, DEBUG
from telegram_bot.utils.welcome_message import welcome_message
import logging

if DEBUG is True:
    # Configurar el registro
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )
    logger = logging.getLogger(__name__)


def main():
    application = ApplicationBuilder().token(TOKEN).concurrent_updates(True).build()
    setup_handlers(application)

    application.run_polling()


if __name__ == "__main__":
    print(welcome_message())
    main()
