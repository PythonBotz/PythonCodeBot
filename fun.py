import discord
from discord.ext import commands
import aiohttp
import json

class Fun:
  def __init__(self, client):
    self.client = client
    
  @commands.command()
  async def ping(self):
    await self.client.say("Pong!")
  
  @commands.command()
  async def python(self):
    await self.client.say("You need python 3.6.5 version")
  
  rank = {
    "24":{"Major General"}
    
  @commands.command(pass_context=True)
  async def ratings(self, ctx, user: str):
    url = "http://ratings.tankionline.com/get_stat/profile/?user={}&lang=en".format(user)
    async with aiohttp.get(url) as r:
      if r.status == 200:
        try:
          response = (await r.json ())["response"]
          kills = response["kills"]
          deaths = response["deaths"]
          crystals = response["earnedCrystals"]
          gold = response["caughtGolds"]
          experience = response["score"]
          premium = response["hasPremium"]
          ranks = response["rank"]
          gearscore = response["gearScore"]
          embed = discord.Embed(title="Tanki Online Ratings".format(user), url="http://ratings.tankionline.com/en/user/{}/".format(user), \
                                description="**Profile:**", color=0x42d9f4)
          embed.add_field(name="Nickname", value="{}".format(user), inline=False)
          embed.add_field(name="Rank", value="{}".format(ranks), inline=False)
          embed.add_field(name="Premium Account", value="{}".format(premium), inline=False)
          embed.add_field(name="Experience", value="{:,}".format(experience), inline=False)
          embed.add_field(name="Crystals Obtained", value="{:,}".format(crystals), inline=False)
          embed.add_field(name="Gold Boxes Caught", value="{:,}".format(gold), inline=False)
          embed.add_field(name="Gear Score", value="{:,}".format(gearscore), inline=False)
          embed.add_field(name="Kills", value="{:,}".format(kills), inline=False)
          embed.add_field(name="Deaths", value="{:,}".format(deaths), inline=False)
          embed.add_field(name="K/D", value="{0:.2f}".format(kills/deaths), inline=False)
          await self.client.say(embed=embed)
        except:
          await self.client.say("Account does not exist.")
    
def setup(client):
  client.add_cog(Fun(client))
