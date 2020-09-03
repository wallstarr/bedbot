import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = '!')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')        

cogs = ['cogs.BedWarsCommands', 'cogs.MiscEventsAndCommands']

if __name__ == '__main__':
    for cog in cogs:
        client.load_extension(cog)
    
client.run(os.getenv('TOKEN'))
