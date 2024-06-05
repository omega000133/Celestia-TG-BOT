from telegram import Update
from telegram.ext import CallbackContext
from config.settings import BASE_URL_API, DEBUG
from utils.httpxapi import cosmos_api_get, cosmos_api_post, run_concurrently
from utils.decorators import timer

# def obtener_annual_provisions():
#     """Obtener las provisiones anuales de la red."""
#     url = f"{BASE_URL_API}/cosmos/mint/v1beta1/annual_provisions"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         annual_provisions = float(data["annual_provisions"])
#         return annual_provisions
#     else:
#         print("Error al obtener las provisiones anuales.")
#         return None


async def obtener_annual_provisions():
    """Obtener las provisiones anuales de la red de forma asíncrona."""
    try:
        url = f"{BASE_URL_API}/cosmos/mint/v1beta1/annual_provisions"
        data = await cosmos_api_get(url)  # Utiliza await aquí
        if data is not None:
            annual_provisions = float(data["annual_provisions"])
            return annual_provisions
        else:
            print("Error al obtener las provisiones anuales.")
            return None
    except Exception as e:
        print(f"Error inesperado al obtener las provisiones anuales: {e}")
        return None


async def obtener_bonded_tokens():
    """Obtener el total de tokens en staking."""
    try:
        url = f"{BASE_URL_API}/cosmos/staking/v1beta1/pool"
        data = await cosmos_api_get(url)
        if data is not None:
            bonded_tokens = float(data["pool"]["bonded_tokens"])
            return bonded_tokens
        else:
            print("Error al obtener el total de tokens en staking.")
            return None
    except Exception as e:
        print(f"Error inesperado al obtener el total de tokens en staking: {e}")
        return None


async def obtener_community_tax():
    """Obtiene el valor del community tax"""
    try:
        url = f"{BASE_URL_API}/cosmos/distribution/v1beta1/params"
        data = await cosmos_api_get(url)
        if data is not None:
            community_tax = float(data["params"]["community_tax"])
            return community_tax
        else:
            print("Error al obtener la tasa de impuesto comunitario.")
            return None
    except Exception as e:
        print(f"Error inesperado al obtener la tasa de impuesto comunitario: {e}")
        return None


def calcular_nominal_apr(annual_provisions, bonded_tokens, community_tax):
    """Calcular el APR nominal basado en las provisiones anuales, tokens en staking y el impuesto comunitario."""
    nominal_apr = annual_provisions * (1 - community_tax) / bonded_tokens * 100
    return nominal_apr


@timer
async def get_apr(update: Update, context: CallbackContext):
    try:

        annual_provisions, bonded_tokens, community_tax = run_concurrently(
            obtener_annual_provisions(),
            obtener_bonded_tokens(),
            obtener_community_tax(),
        )

        if (
            annual_provisions is not None
            and bonded_tokens is not None
            and community_tax is not None
        ):
            nominal_apr = calcular_nominal_apr(
                annual_provisions, bonded_tokens, community_tax
            )
            print(f"Nominal APR: {nominal_apr:.2f}%")
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Nominal APR: {nominal_apr:.2f}%",
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="No se pudo calcular el APR debido a un error al obtener los datos.",
            )
    except Exception as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=f"Error al obtener el APR: {e}"
        )
