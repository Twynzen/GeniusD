"""
Este módulo contiene la definición de la clase Bot que maneja eventos y comandos.
"""
import discord
from discord.ext import commands
from bot.commands.base import BaseCommand


class Bot(commands.Bot):
    """
    Bot personalizado que maneja eventos y comandos.
    """

    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
        self.add_cog(BaseCommand(self))

    async def on_ready(self):
        """
        Evento que se dispara cuando el bot está listo.
        """
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):
        """
        Evento que se dispara cuando el bot recibe un mensaje.
        """
        print(f'Received message: {message.content}')

        # No procesar los mensajes enviados por el bot
        if message.author == self.user:
            return

        # Si el mensaje contiene el nombre del bot
        if self.user.mentioned_in(message):
            ctx = await self.get_context(message)

            # Si el mensaje no es un comando
            if not ctx.valid:
                # Aquí va tu código para procesar el mensaje y hacer la petición a la API
                pass

        await self.process_commands(message)
