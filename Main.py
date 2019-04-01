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
	
@client.command()
async def load(extension):
	try:
		client.load_extension(extension)
		print("loaded {}".format(extension))
	except Exception as error:
		print("{} cannot be loaded. [{}]".format(extension, error))
		
@client.command()
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
