import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='$')

f = open('8ball.txt', 'r')
eightBallresponses = f.readlines()

class miscellaneous(commands.Cog):
  
  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Miscellaneous Commands are ready')

  #Hello command
  @client.command(aliases = ['Hello'])
  async def hello(self, ctx):
    await ctx.send('Hi')

  #8 Ball
  @client.command(aliases = ['8ball', '8Ball', 'EightBall', 'eightball'])
  async def eightBall(self, ctx, *, question):
    eightBallEmbed = discord.Embed(
      color = 0xF2BAC9
    )
    eightBallEmbed.set_author(name = '8-Ball', icon_url = 'https://legomenon.com/images/magic-8-ball-game-accurate.png')
    eightBallEmbed.add_field(name = 'Mystical 8 Ball says', value = str(f'{random.choice(eightBallresponses)}'), inline = True)
    await ctx.send(embed = eightBallEmbed)

  

def setup(client):
  client.add_cog(miscellaneous(client))

  
