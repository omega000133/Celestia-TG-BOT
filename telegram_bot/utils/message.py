from telegram import Update
from telegram.ext import CallbackContext
from bigbang.utils.constant import node_list
from telegram_bot.config.settings import (
    MISSED_BLOCK_NUMBER,
    VALOPER_ADDRESS,
    BASE_RPC_URL,
)

from dotenv import find_dotenv, load_dotenv, get_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)


async def send_message_to_telegram(
    update: Update, context: CallbackContext, message: str
):
    try:
        if get_key(dotenv_file, "CHAT_ID") == update.effective_chat.id:
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text=message
            )
        else:
            await context.bot.send_message(
                chat_id=get_key(dotenv_file, "CHAT_ID"), text=message
            )

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{e}")


async def get_node_info_message(update: Update, context: CallbackContext, message):
    node_list_str = ""
    for node_info in node_list.values():
        if node_info != BASE_RPC_URL:
            node_list_str += f"\t{node_info}\n"
    node_info = [
        ("Bot", f"{message}... \n"),
        ("Config", f" {MISSED_BLOCK_NUMBER} missed blocks, telegram notification\n"),
        ("Rpc nodes", "\n" + node_list_str),
        ("Validator address", VALOPER_ADDRESS + ""),
    ]
    node_info_message_list = [
        f"{command}: {description}" for command, description in node_info
    ]
    await send_message_to_telegram(update, context, "".join(node_info_message_list))
