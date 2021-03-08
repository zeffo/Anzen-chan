import discord
from discord.ext import commands
import string
import datetime
import random
from msg_data import msg_data

exception_color = 0x90D9CD
utility_color = 0xD97B88
function_color = 0xE7E874

class Message(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def save(self, ctx, key, *, msg = "*empty*"):
        try:
            if len(ctx.message.attachments) > 0:
                msg_data[key] = [msg, ctx.author.name, ctx.message.attachments[0].url]
                embed = discord.Embed(title = "Message Saved :)",color = utility_color)
                embed.set_image(url = ctx.message.attachments[0].url)
                embed.add_field(name="Key", value = key)
                embed.add_field(name = "Message", value = msg, inline = False)
                embed.set_footer(text = "Use this Key to access this message anytime")
                embed.set_author(name = self.client.user.name, icon_url = self.client.user.avatar_url)
                self.save_data(msg_data)
                await ctx.send(embed =embed)
            else:
                msg_data[key] = [msg, ctx.author.name]
                embed = discord.Embed(title = "Message Saved", color = utility_color)
                embed.add_field(name="Key", value = key, inline = False)
                embed.add_field(name = "Message", value = msg, inline = False)
                embed.set_footer(text = "Use this Key to access this message anytime")
                embed.set_author(name = self.client.user.name ,icon_url = self.client.user.avatar_url)
                self.save_data(msg_data)
                await ctx.send(embed = embed)
                return
        
        except Exception as e:
            await ctx.send(e)
                
    @commands.command()
    async def getmsg(self, ctx, key):
        try: 
            data = []
            if key in msg_data.keys():
                data = msg_data[key]
                if len(data) > 2:
                    msg = data[0]
                    author = data[1]
                    embed = discord.Embed(title =f"Message Saved by {author.title()}", color = utility_color)
                    embed.add_field(name = "Message", value = msg)
                    embed.set_image(url = data[2])
                    await ctx.send(embed = embed)
                else:
                    msg = data[0]
                    author = data[1]
                    embed = discord.Embed(title =f"Message Saved by {author.title()}", color = utility_color)
                    embed.add_field(name = "Message", value = msg)
                    await ctx.send(embed = embed)
            else:
                await ctx.send(embed = discord.Embed(description = "Are you sure that key actually exists?",color=exception_color))
            
            
        except Exception as e:
            await ctx.send(e)


    @commands.command()
    async def secretmsg(self, ctx, message: discord.Message):
        
        cap_msg = cap_pass = ''.join(random.choice((str.upper, str.lower))(c) for c in message.content)
        reversed_msg = cap_msg[::-1]
        
        await ctx.send(embed = discord.Embed(title = "Secret message for you", description = reversed_msg, color = function_color))

    def save_data(self, data):
        data = str(data)
        data = "msg_data = "+data
        with open ("msg_data.py","w") as datafile:
            datafile.write(data)


def setup(client):
    client.add_cog(Message(client))
