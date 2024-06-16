from telegram import Update
from telegram.ext import CallbackContext
from telegram_bot.config.settings import BASE_URL_API, VALOPER_ADDRESS
from telegram_bot.utils.message import send_message_to_telegram
from telegram_bot.utils.httpxapi import cosmos_api_get

import random


async def node_command(update: Update, context: CallbackContext):
    args = context.args
    if not args:
        await send_message_to_telegram(
            update,
            context,
            "Por favor, proporciona un argumento válido después de /node.",
        )

        return

    if args[0].lower() == "reward":
        node_reward(update, context)

    all_args = " ".join(context.args).lower()
    if "manco" in all_args:
        # Lista de posibles respuestas
        respuestas = ["tu", "sebas", "clyde", "juanpi"]
        # Seleccionar una respuesta aleatoria de la lista
        respuesta_aleatoria = random.choice(respuestas)
        # Enviar la respuesta aleatoria como mensaje
        await send_message_to_telegram(update, context, respuesta_aleatoria)

    if args[0].lower() == "wallet":
        node_wallet(update, context, billetera=args[1].lower())


async def node_reward(update: Update, context: CallbackContext):
    validator_address = VALOPER_ADDRESS
    endpoint = f"/cosmos/distribution/v1beta1/validators/{validator_address}/commission"
    full_url = BASE_URL_API + endpoint

    try:
        data = cosmos_api_get(full_url)
        if data is not None:

            commission_data = data.get("commission", {}).get("commission", [])

            if commission_data:  # Verifica si la lista no está vacía
                # Convertir el valor de 'amount' a float
                raw_amount = commission_data[0].get("amount", "0")
                amount = (
                    float(raw_amount) / 1_000_000
                )  # Convierte de utia a TIA considerando 6 dígitos decimales
                amount = "{:.6f}".format(amount)
                await send_message_to_telegram(
                    update, context, f"Comisiones por reclamar: {amount} TIA"
                )
            else:
                await send_message_to_telegram(update, context, "No existen comisiones")
        else:
            await send_message_to_telegram(update, context, "No existen comisiones")

    except Exception as e:
        await send_message_to_telegram(
            update, context, f"Error al obtener las comisiones: {e}"
        )


async def node_wallet(update: Update, context: CallbackContext, billetera, token=None):
    endpoint_libre = f"/cosmos/bank/v1beta1/balances/{billetera}"
    endpoint_staking = f"/cosmos/staking/v1beta1/delegations/{billetera}"
    endpoint_unstaking = (
        f"/cosmos/staking/v1beta1/delegators/{billetera}/unbonding_delegations"
    )
    full_url_libre = BASE_URL_API + endpoint_libre
    full_url_staking = BASE_URL_API + endpoint_staking
    full_url_unstaking = BASE_URL_API + endpoint_unstaking

    if token is None:
        token = "utia"

    ####### libre ####
    try:
        print("entro en libre")
        data = cosmos_api_get(full_url_libre)
        amount_data = data.get("balances", {})
        print(amount_data)

        for _amount_data in amount_data:
            if _amount_data["denom"] == f"{token}":
                dinerotia = _amount_data["amount"]
                break
            else:
                await send_message_to_telegram(
                    update, context, f"verifica si el token existe"
                )

        if dinerotia:  # Verifica si la lista no está vacía
            # Convertir el valor de 'amount' a float
            # raw_amount = amount_data[0].get('amount', '0')
            amount = (
                float(dinerotia) / 1_000_000
            )  # Convierte de utia a TIA considerando 6 dígitos decimales
            amount_libre = "{:.6f}".format(amount)
            # await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Tienes {amount_libre} Tias en tu wallet {billetera}")
        else:
            await send_message_to_telegram(
                update, context, "No existe valores o revisar manualmente"
            )

    except Exception as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Error al obtener el valor de tu billetera monto libre: {e}",
        )

    ###### staking ####
    try:
        print("entro en staking")
        data = cosmos_api_get(full_url_staking)

        delegation_responses = data.get("delegation_responses", [])
        print(delegation_responses)

        if not delegation_responses:
            # await context.bot.send_message(chat_id=update.effective_chat.id, text='No tienes fondos en staking.')
            amount_staking = 0

        # Asumimos que solo nos interesa el 'balance' del primer 'delegation response'.
        balance_data = delegation_responses[0].get("balance", {})
        if balance_data.get("denom") == token:
            dinerotia = balance_data.get("amount", "0")
        else:
            await send_message_to_telegram(
                update, context, "El token especificado no existe en tu staking."
            )

        if dinerotia != "0":  # Verifica si se encontró un valor.
            amount_staking = (
                float(dinerotia) / 1_000_000
            )  # Convierte de utia a TIA considerando 6 dígitos decimales.
            amount_staking = "{:.6f}".format(amount_staking)
            # await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Tienes {amount_staking_formatted} TIA en staking en tu wallet {billetera}.")
        else:
            await send_message_to_telegram(
                update, context, "No existen valores en staking o revisar manualmente."
            )

    except Exception as e:
        await send_message_to_telegram(
            update, context, f"Error al obtener el valor de staking: {e}"
        )

    ###### unstaking ####
    try:
        print("Entro en unstake")
        data = cosmos_api_get(full_url_unstaking)

        unbonding_responses = data.get("unbonding_responses", [])
        print(unbonding_responses)

        # Inicializa amount_unstaking por defecto
        amount_unstaking = "0.000000"

        if unbonding_responses:
            # Solo procede si hay datos en unbonding_responses
            entries = unbonding_responses[0].get("entries", [])
            if not entries:
                print("No hay entradas en unstaking, revisar manualmente.")
            else:
                # Procede con la logica para el primer 'entry' si hay entradas
                balance = entries[0].get("balance", "0.000000")
                amount_unstaking = (
                    float(balance) / 1_000_000
                )  # Convierte de utia a TIA considerando 6 dígitos decimales
                amount_unstaking = "{:.6f}".format(amount_unstaking)
                print(amount_unstaking)
    except Exception as e:
        await send_message_to_telegram(
            update, context, f"Error al obtener el valor de unstaking: {e}"
        )

    ####### final #####

    print(f"{amount_libre}")
    print(f"{type(amount_libre)}")
    print(f"{amount_staking}")
    print(f"{type(amount_staking)}")
    print(f"{amount_unstaking}")
    print(f"{type(amount_unstaking)}")

    montos = [
        ("libre:", float(amount_libre)),
        ("staking:", float(amount_staking)),
        ("unstaking:", float(amount_unstaking)),
        (
            "En total:",
            float(amount_libre) + float(amount_staking) + float(amount_unstaking),
        ),
    ]

    # Construir el mensaje con Markdown
    mensaje_final = "```\n"  # Uso de texto preformateado para conservar espacios
    for descripcion, valor in montos:
        mensaje_final += f"{descripcion:<10} {valor:,.2f} TIA\n"
    mensaje_final += "```"

    await send_message_to_telegram(update, context, mensaje_final)
