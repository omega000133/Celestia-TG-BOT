import requests
import base64
import hashlib
import bech32
from config.settings import BASE_URL_API, VALOPER_ADDRESS
from telegram import Update
from telegram.ext import CallbackContext

def bech32_to_hex(address: str) -> str:
    """
    Decodifica una dirección Bech32 y la convierte a hexadecimal.
    """
    _, data = bech32.decode(address)
    converted_data = bech32.convertbits(data, 5, 8, False)
    hex_address = ''.join(format(x, '02x') for x in converted_data)
    return hex_address.upper()

def get_validator_info(api_url: str, valoper_address: str) -> dict:
    """
    Obtiene información sobre un validador utilizando la API REST de Cosmos SDK.
    """
    endpoint = f"/cosmos/staking/v1beta1/validators/{valoper_address}"
    try:
        response = requests.get(api_url + endpoint)
        response.raise_for_status()
        return response.json()  # Retorna la respuesta como un diccionario de Python
    except requests.RequestException as e:
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

def process_validator_info(validator_info: dict) -> str:
    """
    Procesa la información del validador, extrayendo y convirtiendo la clave pública de consenso.
    """
    if 'validator' in validator_info:
        consensus_pubkey = validator_info['validator']['consensus_pubkey']['key']
        validator_address_hex = pubkey_to_validator_address(consensus_pubkey)
        return f"Validator Address (Hex): {validator_address_hex}"
    else:
        return f"No se pudo encontrar la información del validador."
    
def get_validator_address(update: Update, context: CallbackContext):
    validator_info = get_validator_info(BASE_URL_API, VALOPER_ADDRESS)
    print(validator_info)
    update.message.reply_text(process_validator_info(validator_info))

if __name__ == '__main__':
    
    # Obtener información del validador
    validator_info = get_validator_info(BASE_URL_API, VALOPER_ADDRESS)
    
    # Procesar la información del validador para extraer y convertir la clave pública de consenso
    print(validator_info)
    print(process_validator_info(validator_info))