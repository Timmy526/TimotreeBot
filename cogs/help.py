import discord 
from discord.ext import commands 

client = commands.Bot(command_prefix='$')
client.remove_command('help')

class help(commands.Cog):  
  def __init__(self, bot): 
    self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print('Help is ready')

  @client.group()
  async def help(self, ctx):
    helpEmbed = discord.Embed(title = 'Help', description = 'List of commands', color=0xF2BAC9)

    helpEmbed.add_field(name = 'Moderation', value = 'Ban, Kick, Purge, Rules, Unban', inline = False)
    helpEmbed.add_field(name = 'Miscellaneous', value = '8ball, Hello, Ping', inline = False)
    await ctx.send(embed = helpEmbed)
  
  @help.command() 
  async def kick(self, ctx):
    helpEmbed = discord.Embed(title = 'Kick', description = 'Kicks a member from the server', color = discord.Color.red)
    helpEmbed.add_field(name = '**Syntax**', value = '$kick {member} [reason]')

    await ctx.send(embed = helpEmbed)

def setup(bot):
  bot.add_cog(help(bot))
