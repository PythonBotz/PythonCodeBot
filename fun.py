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
    
def setup(client):
  client.add_cog(Main(client))
