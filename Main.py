import discord
from discord.ext import commands
import asyncio
import os

extensions = ["fun", "moderation"]

client = commands.Bot(command_prefix = "p!")

@client.event
async def on_ready():
	print("Bot online")
	
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
