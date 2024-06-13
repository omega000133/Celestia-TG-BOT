from telegram.ext import CommandHandler
from telegram_bot.commands.disk_management import diskalert_os, diskalert_py
from telegram_bot.commands.node_management import node_command
from telegram_bot.commands.missing_blocks import get_validator_address
from telegram_bot.commands.get_apr import get_apr
from telegram_bot.commands.help import help

from telegram_bot.commands.alerts import start_alerts, stop_alerts


def setup_handlers(application):
    application.add_handler(CommandHandler("diskalert_os", diskalert_os))
    application.add_handler(CommandHandler("diskalert_py", diskalert_py))
    application.add_handler(CommandHandler("node", node_command))
    application.add_handler(CommandHandler(["help", "start"], help))
    application.add_handler(CommandHandler("get_apr", get_apr))
    application.add_handler(
        CommandHandler("get_validator_address", get_validator_address)
    )
    application.add_handler(CommandHandler("start_alerts", start_alerts))
    application.add_handler(CommandHandler("stop_alerts", stop_alerts))
    # application.add_handler(CommandHandler("done", done))
