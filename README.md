# BedBot 

## A Python 3 Discord bot made using Discord.py and Beautiful Soup for Minecraft BedWars

### Contributors
- Dan Blustein
- Junryu Fu

### How to use the bot
- !bedwars is the only command. Add a number (1, 2, 3, or 4 for Solo, Double, Threes, and Fours respectivevly) and then add a username
- For example, !bedwars 4 wallstarr gets the stats for user with username wallstarr in the Fours gamemode. 

### Demo Gif:
![Screen-Recording-2020-09-06-at-1](https://user-images.githubusercontent.com/51876078/92317407-2bfda000-f03b-11ea-9c04-6ab9fe5140f2.gif)

### How to develop and run the bot locally
- First install the required modules
```
pip3 install -r requirements.txt
```
- There is a fair amount of documentation in /cogs/game_functions/bw_scraper.py explaining what each method does. 
- This bot utilizes a [cogs system](https://www.youtube.com/watch?v=vQw8cFfZPx0&t=670s&ab_channel=Lucas) -- this is because we may add other player stat retrieving functions for different games to our bot in the future. 
- To actually run the bot locally, just cd into the main bedbot folder and run:
```
python3 bedbot.py
```
