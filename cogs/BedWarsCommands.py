import discord
from discord.ext import commands

# ↓ This import statement would usually never work but it does because
# ↓ it is being called from bedbot.py when bedbot.py gets executed
import cogs.game_functions.bw_scraper as scraper

class BedWarsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def bedwars(self, cxt, gamemode, username):
        await cxt.send(scraper.getBedStats(username, convertGamemodeStringToInt(gamemode)))
        print("Bedwars command received")

def setup(bot):
    bot.add_cog(BedWarsCommands(bot))

def convertGamemodeStringToInt(gamemode: str):
    if (gamemode == "1"):
        return 1
    elif (gamemode == "2"):
        return 2
    elif (gamemode == "3"): 
        return 3
    elif (gamemode == "4"):   
        return 4
    else:
        return -1    