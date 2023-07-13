"""
Este módulo contiene la definición de la clase BaseCommand que maneja el comando base.
"""
from discord.ext import commands
import openai
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')
openai.api_key = OPENAI_KEY

    
class BaseCommand(commands.Cog):
    """
    Comando base que se ejecuta cuando se envía "!base" en Discord.
    """
    @commands.command(name='base')
    async def base_command(self, ctx, *, query):
        """
        Método que se ejecuta cuando se llama al comando base.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Hello, how can I assist you today?"},
                    {"role": "user", "content": query}
                ]
            )
            response_text = response['choices'][0]['message']['content']
            await ctx.send(response_text)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            await ctx.send("Sorry, I encountered an unexpected error. Please try again later.")





