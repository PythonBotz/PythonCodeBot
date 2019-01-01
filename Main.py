import discord
from discord import commands

@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  
@bot.command(pass_context=True)
async def python(ctx):
  """Tells you which python version you need"""
  await bot.say('you need python 3.6.5')
  
bot.run(os.environ['BOT_TOKEN'])
