from telegram import Update
from telegram.ext import CallbackContext
from telegram_bot.utils.message import send_message_to_telegram
from bigbang.monitor.node_monitor import run_monitoring, stop_monitoring


async def monitor_command(update: Update, context: CallbackContext):
    args = context.args

    if not args or (args and args[0].lower() == "help"):
        commands = [
            ("/monitor alert start", "start monitoring"),
            ("/monitor alert stop", "stop  monitoring"),
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
