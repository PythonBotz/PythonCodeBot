import discord
from discord.ext import commands

class Fun:
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def ping(self):
    await self.client.say("Pong!")
    
  @commands.command(pass_context=True)
  async def userinfo(self, ctx user: discord.Member):
    embed = discord.Embed(description=" ")
    embed.add_field(name="Nickname", value="{}".format(ctx.message.author))
    await self.client.say(embed=embed)
    
def setup(client):
  client.add_cog(Fun(client))
