import discord
from discord.ext import commands
import asyncio
import os

extensions = ["fun"]

client = commands.Bot(command_prefix = "p!")

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
	
def user_is_me(ctx):
	return ctx.message.author.id == "601622622957994006"
	
@client.command(hidden=True)
@commands.check(user_is_me)
async def load(extension):
	try:
		client.load_extension(extension)
		await client.say("loaded {}".format(extension))
	except Exception as error:
		await client.say("{} cannot be loaded. [{}]".format(extension, error))
		
@client.command(hidden=True)
@commands.check(user_is_me)
async def unload(extension):
	try:
		client.unload_extension(extension)
		await client.say("unloaded {}".format(extension))
	except Exception as error:
		await client.say("{} cannot be unloaded. [{}]".format(extension, error))

if __name__ == "__main__":
	for extension in extensions:
		try:
			client.load_extension(extension)
		except Exception as error:
			print("{} cannot be loaded. [{}]".format(extension, error))
			
	client.run(os.environ['BOT_TOKEN'])
