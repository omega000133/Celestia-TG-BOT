from telegram import Update
from telegram.ext import CallbackContext

from bigbang.monitor.node_monitor import run_monitoring, stop_monitoring
from telegram_bot.utils.message import get_node_info_message, send_message_to_telegram
from dotenv import find_dotenv, load_dotenv, set_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)


async def monitor_command(update: Update, context: CallbackContext):
    args = context.args

    if not args or (args and args[0].lower() == "help"):
        commands = [
            ("/monitor alert start", "start monitoring"),
            ("/monitor alert stop", "stop  monitoring"),
            ("/monitor status", "get monitoring info"),
            ("/monitor set chat_id xxxxxxxxx", "get group id for the chat"),
            ("/monitor set missed_block_number 5", "get group id for the chat"),
        ]

        sub_message_list = [
            f"{command}: {description}" for command, description in commands
        ]
        message = ""
        message += "Please provide a valid argument after /monitor. \n"
        message += "Here is available command: \n".join(sub_message_list)
        message += ""

        await send_message_to_telegram(update, context, message)
        return

    if args[0].lower() == "alert":
        if args[1].lower() == "start":
            await start_alerts(update, context)
            return

        elif args[1].lower() == "stop":
            await stop_alerts(update, context)
            return
        else:
            return

    if args[0].lower() == "status":
        await get_node_info_message(update, context, "Currenlty node info: \n")
        return

    if args[0].lower() == "set" and len(args) > 2:
        if args[1].lower() == "chat_id":
            set_key(dotenv_file, "CHAT_ID", args[2])
            return
        if args[1].lower() == "missed_block_number":
            set_key(dotenv_file, "MISSED_BLOCK_NUMBER", args[2])
            return


async def start_alerts(update: Update, context: CallbackContext):
    try:
        # await send_message_to_telegram(update, context, "Starting monitoring...")
        run_monitoring(update, context)

    except Exception as e:
        await send_message_to_telegram(update, context, f"{e}")


async def stop_alerts(update: Update, context: CallbackContext):
    try:
        await send_message_to_telegram(update, context, "Stopping monitoring...")
        stop_monitoring(update, context)
    except Exception as e:
        await send_message_to_telegram(update, context, f"{e}")
