import logging
import asyncio
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configurar el registro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Definir una función asincrónica para el comando /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hola! Soy un bot de ejemplo de Telegram.')

# Definir una función principal asincrónica
async def main() -> None:
    # Crear una instancia del Updater con tu token
    updater = Updater("6420807698:AAF5KaKictwLAPBz3Np3hB6CLqcAZ1V9B50", use_context=True)

    # Obtener el despachador para registrar controladores
    dispatcher = updater.dispatcher

    # Registrar el controlador para el comando /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Iniciar el bot de forma asincrónica
    updater.start_polling()
    # Crear un bucle de eventos para manejar las actualizaciones de forma asincrónica
    loop = asyncio.get_event_loop()
    await loop.create_task(updater.idle())

if __name__ == '__main__':
    asyncio.run(main())