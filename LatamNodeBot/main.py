# main.py
from bot.handlers import setup_handlers
from telegram.ext import Updater
from config.settings import TOKEN, DEBUG
from utils.welcome_message import welcome_message
import logging

if DEBUG is True:
    # Configurar el registro
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__name__)

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    setup_handlers(dispatcher)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    print(welcome_message())
    main()