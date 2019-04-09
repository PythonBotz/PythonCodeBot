import discord
from discord.ext import commands
import asyncio
import os

extensions = ["fun"]

client = commands.Bot(command_prefix = "p!")

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="testing the bot"))
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	
@client.event
async def on_member_join(member):
	server = member.server
	channel = bot.get_channel("517207233767931906")
	embed = discord.Embed(title="👋 {} just joined {}".format(member.name, server.name), description="Welcome! to {} {}! Enjoy your stay here!".format(server.name, member.name), color=0x00ff00)
	embed.set_thumbnail(url=member.avatar_url)
	embed.add_field(name="Current Member count", value=member.server.member_count)
	await client.send_message(channel, embed=embed)

@client.event
async def on_member_remove(member):
	channel = bot.get_channel("517207233767931906")
	embed = discord.Embed(title="👋 {} just left the server.".format(member.name), description="Goodbye! {} hope to see you again".format(member.name), color=0x00ff00)
	embed.set_thumbnail(url=member.avatar_url)
	embed.add_field(name="Current Member Count", value=member.server.member_count)
	await client.send_message(channel, embed=embed)
	
@client.command(hidden=True)
async def load(extension):
	try:
		client.load_extension(extension)
		print("loaded {}".format(extension))
	except Exception as error:
		print("{} cannot be loaded. [{}]".format(extension, error))
		
@client.command(hidden=True)
async def unload(extension):
	try:
		client.unload_extension(extension)
		print("unloaded {}".format(extension))
	except Exception as error:
		print("{} cannot be unloaded. [{}]".format(extension, error))

if __name__ == "__main__":
	for extension in extensions:
		try:
			client.load_extension(extension)
		except Exception as error:
			print("{} cannot be loaded. [{}]".format(extension, error))
			
	client.run(os.environ['BOT_TOKEN'])
