import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '[', intents = intents)

@bot.event
async def on_ready():
    print("bot is online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(987743603700928572)
    await channel.send(f'{member} joins!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(987743634805891113)
    await channel.send(f'{member} leaves!')


bot.run("OTg3NzIyODA1ODUwMzA4NzI5.G52qqc.zfcny6oaENC4-CaQYWPLaCVvDHqcttIRAWYzeY")
