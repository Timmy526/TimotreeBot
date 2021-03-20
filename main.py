import discord
import os
import keep_alive
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

client = commands.Bot(command_prefix="$", help_command = None)
status = cycle(['Valorant', 'TFT', 'League of Legends', 'Spotify'])
keep_alive.keep_alive()


@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.online)
    print('Bot is ready')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command does not exist')
        await client.process_commands(ctx)


#Autoroles
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Unverified')
    await member.add_roles(role)


@client.command()
async def displayembed(ctx):
    embed = discord.Embed(title='Title',
                          description='This is a description',
                          color=0xF2BAC9)
    embed.set_footer(text='This is a footer.')
    embed.set_image(
        url=
        'https://image.freepik.com/free-vector/cute-panda-eat-ramen-noodle-icon-illustration-panda-mascot-cartoon-character-animal-icon-concept-isolated_138676-839.jpg'
    )
    embed.set_thumbnail(
        url=
        'https://image.freepik.com/free-vector/cute-panda-eat-ramen-noodle-icon-illustration-panda-mascot-cartoon-character-animal-icon-concept-isolated_138676-839.jpg'
    )
    embed.set_author(
        name='Author Name',
        icon_url=
        'https://image.freepik.com/free-vector/cute-panda-eat-ramen-noodle-icon-illustration-panda-mascot-cartoon-character-animal-icon-concept-isolated_138676-839.jpg'
    )
    embed.add_field(name='Field Name 1', value='Field Value', inline=False)
    embed.add_field(name='Field Name 2', value='Field Value', inline=True)
    embed.add_field(name='Field Name 3', value='Field Value', inline=True)

    await ctx.send(embed=embed)


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

#Ping/Pong
@client.command()
async def ping(ctx):
    pingEmbed = discord.Embed(color=0xF2BAC9)
    pingEmbed.add_field(name='Ping',
                        value=str(f'Pong! {round(client.latency * 1000)}ms'),
                        inline=True)

    await ctx.send(embed=pingEmbed)

client.run(os.getenv('TOKEN'))
