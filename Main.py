import discord
from discord.ext import commands
import asyncio
import os
import time

client = commands.Bot(command_prefix = "p!")
client.remove_command('help')

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="p!help"))
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print(discord.__version__)
	
@client.event
async def on_member_join(member):
	server = member.server
	channel = client.get_channel("596774141592600606")
	embed = discord.Embed(title="👋 {} just joined {}".format(member.name, server.name), description="Welcome! to {} {}! Enjoy your stay here!".format(server.name, member.name), color=0x00ff00)
	embed.set_thumbnail(url=member.avatar_url)
	embed.add_field(name="Current Member Count", value=member.server.member_count)
	await client.send_message(channel, embed=embed)

@client.event
async def on_member_remove(member):
	channel = client.get_channel("596774141592600606")
	embed = discord.Embed(title="👋 {} just left the server.".format(member.name), description="Goodbye! {} hope to see you again".format(member.name), color=0x00ff00)
	embed.set_thumbnail(url=member.avatar_url)
	embed.add_field(name="Current Member Count", value=member.server.member_count)
	await client.send_message(channel, embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await client.send_typing(channel)
	t2 = time.perf_counter()
	await client.say("🏓 {}ms".format(round((t2-t1)*1000)))
  
@client.command()
async def python():
	await client.say("You need python 3.6.5 version")
    
@client.command()
async def baselink():
	await client.say("<https://discordapp.com/oauth2/authorize?&client_id=YOUR_CLIENTID_HERE&scope=bot&permissions=YOUR_VALUE_HERE>")
    
@client.command()
async def download():
	"""| download link for python 3.6.5"""
	await client.say("<https://www.python.org/downloads/release/python-365/>")
    
@client.command(pass_context=True)
async def help(ctx):
	embed = discord.Embed(description=" ")
	embed.add_field(name="Help", value="Shows this message", inline=False)
	embed.add_field(name="download", value="Shows download link for Python", inline=False)
	embed.add_field(name="Ping", value="Shows simple ping", inline=False)
	await client.say(embed=embed)
    
def user_is_me(ctx):
	return ctx.message.author.id == "601622622957994006"
  
@client.command(name="eval", hidden=True, pass_context=True)
@commands.check(user_is_me)
async def _eval(self, ctx, *, command):
	res = eval(command)
	if inspect.isawaitable(res):
		await client.say(await res)
	else:
		await client.delete_message(ctx.message)
		await client.say(res)
			
client.run(os.environ['BOT_TOKEN'])
