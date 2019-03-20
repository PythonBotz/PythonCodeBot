import discord
from discord.ext import commands

class Fun:
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def ping(self):
    await self.client.say("Pong!")
    
def setup(client):
  client.add_cog(Fun(cliebt))
