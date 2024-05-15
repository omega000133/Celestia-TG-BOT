from telegram import Update
from telegram.ext import CallbackContext

def help(update: Update, context: CallbackContext):
    comandos = [
        ("/help", "Muestra este mensaje de ayuda."),
        ("/node reward", "Consulta Comisiones pendientes del Nodo."),
        ("/node wallet <celes1wallet>", "Consulta el balance total de una wallet."),
        ("/node manco?", "Te dira quien es el mas manco"),
        ("/diskalert_os", "Uso del disco usando built-in commands"),
        ("/diskalert_py", "Uso del disco usando built-in python package"),
        ("/get_apr", "Obtiene el APR de Celestia en tiempo real"),
        ("/get_validator_address", "Obtiene el hex validator address"),
        # Agrega más comandos según sea necesario
    ]

    # Construir el mensaje de ayuda
    lineas_ayuda = [f"{comando}: {descripcion}" for comando, descripcion in comandos]
    mensaje_ayuda = "```"
    mensaje_ayuda += "Comandos_disponibles:\n" + "\n".join(lineas_ayuda)
    mensaje_ayuda += "```"

    update.message.reply_text(mensaje_ayuda, parse_mode='MarkdownV2')