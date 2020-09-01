import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://plancke.io/hypixel/player/stats/samuraigorila10#BedWars'

# Connect to the URL
dater = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(dater.text, "html.parser")

THREES_NORMAL_KILLS_INDEX = 86
THREES_NORMAL_DEATHS_INDEX = 87
THREES_NORMAL_RATIO_INDEX = 88
THREES_FINAL_KILLS_INDEX = 89
THREES_FINAL_DEATHS_INDEX = 90
THREES_FINAL_RATIO_INDEX = 91
THREES_WINS_INDEX = 92
THREES_LOSSES_INDEX = 93
THREES_WIN_RATIO_INDEX = 94
THREES_BEDS_INDEX = 95

FOURS_NORMAL_KILLS_INDEX = 96
FOURS_NORMAL_DEATHS_INDEX = 97
FOURS_NORMAL_RATIO_INDEX = 98
FOURS_FINAL_KILLS_INDEX = 99
FOURS_FINAL_DEATHS_INDEX = 100
FOURS_FINAL_RATIO_INDEX = 101
FOURS_WINS_INDEX = 102
FOURS_LOSSES_INDEX = 103
FOURS_WIN_RATIO_INDEX = 104
FOURS_BEDS_INDEX = 105

selection = soup.select('td')
tds = []
for td in selection:
    tds.append(td)
    if td.text == '22':
        print(len(tds) - 1)

def generatelink(user):
  userlink = 'https://plancke.io/hypixel/player/stats/' + str(user) + '#Bedwars'
  print(userlink)

