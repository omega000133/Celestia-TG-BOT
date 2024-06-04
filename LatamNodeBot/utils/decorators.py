import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        # Ejecuta la funcion original, que puede incluir asyncio.run()
        result = func(*args, **kwargs)

        duration = time.time() - start_time
        print(f"La ejecucion de {func.__name__} tomo {duration:.4f} segundos.")
        return result

    return wrapper
