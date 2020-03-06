import discord
from discord.ext import commands
import asyncio
import os

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
			
client.run(os.environ['BOT_TOKEN'])
