import discord
from discord.ext import commands
import aiohttp
import json

class Main:
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def ping(self):
    await self.client.say("Pong!")
  
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
  
  @commands.command(hidden=True, pass_context=True)
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
