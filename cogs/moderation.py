import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$')

f = open('rules.txt', 'r')
rules = f.readlines()

class moderation(commands.Cog):
  
  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Moderation commands are ready')

  #Rules command
  @client.command(aliases = ['rules'])
  async def rule(self, ctx, *, number):
    await ctx.send(rules[int(number)-1])

  #Purge command
  @client.command(aliases = ['c', 'purge'])
  @commands.has_permissions(manage_messages = True)
  async def clear(self, ctx, amount=2):
    await ctx.channel.purge(limit = amount)

  #Kick command
  @client.command(aliases = ['k'])
  @commands.has_permissions(kick_members = True)
  async def kick(self, ctx, member : discord.Member, *, reason = 'No reason provided'):
    await member.kick(reason = reason)

  #Ban command
  @client.command(aliases = ['b'])
  @commands.has_permissions(ban_members = True)
  async def ban(ctx, member : discord.Member, *, reason = 'No reason provided'):
    await member.ban(reason = reason)

  #Unban command
  @client.command()
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.mention}')
        return

def setup(client):
  client.add_cog(moderation(client))

  
