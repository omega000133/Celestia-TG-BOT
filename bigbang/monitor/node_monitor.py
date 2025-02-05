import time
import threading
import asyncio
from telegram import Update
from telegram.ext import CallbackContext
from telegram_bot.utils.message import send_message_to_telegram, get_node_info_message
from telegram_bot.config.settings import MISSED_BLOCK_NUMBER

from bigbang.utils.api import get
from bigbang.utils import constant
from dotenv import find_dotenv, load_dotenv, get_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)


def get_block_number(url):
    try:
        response = get(f"{url}/status")
        if response is not None:
            return int(response["result"]["sync_info"]["latest_block_height"])
        else:
            return None
    except Exception as e:
        print(e)
        return None


def monitor_node(name, url, block_numbers, update: Update, context: CallbackContext):
    while not constant.stop_threads:
        block_number = get_block_number(url)

        if block_number is not None:
            block_numbers[name] = block_number
        else:
            if name == "basic_node":
                send_message_to_telegram(update, context, f"latam node is turning off")
        time.sleep(10)


async def compare_blocks(block_numbers, update: Update, context: CallbackContext):
    while not constant.stop_threads:
        latam_block = block_numbers.get("basic_node")
        if latam_block is None:
            continue

        time.sleep(10)
        diff_block = max(block_numbers.values(), default=0) - latam_block
        print(block_numbers)
        if diff_block > int(get_key(dotenv_file, "MISSED_BLOCK_NUMBER")):
            # asyncio.get_running_loop()
            await send_message_to_telegram(
                update, context, f"Just found {diff_block} blocks"
            )


def run_monitoring(update: Update, context: CallbackContext):
    # allow to run async in event loop
    asyncio.get_running_loop()
    if not constant.stop_threads:
        print("/monitor alert start")
        asyncio.ensure_future(
            get_node_info_message(update, context, "monitering is already started")
        )
        return

    constant.stop_threads = False
    for node_name, node_url in constant.node_list.items():
        thread = threading.Thread(
            target=monitor_node, args=(node_name, node_url, constant.block_numbers, update, context)
        )
        constant.threads.append(thread)
        thread.start()

    comparison_thread = threading.Thread(
        target=asyncio.run,
        args=(compare_blocks(constant.block_numbers, update, context),),
    )
    comparison_thread.start()

    asyncio.ensure_future(get_node_info_message(update, context, "started montering"))


def stop_monitoring(update: Update, context: CallbackContext):
    print("stop montiring")
    asyncio.get_running_loop()

    constant.stop_threads = True
    for thread in constant.threads:
        thread.join()

    constant.threads.clear()
    asyncio.ensure_future(
        send_message_to_telegram(update, context, "Stopped all monitoring threads")
    )
    return
