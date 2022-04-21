import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv

bot = commands.Bot(command_prefix=['~'], intents=discord.Intents.all(), description='')
startup_extensions = ['fun']


@bot.event
async def on_ready():
  
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your every move"))
  
  for extension in startup_extensions:
    try:
      bot.load_extension(extension)
    except Exception as e:
      print(e)

  print('Hello, world!')


load_dotenv()
TOKEN = getenv('TOKEN')

bot.run(TOKEN)