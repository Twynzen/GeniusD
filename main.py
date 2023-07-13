# pylint: disable=import-error
"""
Este es el módulo principal de la aplicación. Aquí es donde se inicia el bot.
"""

from bot.bot import Bot
from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


def main():
    """
    Función principal que inicializa y ejecuta el bot.
    """
    
    bot = Bot()
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
