from telegram.ext import CommandHandler
from commands.disk_management import diskalert_os, diskalert_py
from commands.node_management import node_command
from commands.missing_blocks import get_validator_address
from commands.get_apr import get_apr 
from commands.help import help
#from commands.alerts import start_alerts, done

def setup_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("diskalert_os", diskalert_os))
    dispatcher.add_handler(CommandHandler("diskalert_py", diskalert_py))
    dispatcher.add_handler(CommandHandler("node", node_command, pass_args=True))
    dispatcher.add_handler(CommandHandler(["help","start"], help))
    dispatcher.add_handler(CommandHandler("get_apr", get_apr))
    dispatcher.add_handler(CommandHandler("get_validator_address", get_validator_address))
    #dispatcher.add_handler(CommandHandler("start_alerts", start_alerts))
    #dispatcher.add_handler(CommandHandler("done", done))