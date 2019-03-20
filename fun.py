import discord
from discord.ext import commands

class Fun:
  def __init__(self, client):
    self.client = bot
    
  @commands.command()
  async def ping(self):
    await self.bot.say("Pong!")
    
def setup(bot):
  bot.add_cog(Fun(bot))
