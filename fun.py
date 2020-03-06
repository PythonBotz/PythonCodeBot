import discord
from discord.ext import commands
import aiohttp
import json
import inspect

class Main:
  def __init__(self, client):
    self.client = client
  
  @commands.command(pass_context=True)
  async def ping(self, ctx):
    """pseudo-ping time"""
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await self.client.send_typing(channel)
    t2 = time.perf_counter()
    await self.client.say("🏓 {}ms".format(round((t2-t1)*1000)))
  
  @commands.command()
  async def python(self):
    await self.client.say("You need python 3.6.5 version")
    
  @commands.command(hidden=True)
  async def baselink(self):
    await self.client.say("<https://discordapp.com/oauth2/authorize?&client_id=YOUR_CLIENTID_HERE&scope=bot&permissions=YOUR_VALUE_HERE>")
    
  @commands.command()
  async def download(self):
    """| download link for python 3.6.5"""
    await self.client.say("<https://www.python.org/downloads/release/python-365/>")
    
  @commands.command()
  async def help(self):
    embed = discord.Embed(description=" ")
    embed.add_field(name="Help", value="Shows this message")
    embed.add_field(name"download", value="Shows download link for Python")
    embed.add_field(name="Ping", value="Shows simple ping")
    await self.client.say(embed=embed)
    
  def user_is_me(ctx):
    return ctx.message.author.id == "601622622957994006"
  
  @commands.command(name="eval", hidden=True, pass_context=True)
  @commands.check(user_is_me)
  async def _eval(self, ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
      await self.client.say(await res)
    else:
      await self.client.delete_message(ctx.message)
      await self.client.say(res)
  
def setup(client):
  client.add_cog(Main(client))
