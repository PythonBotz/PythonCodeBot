import discord
from discord.ext import commands
import asyncio

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  
@client.command(pass_context=True)
async def python(ctx):
  """Tells you which python version you need"""
  await client.say('you need python 3.6.5')
  
client.run(os.environ['BOT_TOKEN'])
