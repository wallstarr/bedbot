import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = '!')

# Custom Help Command
client.remove_command("help")
@client.command()
async def help(ctx):
    first_line = "```diff\n"
    second_line = "                BedBot Help:\n"
    third_line = "--------------------------------------------\n"
    fourth_line = "+ !bedwars <gamemode> <username>\n"
    fifth_line = "     - For <gamemode> use 1, 2, 3, or 4 to get stats for said gamemode.\n"
    sixth_line = "```\n*If you like BedBot visit https://github.com/wallstarr/bedbot and give me a star!*"
    message = first_line + second_line + third_line + fourth_line + fifth_line + sixth_line
    await ctx.send(message)

# Cog Loading/Unloading Commands
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
