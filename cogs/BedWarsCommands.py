import discord
from discord.ext import commands

class BedWarsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def bedwars(self, cxt):
        await cxt.send("Your stats are pretty bad")
        print("Bedwars command received")

def setup(bot):
    bot.add_cog(BedWarsCommands(bot))    