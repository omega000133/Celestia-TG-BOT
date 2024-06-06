import subprocess
import shutil
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
# sys.path['C:/Users/User/Desktop/PythonETHnodesrpc/LatamNodeBot/']
# sys.path[sys]

from telegram import Update
from telegram.ext import CallbackContext
from telegram_bot.config.settings import MIN_FREE_SPACE, PORCENTAJE
from telegram_bot.utils.decorators import timer
from telegram_bot.utils.subprocess_utils import run_command
from telegram_bot.utils.message import send_message_to_telegram


async def diskalert_os(update: Update, context: CallbackContext):
    # Lógica para el comando diskalert...
    # Ejecutar el comando para obtener el espacio libre en disco
    try:
        comando_df = ["df", "-BG", "/"]
        resultado_df = subprocess.run(
            comando_df, capture_output=True, text=True, check=True
        )

        # Paso 2: Procesar la salida de `df` para obtener la línea de interés (la última línea)
        linea_interes = resultado_df.stdout.strip().split("\n")[-1]

        # Paso 3: Extraer el cuarto campo (espacio libre) y quitar la 'G' al final
        espacio_libre_con_g = linea_interes.split()[3]
        espacio_libre = espacio_libre_con_g[:-1]  # Quita el último carácter, que es 'G'

        # Convertir a entero si necesario
        espacio_libre_gb = int(espacio_libre)
        print(f"Espacio libre en GB: {espacio_libre_gb}")
    except subprocess.CalledProcessError as e:
        await send_message_to_telegram(
            update, context, "Error al verificar el espacio en disco."
        )

    except Exception as e:
        await send_message_to_telegram(update, context, f"{e}")

    # Verificar si el espacio libre es menor que el mínimo requerido y enviar alerta
    if int(espacio_libre) < MIN_FREE_SPACE:
        await send_message_to_telegram(
            update,
            context,
            f"Alerta de espacio en disco bajo: Solo quedan {espacio_libre_gb} GB libres en el servidor.",
        )

    else:
        await send_message_to_telegram(
            update,
            context,
            f"Espacio en disco suficiente: {espacio_libre_gb} GB libres.",
        )


@timer
async def diskalert_py(
    update: Update = None,
    context: CallbackContext = None,
    path="/",
    porcentaje=PORCENTAJE,
):
    """
    Calcula el uso del disco para una ruta dada, devuelve el espacio libre en gigabytes y el porcentaje de espacio libre.
    Si el espacio libre es menor o igual al 10% del total, muestra una alerta.
    Se comporta de manera diferente si se ejecuta desde un bot de Telegram o como un script directo.

    Parámetros:
    - update: Update. Objeto de actualización del bot de Telegram. Por defecto es None.
    - context: CallbackContext. Contexto de callback del bot de Telegram. Por defecto es None.
    - path: str. La ruta del archivo para calcular el uso del disco. Por defecto es la raíz ("/").

    Devoluciones:
    - No retorna directamente si se llama desde un bot de Telegram, en su lugar, envía un mensaje a través del bot.
    - Retorna el espacio libre en GB y el porcentaje de espacio libre si se ejecuta como un script directo.
    """
    # Obtener el total, usado, y espacio libre en bytes
    total, used, free = shutil.disk_usage(path)

    # Convertir bytes a gigabytes
    total_gb = total / (2**30)
    free_gb = free / (2**30)
    free_percent = (free / total) * 100

    # Preparar el mensaje de salida
    alert_message = ""
    if porcentaje is True:
        if free_percent <= MIN_FREE_SPACE:
            alert_message = "¡Alerta! Espacio en disco bajo."
        else:
            alert_message = f"Espacio en disco suficiente: {free_gb:.2f} GB libres, {free_percent:.2f}% disponible."
    else:
        if free_gb <= MIN_FREE_SPACE:
            alert_message = "¡Alerta! Espacio en disco bajo."
        else:
            alert_message = f"Espacio en disco suficiente: {free_gb:.2f} GB libres"

    # Comprobar si se ejecuta desde un bot de Telegram o directamente
    if update is not None and context is not None:
        await send_message_to_telegram(update, context, alert_message)

    else:
        print(alert_message)
        return free_gb, free_percent


# Ejemplo de cómo llamar a la función directamente
if __name__ == "__main__":
    diskalert_py()

# # Obtener información del espacio de disco del directorio raíz
# total_gb, used_gb, free_gb = diskalert_py()

# print(f"Espacio total: {total_gb:.2f} GB")
# print(f"Espacio usado: {used_gb:.2f} GB")
# print(f"Espacio libre: {free_gb:.2f} GB")
