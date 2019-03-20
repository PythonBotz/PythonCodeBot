import discord
from discord.ext import commands
import aiohttp
import json

class Fun:
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def ping(self):
    await self.client.say("Pong!")
  
  @commands.command()
  async def python(self):
    await self.client.say("You need python 3.6.5 version")
  
  @commands.command()
  async def test():
    embed = discord.Embed(description=" ")
    embed.add_field(name="test1", value="test2")
    await self.client.say(embed=embed)
    
def setup(client):
  client.add_cog(Fun(client))
