import base64
import hashlib
import bech32
from config.settings import BASE_URL_API, VALOPER_ADDRESS
from telegram import Update
from telegram.ext import CallbackContext

from telegram_bot.utils.httpxapi import cosmos_api_get
from telegram_bot.utils.message import send_message_to_telegram


def bech32_to_hex(address: str) -> str:
    """
    Decodifica una dirección Bech32 y la convierte a hexadecimal.
    """
    _, data = bech32.decode(address)
    converted_data = bech32.convertbits(data, 5, 8, False)
    hex_address = "".join(format(x, "02x") for x in converted_data)
    return hex_address.upper()


async def get_validator_info(api_url: str, valoper_address: str) -> dict:
    """
    Obtiene información sobre un validador utilizando la API REST de Cosmos SDK.
    """
    try:
        url = f"{api_url}/cosmos/staking/v1beta1/validators/{valoper_address}"

        data = await cosmos_api_get(url)
        if data is not None:
            return data
        else:
            return None
    except Exception as e:
        print(f"Error al obtener información del validador: {e}")
        return {}


def pubkey_to_validator_address(pubkey_base64: str) -> str:
    """
    Convierte una clave publica de consenso en formato base64 a una direccion de validador en formato hexadecimal.
    """
    pubkey_bytes = base64.b64decode(pubkey_base64)
    hash_sha256 = hashlib.sha256(pubkey_bytes).digest()
    address_bytes = hash_sha256[:20]
    return address_bytes.hex().upper()


def pubkey_to_consensus_address(pubkey_base64: str) -> str:
    """
    get consensus address from publickey
    """
    prefix = "celestiavalcons"
    pubkey_bytes = base64.b64decode(pubkey_base64)
    sha256_hash = hashlib.sha256(pubkey_bytes).digest()
    address_bytes = sha256_hash[:20]

    consensus_address = bech32.bech32_encode(
        prefix, bech32.convertbits(address_bytes, 8, 5)
    )

    return consensus_address


async def get_missed_block(api_url: str, consensus_address: str) -> str:
    """
    Get missed block using consensus address
    """
    try:
        url = f"{api_url}/cosmos/slashing/v1beta1/signing_infos/{consensus_address}"
        data = await cosmos_api_get(url)
        if data is not None:
            return data["val_signing_info"]["missed_blocks_counter"]
        else:
            return None
    except Exception as e:
        return "validator signing infomation couldn't be found"


async def process_validator_info(validator_info: dict) -> str:
    """
    Procesa la información del validador, extrayendo y convirtiendo la clave pública de consenso.
    """
    if "validator" in validator_info:
        consensus_pubkey = validator_info["validator"]["consensus_pubkey"]["key"]
        validator_address_hex = pubkey_to_validator_address(consensus_pubkey)
        consensus_address = pubkey_to_consensus_address(consensus_pubkey)
        missed_block = await get_missed_block(BASE_URL_API, consensus_address)
        return f"Validator Address (Hex): {validator_address_hex}\nMissed Block count: {missed_block}"
    else:
        return f"No se pudo encontrar la información del validador."


async def get_validator_address(update: Update, context: CallbackContext):
    validator_info = await get_validator_info(BASE_URL_API, VALOPER_ADDRESS)
    print(validator_info)
    message = await process_validator_info(validator_info)
    await send_message_to_telegram(update, context, message)


if __name__ == "__main__":

    # Obtener información del validador
    validator_info = get_validator_info(BASE_URL_API, VALOPER_ADDRESS)

    # Procesar la información del validador para extraer y convertir la clave pública de consenso
    print(validator_info)
    print(process_validator_info(validator_info))
