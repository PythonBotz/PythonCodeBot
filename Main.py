import discord
from discord.ext import commands
import asyncio
import inspect
import os

bot = commands.Bot(command_prefix=("p!"))

@bot.event
async def on_ready():
  print('Logged in as')
  print(bot.user.name)
  print(bot.user.id)
  
@bot.command(pass_context=True)
async def python(ctx):
  """Tells you which python version you need"""
  await bot.say('you need python 3.6.5')
  
def user_is_me(ctx):
	return ctx.message.author.id == "277983178914922497"

@bot.command(name='eval', pass_context=True, hidden=True)
@commands.check(user_is_me)
async def _eval(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await bot.say(await res)
    else:
    	await bot.say(res)
  
bot.run(os.environ['BOT_TOKEN'])
