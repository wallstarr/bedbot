import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def bedbot(ctx):
    await ctx.send(f'ur stats are bad. \nlatency: {round(client.latency * 1000)}ms')
    print("Bruh")


client.run("token here")
