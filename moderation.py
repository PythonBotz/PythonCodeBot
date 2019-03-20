import discord
from discord.ext import commands

class Moderation:
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def userinfo(self):
    await self.client.say("your nickname is noobperson")
    
def setup(client):
  client.add_cog(Moderation(client))
