import discord
from discord.ext import commands
import datetime

exception_color = 0x90D9CD
utility_color = 0xD97B88
function_color = 0xE7E874

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, msg):

        if self.client.user in msg.mentions:
            embed = discord.Embed(description = "My prefix for this guild is `::`", color = 0xFFC5A8)
            embed.set_footer(text = "Type ::help to know about my commands.")
            await msg.channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed = discord.Embed(description = "Are you sure that command exists?", color = exception_color))
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = discord.Embed(description = "You seem to be missing some arguments", color = exception_color))

def setup(client):
    client.add_cog(Events(client))