import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("STEAM_API_KEY")
steam_id = "76561199125657263"  # replace with your real 17-digit SteamID64

url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"

params = {
    "key": api_key,
    "steamid": steam_id,
    "format": "json",
    "include_appinfo": True,
}

response = requests.get(url, params=params)
data = response.json()
games = data["response"]["games"]

for game in games:
    print(game["name"], game["playtime_forever"] / 60)
