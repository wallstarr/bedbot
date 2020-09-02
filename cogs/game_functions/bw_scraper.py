import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def getBedStats(username: str, gamemode: int):
  if (gamemode == -1):
    return "Invalid Input: 1's, 2's, 3's, & 4's are the only supported gamemodes."

  userLink = generateLink(username)

  # Connect to the URL
  dater = requests.get(userLink)

  # Parse HTML and save to BeautifulSoup object
  soup = BeautifulSoup(dater.text, "html.parser")

  # Select all tr (table row) elements in the bedwars table and append them to trs
  bedwars_div = soup.find(id="stat_panel_BedWars")
  stat_table = bedwars_div.find("table", class_="table")
  stat_tr = stat_table.select("tr")

  # Loops through all the tr's that have actual stats in them
  stats = []
  for tr in stat_tr:
    if (len(tr.select("td")) == 10): # 10 is the number of stats for each gamemode
      stats.append(tr)
      for td in tr.select("td"):
        print(td.text)
        
        
  return "Placeholder"  

def generateLink(username: str):
  userLink = 'https://plancke.io/hypixel/player/stats/' + username + '#Bedwars'
  return userLink

def scrapeData(userlink: str, gamemode: int):
  print("Placeholder")