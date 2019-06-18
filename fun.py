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
  
  @commands.command()
  async def welcome(self):
    embed = discord.Embed(title="👋 Nucleo | RJ just joined discord.py"), description="Welcome! to discord.py Nucleo | RJ! Enjoy your stay here!"), color=0x00ff00)
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/rQcK0ZEeVhvlER973W2DG94YocL9bJuwx-vii-dNrus/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/403250141236166656/5ac09cf70179ad4d06aa2087edd8cd82.webp?format=png")
    embed.add_field(name="Current Member Count", value="58")
    await self.client.send_message(message.channel, embed=embed)
    
def setup(client):
  client.add_cog(Main(client))
