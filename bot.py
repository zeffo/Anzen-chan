import discord
from discord.ext import commands
import random
import asyncio
import datetime
import jishaku
import os

client = commands.Bot(command_prefix="::",intents = discord.Intents.all(), case_insensitive = True, help_command=None)

exception_color = 0x90D9CD
utility_color = 0xD97B88
function_color = 0xE7E874

@client.event
async def on_ready():
    print("Let's win this one")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Your IP Address"))
    client.load_extension('jishaku')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Reloaded {extension}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("ODEzMzUwODg2Njc1ODQxMDY1.YDOCCg.BquCMJJGXl_83SOftTWO0J99GuA")