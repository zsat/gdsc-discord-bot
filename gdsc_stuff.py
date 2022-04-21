from discord.ext import commands
import discord


class gdsc_stuff(commands.Cog):

  def __init__(self, bot):
    self.bot = bot





def setup(bot):
  bot.add_cog(gdsc_stuff(bot))