from telegram.ext import CommandHandler
from commands.disk_management import diskalert_os, diskalert_py
from commands.node_management import node_command
from commands.missing_blocks import get_validator_address
from commands.get_apr import get_apr
from commands.help import help

# from commands.alerts import start_alerts, done


def setup_handlers(application):
    application.add_handler(CommandHandler("diskalert_os", diskalert_os))
    application.add_handler(CommandHandler("diskalert_py", diskalert_py))
    application.add_handler(CommandHandler("node", node_command))
    application.add_handler(CommandHandler(["help", "start"], help))
    application.add_handler(CommandHandler("get_apr", get_apr))
    application.add_handler(
        CommandHandler("get_validator_address", get_validator_address)
    )
    # application.add_handler(CommandHandler("start_alerts", start_alerts))
    # application.add_handler(CommandHandler("done", done))
