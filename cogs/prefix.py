import discord
import json
from discord.ext import commands

client = commands.Bot(command_prefix='$')

class prefix(commands.Cog):
  
  def __init__(self,client):
    self.client = client

  def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
      prefixes = json.load

    return prefixes[str(message.guild.id)]

  client = commands.Bot(command_prefix = get_prefix)

  @commands.Cog.listener()
  async def on_ready(self):
    print('Prefix Commands are ready')

  @client.event 
  async def on_guild_join(self, ctx, guild):
    with open('prefixes.json', 'r') as f:
      prefixes = json.load(f)
    
    prefixes[str(guild.id)] = '$'

    with open('prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent = 4)

  @client.event 
  async def on_guild_remove(self, ctx, guild):
    with open('prefixes.json', 'r') as f:
      prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent = 4)

  @client.event 
  async def changeprefix(self, ctx, prefix):
    with open('prefixes.json', 'r') as f:
      prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent = 4)
  

def setup(client):
  client.add_cog(prefix(client))

  
