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
  @client.command()
  async def hello(self, ctx):
    await ctx.send('Hi')

  #Ping/Pong
  @client.command()
  async def ping(self, ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

  #8 Ball
  @client.command(aliases = ['8ball'])
  async def eightBall(self, ctx, *, question):
    await ctx.send(f'Question: {question}\n Answer: {random.choice(eightBallresponses)}')
  

def setup(client):
  client.add_cog(miscellaneous(client))

  
