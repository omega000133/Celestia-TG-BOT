import httpx
import os
import inspect
import asyncio
import time
from functools import wraps

async def cosmos_api_get(url):
    """Funcion generica cosmos_api_get para obtener datos de una URL de API usando la librería httpx de Python utilizando async 
    de forma concurrente y con manejo de errores."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, follow_redirects=True, timeout=5)
            if response.status_code == 200:
                return response.json()
            else:
                caller_name, file_name, line_no = obtener_info_llamante()
                print(f"error {response.status_code}: {response.reason_phrase} llamado desde {caller_name}, archivo {file_name}, línea {line_no}")
                return None
    except Exception as e:
        print(f"Error al obtener los datos de la API: {e} llamado desde {caller_name}, archivo {file_name}, línea {line_no}")
        return None


async def cosmos_api_post(url, data):
    """Funcion generica cosmos_api_post para obtener datos de una URL de API usando la librería httpx de Python de forma async
      y con manejo de errores de forma concurrente."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, follow_redirects=True, timeout=5)
            if response.status_code == 200:
                return response.json()
            else:
                return None
    except Exception as e:
        print(f"Error al obtener los datos de la API: {e}")
        return None

def obtener_info_llamante():
    """Obtiene información sobre la función llamante, excluyendo llamadas desde un archivo específico."""
    # Obtener la ruta del archivo actual para excluirlo
    archivo_actual = inspect.getfile(obtener_info_llamante)
    archivo_actual = os.path.abspath(archivo_actual)  # Normaliza la ruta para comparación precisa

    caller_frame = inspect.currentframe().f_back  # Comienza con el marco anterior

    while caller_frame:
        frame_file = caller_frame.f_code.co_filename
        frame_file = os.path.abspath(frame_file)  # Normaliza la ruta

        if frame_file != archivo_actual:
            caller_name = caller_frame.f_code.co_name
            line_no = caller_frame.f_lineno
            return caller_name, frame_file, line_no

        caller_frame = caller_frame.f_back

    # Si se llega al final de la pila sin encontrar un marco externo, devolver valores predeterminados
    return "Desconocido", "Desconocido", 0

async def execute_asynchronously(*tasks):
    return await asyncio.gather(*tasks)

def run_concurrently(*tasks):
    return asyncio.run(execute_asynchronously(*tasks))


