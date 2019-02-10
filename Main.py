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
	server = member.server
	channel = bot.get_channel("517207233767931906")
	embed = discord.Embed(title="👋 {} just joined {}".format(member.name, server.name), description="Welcome! to {} {}! Enjoy your stay here!".format(server.name, member.name), color=0x00ff00)
	embed.set_thumbnail(url=member.avatar_url)
	embed.add_field(name="Current Member count", value="there is {} members in this server".format(member.server.member_count))
	await bot.send_message(channel, embed=embed)

@bot.event
async def on_member_remove(member):
	channel = bot.get_channel("517207233767931906")
	embed = discord.Embed(title="👋 {} just left the server.".format(member.name), description="Goodbye! {} hope to see you again".format(member.name), color=0x00ff00)
	embed.set_thumbnail(url=member.avatar_url)
	embed.add_field(name="Current Member Count", value="there is {} members in this server".format(member.server.member_count))
	await bot.send_message(channel, embed=embed)
  
@bot.command(pass_context=True)
async def python(ctx):
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
		
@bot.command(name="addrole", pass_context=True, hidden=True)
@commands.has_permissions(administrator=True, manage_roles=True)
async def _addrole(ctx, user: discord.Member = None, *, name = None):
	author = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name=name)
	await bot.add_roles(user, role)
	text = await bot.say(f'{author.mention} I have added the {role.name} role to a user {user.name}'.format(role.name))
	await bot.delete_message(ctx.message)
	await asyncio.sleep(1)
	await bot.delete_message(text)
    
@_addrole.error
async def addrole_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have a manage roles permission to use this command.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)

@bot.command(name="removerole", pass_context=True, hidden=True)
@commands.has_permissions(administrator=True, manage_roles=True)
async def _removerole(ctx, user: discord.Member = None, *, name = None):
	author = ctx.message.author
	role = discord.utils.get(ctx.message.server.roles, name=name)
	await bot.remove_roles(user, role)
	text = await bot.say(f'{author.mention} I have removed the {role.name} role from a user {user.name}'.format(role.name))
	await bot.delete_message(ctx.message)
	await asyncio.sleep(1)
	await bot.delete_message(text)
	
@_removerole.error
async def removerole_error(error, ctx):
	if isinstance(error, discord.ext.commands.errors.CheckFailure):
		text = "Sorry {}, You don't have a manage roles permission to use this command.".format(ctx.message.author.mention)
		await bot.send_message(ctx.message.channel, text)
  
bot.run(os.environ['BOT_TOKEN'])
