from telegram_bot.config.settings import DEBUG
from telegram_bot.utils.welcome_message import welcome_message
from telegram_bot.main import run_bot
import logging

if DEBUG is True:
    # Configurar el registro
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )
#     logger = logging.getLogger(__name__)

if __name__ == "__main__":
    print(welcome_message())
    run_bot()
