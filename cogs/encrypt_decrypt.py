import discord
from discord.ext import commands
import base64
import random
import datetime
from googletrans import Translator

exception_color = 0x90D9CD
utility_color = 0xD97B88
function_color = 0xE7E874

class Encryption(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def encode(self, ctx, *, string):
        try:
            ss = string.encode("ascii") 
            base64_bytes = base64.b64encode(ss) 
            base64_string = base64_bytes.decode("ascii") 
            embed = discord.Embed(color = 0xFFC5A8)
            embed.add_field(name = "Encoded - ", value = f"```{base64_string}```")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        except Exception as e:
            await ctx.send(e)
            await ctx.send(embed = discord.Embed(description = "Couldn't Encode the given string.", color = exception_color))
    
    @commands.command()
    async def decode(self, ctx,*,string):
        try:
            base64_bytes = string.encode("ascii") 
            sample_string_bytes = base64.b64decode(base64_bytes) 
            sample_string = sample_string_bytes.decode("ascii")
            embed = discord.Embed(color = 0xFFC5A8)
            embed.add_field(name = "Decoded - ", value = f"```{sample_string}```")
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
            await ctx.send(embed= embed)
        except:
            await ctx.send(embed = discord.Embed(description = "Couldn't Decode the Code, make sure that you didn't have a typo.",color =0xFFC5A8))

    @commands.command()
    async def lang(self, ctx, *, arg):
        translator = Translator()
        trs = translator.translate(arg, dest="en")
        embed = discord.Embed(title = "Here is your translated text", description = trs.text, color = function_color)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Encryption(client))