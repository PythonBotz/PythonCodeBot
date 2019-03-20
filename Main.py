import discord
from discord.ext import commands
import asyncio
import inspect
import os

extensions = ["fun"]

bot = commands.Bot(command_prefix=("p!"))

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="p!help"))
	print("Logged in as")
	print(bot.user.name)
	print(bot.user.id)
	
@bot.command()
async def load(extension):
	try:
		bot.load_extension(extension)
		print("loaded {}".format(extension))
	except Exception as error:
		print("{} cannot be loaded. [{}]".format(extension, error))
		
@bot.command()
async def unload(extension):
	try:
		bot.unload_extension(extension)
		print("unloaded {}".format(extension))
	except Exception as error:
		print("{} cannot be unloaded. [{}]".format(extension, error))

if __name__ == "__Main__":
	for extension in extensions:
		try:
			bot.load_extension(extension)
		except Exception as error:
			print("{} cannot be loaded. [{}]".format(extension, error))
			
	bot.run(os.environ['BOT_TOKEN'])
