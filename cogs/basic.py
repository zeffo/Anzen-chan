import discord
from discord.ext import commands
import datetime
from PIL import Image, ImageDraw, ImageFont
import random
import asyncio
import wonderwords
import os

exception_color = 0x90D9CD
utility_color = 0xD97B88
function_color = 0xE7E874

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, *, category = None):  

        if category == None:

            embed = discord.Embed(title = "Available Commands", color = 0x2F3136)
            
            embed.add_field(name = "password", value = "Generates a strong password from an easy one")
            embed.add_field(name = "randompass", value = "Generates a random password with n length for you")
            embed.add_field(name = "encode", value = "Encodes a piece of string")
            embed.add_field(name = "decode", value = "Decodes a piece of string")
            embed.add_field(name = "imgdec", value = "Decodes an image")
            embed.add_field(name = "imgenc", value = "Encodes an image")
            embed.add_field(name = "secretmsg", value = "Makes a secret message from a given message")
            embed.add_field(name = "save", value = "Saves a piece of string")
            embed.add_field(name = "getmsg", value = "Shows a saved message")
            embed.add_field(name = "typerace", value = "Starts a typerace")
            
            embed.add_field(name = "ping", value = "Shows the ping latency of the bot")
            embed.add_field(name = "info", value = "Shows info about me")
            embed.add_field(name = "help", value = "Shows this page")
            
            embed.set_thumbnail(url = self.client.user.avatar_url)
            embed.set_footer(text = "Type ::help [command] for more info on a command.")
            await ctx.send(embed = embed)

        elif category == "password":
            embed = discord.Embed(description = "Generates a strong password from an easy one", color = utility_color)
            embed.add_field(name = "Usage", value = "```::password hello world```")
            await ctx.send(embed = embed)
        elif category == "randompass":
            embed = discord.Embed(description = "Generates a random password with n length for you", color = utility_color)
            embed.add_field(name = "Usage", value = "```::randompass [9](optional)```")
            await ctx.send(embed = embed)
        elif category == "encode":
            embed = discord.Embed(description = "Encodes a piece of string", color = utility_color)
            embed.add_field(name = "Usage", value = "```::encode hello world```")
            await ctx.send(embed = embed)
        elif category == "decode":
            embed = discord.Embed(description = "Decodes a piece of string", color = utility_color)
            embed.add_field(name = "Usage", value = "```::decode aGVsbG8gd29ybGQ=```")
            await ctx.send(embed = embed)
        elif category == "imgenc":
            embed = discord.Embed(description = "Encodes an image", color = utility_color)
            embed.add_field(name = "Usage", value = "```::imgenc [attach an image with the message]```")
            embed.set_image(url = self.client.user.avatar_url)
            await ctx.send(embed = embed)
        elif category == "imgdec":
            embed = discord.Embed(description = "Decodes an image", color = utility_color)
            embed.add_field(name = "Usage", value = "```::imgdec [encoding of an image]```")
            await ctx.send(embed = embed)
        elif category == "secretmsg":
            embed = discord.Embed(description = "Makes a secret message from a given message", color = utility_color)
            embed.add_field(name = "Usage", value = "```::secretmsg [message id]```")
            await ctx.send(embed = embed)
        elif category == "save":
            embed = discord.Embed(description = "Saves a piece of string", color = utility_color)
            embed.add_field(name = "Usage", value = "```::save [akey](key) [this is a saved message](message)```")
            await ctx.send(embed = embed)
        elif category == "getmsg":
            embed = discord.Embed(description = "Shows a saved message", color = utility_color)
            embed.add_field(name = "Usage", value = "```::getmsg [akey](previousely saved key)```")
            await ctx.send(embed = embed)
        elif category == "typerace":
            embed = discord.Embed(description = "Starts a typerace", color = utility_color)
            embed.add_field(name = "Usage", value = "```::typerace```")
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = discord.Embed(description = "Are you sure that actually exists?",color=exception_color))


    @commands.command(aliases = ["information"])
    async def info(self, ctx):
        try:

            member_count = 0
            for guild in self.client.guilds:
                for member in guild.members:
                    member_count+=1 

            embed = discord.Embed(title = "Information", color = utility_color)
            embed.add_field(name = "Client Name", value = self.client.user)
            embed.add_field(name = "ID", value = self.client.user.id, inline = False)
            embed.add_field(name = "Created At", value = self.client.user.created_at.__format__('%x, %H:%M:%S %p'), inline = False)
            embed.add_field(name = "Devs", value = "Drift Asimov#3338 and Code Stacks#8704", inline = False)
            embed.add_field(name = "Ping Latency", value = f"**{round(self.client.latency * 1000)}** ms", inline = False)
            embed.add_field(name = "Guilds", value = len(self.client.guilds))
            embed.add_field(name = "Users", value = member_count)
            embed.set_footer(text = "Type ::help to know about my commands.")
            embed.set_thumbnail(url = self.client.user.avatar_url)
            await ctx.send(embed = embed)

        except Exception as e:
            await ctx.send(e)

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(description = f"<a:tick:813719562809638922> **|** Pong! I have a client ping of: **{round(self.client.latency * 1000)}ms**", color = discord.Color.green())
        embed.set_footer(text = "It's your turn now!")
        await ctx.send(embed = embed)
        
    @commands.command()
    async def typerace(self, ctx):
        try:
            sentence = wonderwords.RandomSentence().sentence()
            await ctx.send(sentence)

            image = Image.open('Typerace.jpg')
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('arial.ttf', 100)
            draw.text((50, 10), sentence, font=font, fill=(222, 222, 222))
            image.save("to_send.jpg")
            
            sent = await ctx.send(file = discord.File("to_send.jpg"))
            os.remove("to_send.jpg")

            def check(msg):
                return msg.content == sentence
            try:
                s = await self.client.wait_for('message', timeout=180.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send(embed = discord.Embed(description = "No one answered in time.", color = exception_color))
            else:
                time = str(sent.created_at - ctx.message.created_at)
                time_format = time[5:][:-5]
                complete = await ctx.send(embed = discord.Embed(description = f"{s.author.mention} Completed the typerace in {time_format} seconds.", color=function_color))
                    
        except Exception as e:
            await ctx.send(e)

def setup(client):
    client.add_cog(Basic(client))