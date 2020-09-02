import requests
import urllib.request
import time
from bs4 import BeautifulSoup

NORMAL_KILLS_INDEX = 0
NORMAL_DEATHS_INDEX = 1
NORMAL_KD_RATIO_INDEX = 2
FINAL_KILLS_INDEX = 3
FINAL_DEATHS_INDEX = 4
FINAL_KD_RATIO_INDEX = 5
WINS_INDEX = 6
LOSSES_INDEX = 7
WIN_LOSS_RATIO_INDEX = 8
BEDS_BROKEN_INDEX = 9

def getBedStats(username: str, gamemode: int):
  if (gamemode == -1):
    return "Ur trolling, nice try buddy. Invalid Input: 1's, 2's, 3's, & 4's are the only supported gamemodes."

  userlink = generateLink(username)
  gamestats = scrapeData(userlink, gamemode)

  if (gamestats):
    return createStatMessage(username, gamemode, gamestats)
  return "Invalid username, try again"  

def generateLink(username: str):
  userLink = 'https://plancke.io/hypixel/player/stats/' + username + '#Bedwars'
  return userLink

def scrapeData(userlink: str, gamemode: int):
  # Connect to the URL
  dater = requests.get(userlink)

  # Parse HTML and save to BeautifulSoup object
  soup = BeautifulSoup(dater.text, "html.parser")

  # If invalid username, return empty array
  if (soup.find_all("b", text="Player does not exist!")):
    return []

  # Select all tr (table row) elements in the bedwars table and append them to trs
  bedwars_div = soup.find(id="stat_panel_BedWars")
  stat_table = bedwars_div.find("table", class_="table")
  trs = stat_table.select("tr")

  # Loops through all the tr's that have actual stats in them
  stat_trs = []
  for tr in trs:
    if (len(tr.select("td")) == 10): # 10 is the number of stats for each gamemode
      stat_trs.append(tr)          

  tds = stat_trs[gamemode - 1].find_all("td")
  game_stats = []
  for td in tds:
    game_stats.append(td.text)

  return game_stats 


def createStatMessage(username: str, gamemode: int, gamestats: []):
  gs = gamestats
  gametype_string: str
  if (gamemode == 1):
    gametype_string = "Solo"
  elif (gamemode == 2):
    gametype_string = "Doubles"
  elif (gamemode == 3):
    gametype_string = "Threes"
  else:
    gametype_string = "Fours"

  beds_per_game = round(((int(gs[BEDS_BROKEN_INDEX]) / (int(gs[WINS_INDEX]) + int(gs[LOSSES_INDEX]))) * 1000)) / 1000
  
  first_line = "```prolog\n"
  second_line = f"BedWars Stats: {username} - {gametype_string}\n"
  third_line = "---------------------------------------\n"
  fourth_line = f"Total Normal Kills/Deaths: {gs[NORMAL_KILLS_INDEX]} - {gs[NORMAL_DEATHS_INDEX]}, {gs[NORMAL_KD_RATIO_INDEX]}KD\n"
  fifth_line = f"Total Final Kills/Deaths: {gs[FINAL_KILLS_INDEX]} - {gs[FINAL_DEATHS_INDEX]}, {gs[FINAL_KD_RATIO_INDEX]}KD\n"
  sixth_line = f"Beds Broken: {gs[BEDS_BROKEN_INDEX]} Broken, {beds_per_game} per game\n"
  seventh_line = f"Wins & Losses: {gs[WINS_INDEX]}Ws, {gs[LOSSES_INDEX]}Ls - {gs[WIN_LOSS_RATIO_INDEX]}W/L\n"
  eighth_line = "```"
  
  message = first_line + second_line + third_line + fourth_line + fifth_line + sixth_line + seventh_line + eighth_line
  return message
