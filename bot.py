import discord
from discord.ext import commands
import random
import asyncio
import datetime
import os

client = commands.Bot(command_prefix="::",intents = discord.Intents.all(), case_insensitive = True, help_command=None)
TOKEN = os.environ["TOKEN"]

exception_color = 0x90D9CD
utility_color = 0xD97B88
function_color = 0xE7E874

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Your IP Address"))

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Reloaded {extension}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
