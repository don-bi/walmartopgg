import requests
import json
import pprint
import random
import os
def find_summoner_info(user):
    token = api_key
    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{user}"
    data = json.loads(requests.get(url, headers = {"X-Riot-Token" : token}).text)
    return data