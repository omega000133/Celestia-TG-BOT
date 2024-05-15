def welcome_message():
    # Define los códigos de colores ANSI
    cyan = '\033[96m'
    yellow = '\033[93m'
    red = '\033[91m'  # Color rojo para el corazón
    end_color = '\033[0m'

    # Arte ASCII y mensaje con colores y corazón ASCII
    art =f"""
    LatamNodes BOT v0.01 {red}♥{end_color} made with {red}♥{end_color} from Latin America\n
    Would you buy me a coffee? Just kidding... unless? 😉
    """

    # Retorna el arte y el mensaje
    return art