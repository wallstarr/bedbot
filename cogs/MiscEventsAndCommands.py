import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

class MiscEventsAndCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener() 
    async def on_ready(self):
        print("Ready!")

def setup(bot):
    bot.add_cog(MiscEventsAndCommands(bot)) 