import discord
from discord.ext import commands


# Configuración de intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Prefijo de comandos
bot = commands.Bot(command_prefix="$", intents=intents)

# Evento cuando el bot se conecta
@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")


@bot.command()
async def saludar(ctx):
    await ctx.send("Hola")


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

bot.run("")
