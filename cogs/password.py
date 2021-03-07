import discord
from discord.ext import commands
import datetime
import random
import string

exception_color = 0x90D9CD
utility_color = 0xD97B88
function_color = 0xE7E874

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  '*', '(', ')']

class Password(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["passw","strongpass"])
    async def password(self, ctx, *, passw,length = 8):

        cap_pass = ''.join(random.choice((str.upper, str.lower))(c) for c in passw)
        var1 = ''.join('%s%s' % (x, random.choice((random.choice(SYMBOLS), ""))) for x in cap_pass)
        try:
            var1 = var1.replace(" ","")
        except:
            pass
        while len(var1)<=length:
            var1 += random.choice(SYMBOLS)

        embed = discord.Embed(description = "Generated new password for you!", color = function_color, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Old Password", value = f"```{passw}```", inline = False)
        embed.add_field(name = "New Password", value = f"```{var1}```", inline = False)
        embed.add_field(name = "Length", value = f"```{len(var1)}```")
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @commands.command()
    async def randompass(self, ctx, number: int = 6):

        if number > 100:
            await ctx.send(embed = discord.Embed(description = "Isn't that digit too long?", color = exception_color))

        if number < 6:
            await ctx.send(embed = discord.Embed(description = "Isn't that digit too short?", color = exception_color))

        def password(stringLength):
            password_character = string.ascii_letters + string.digits + string.punctuation
            return "".join(random.choice(password_character) for i in range(stringLength))

        embed = discord.Embed(color = function_color, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "Random Password", value = f"```{password(number)}```")
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Password(client))