import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = '!')

cogs = ['cogs.BedWarsCommands', 'cogs.MiscEventsAndCommands']

if __name__ == '__main__':
    for cog in cogs:
        client.load_extension(cog)
    
client.run(os.getenv('TOKEN'))
