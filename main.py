import discord
import os
import keep_alive
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix='$')
status = cycle(['Valorant', 'TFT', 'League of Legends', 'Spotify'])


@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.online)
    print('Bot is ready')


keep_alive.keep_alive()


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command does not exist')


@tasks.loop(hours=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


#Load Cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


#Unload Cogs
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


#Reload Cogs
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


#Goes to the Cog directory and loads the py files
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


#Autoroles
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Saplings')
    await client.add_roles(member, role)
    print('Role has been assigned')


client.run(os.getenv('TOKEN'))
