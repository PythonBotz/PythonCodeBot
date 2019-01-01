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

@bot.event
async def on_member_join(member):
	await bot.get_channel("517207233767931906")
	await bot.send_message(message.channel, "Welcome + member.name + to {} server :wink:".format(server.name))
  
@bot.command(pass_context=True)
async def python(ctx):
  """Tells you which python version you need"""
  await bot.say('you need python 3.6.5 version')
  
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
  
bot.run(os.environ['BOT_TOKEN'])
