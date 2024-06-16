from telegram_bot.config.settings import BASE_RPC_URL

stop_threads = True
threads = []
block_numbers = {}

node_list = {
    "basic_node": BASE_RPC_URL,
    "numia": "https://public-celestia-rpc.numia.xyz",
    "mesa": "https://celestia-rpc.mesa.newmetric.xyz",
    "luna": "https://rpc.lunaroasis.net",
    "nodestake": "https://rpc.celestia.nodestake.top",
    "brightlystake": "https://celestia-rpc.brightlystake.com",
    "pops": "http://rpc.celestia.pops.one",
}
