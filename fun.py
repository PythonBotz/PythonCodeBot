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
    
def setup(client):
  client.add_cog(Main(client))
