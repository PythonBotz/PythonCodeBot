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
	
@bot.command(pass_context=True)
async def autobaselink(ctx):
	try:
		x = int(ctx.message.content[15:])
		await bot.say("**Your bot's invite link is:** <https://discordapp.com/oauth2/authorize?&client_id=" + str(x) + "&scope=bot&permissions=8>")
	except:
		text = await bot.say("**Invalid client id, recheck the id and make sure that you didn't accidentally use your bot token or client secret <@" + str(ctx.message.author.id) + ">**")
		await bot.delete_message(ctx.message)
		await asyncio.sleep(5)
		await bot.delete_message(text)
		
@bot.command(pass_context=True)
async def pythondownload(ctx):
	await bot.send_message(ctx.message.channel, embed=discord.Embed(title="Here's the python download, description=f"[Click here](https://www.python.org/downloads/release/python-365/), colour=0X008CFF")
  
bot.run(os.environ['BOT_TOKEN'])
