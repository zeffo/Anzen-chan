import discord
from discord.ext import commands
import base64
import random
import datetime

exception_color = 0x90D9CD
utility_color = 0xD97B88
function_color = 0xE7E874

class Images(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def imgenc(self, ctx):
        if len(ctx.message.attachments) <= 0:
            await ctx.send(embed = discord.Embed(description = "Make sure your msg have an image attached with it.", color = exception_color))
            return
        url = ctx.message.attachments[0].url    
        ss = url.encode("ascii") 
        base64_bytes = base64.b64encode(ss) 
        base64_string = base64_bytes.decode("ascii") 
        await ctx.send(embed = discord.Embed(title = "Image Encoded", description = f"```{base64_string}```", color =  function_color))

    @commands.command()
    async def imgdec(self, ctx,*,string):
        try:
            base64_bytes = string.encode("ascii") 
            sample_string_bytes = base64.b64decode(base64_bytes) 
            sample_string = sample_string_bytes.decode("ascii") 
            embed = discord.Embed(color = 0xFFC5A8)
            embed.set_image(url = sample_string)
            embed.set_author(name = ctx.author.name,url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        except Exception as e:
            await ctx.send(embed = discord.Embed(description = "Couldn't Decode the Code, make sure that you didn't have a typo.", color = exception_color))

def setup(client):
    client.add_cog(Images(client))