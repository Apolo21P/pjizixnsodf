from settings import settings
import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
@bot.command()
async def mem(ctx):
    with open('bot img/img1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def mem1(ctx):
    img=os.listdir("bot img")
    with open(f'bot img/{random.choice(img)}', 'rb') as f:
            picture = discord.File(f)
    
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
@bot.command()
async def res(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
@bot.command()
async def contaminacion(ctx):
    await ctx.send(f"""Hola, soy un bot {bot.user}!""")# esta linea saluda
    await ctx.send(f'te voy a hablar sobre la programación')
    await ctx.send(f'En el ámbito de la informática, la programación refiere a la acción de crear programas o aplicaciones a través del desarrollo de un código fuente, que se basa en el conjunto de instrucciones que sigue el ordenador para ejecutar un programa. La programación es lo que permite que un ordenador funcione y realice las tareas que el usuario solicita.')
    # Enviar una pregunta al usuario
    await ctx.send("te gustaria saber que es un lenguaje de programación? Responde con 'sí' o 'no'.")
# Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("1. Un lenguaje de programación es un lenguaje formal (o artificial, es decir, un lenguaje con reglas gramaticales bien definidas) que proporciona a una persona, en este caso el programador, la capacidad y habilidad de escribir (o programar) una serie de instrucciones o secuencias de órdenes en forma de algoritmos con el fin de controlar el comportamiento físico o lógico de un sistema informático")
            await ctx.send("2. Un lenguaje de programación, en palabras simples, es el conjunto de instrucciones a través del cual los humanos interactúan con las computadoras.")   
        else:
            await ctx.send("Está bien,en caso de tener alguna duda puede consultarlo aqui mismo")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

bot.run(settings["TOKEN"])

