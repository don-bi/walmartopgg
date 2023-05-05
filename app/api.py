import requests
import json
import pprint as pp
import random
import os
import time

global token
token = "RGAPI-aa7be6ad-ab76-4479-b84a-65dc2b81f792"

def create_summoner_ids():
    league_list = ['challenger','grandmaster','master']
    for league in league_list:
        url = f"https://na1.api.riotgames.com/lol/league/v4/{league}leagues/by-queue/RANKED_SOLO_5x5"
        data = json.loads(requests.get(url, headers = {"X-Riot-Token" : token}).text)
        summonerids = []
        for player in data['entries']:
            summonerids.append(player['summonerId'])
            if (len(summonerids) >= 1000):
                break
    
    f = open("summoner_ids.txt", "w")
    for id in summonerids:
        f.write(id + "\n")
    f.close()

# create_summoner_ids()

def find_match_ids():
    f = open("summoner_ids.txt", "r")
    summonerids = f.readlines() #list of summoner ids
    count = 0
    f.close()
    match_ids = {}
    for id in summonerids:
        id = id.strip()
        #gets puuid
        url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/{id}"
        data = json.loads(requests.get(url, headers = {"X-Riot-Token" : token}).text) #data of summoner
        if 'puuid' not in data:
            continue
        puuid = data['puuid']

        #gets match ids
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
        data = json.loads(requests.get(url, headers = {"X-Riot-Token" : token}).text) #list of match ids
        for match in data:
            match_ids[match] = 1
        print(f'added {data}')
        count += 1 #keep track of how many summoners have been added
        print(f'{len(summonerids) - count} summoners left')
        # time.sleep(3/len(tokens))``
        time.sleep(3)

    f = open("match_ids.txt", "w")
    for id in match_ids:
        f.write(id + "\n")
    f.close()

#find_match_ids()

def make_match_data():
    f = open("match_ids.txt", "r")
    match_ids = f.readlines()
    f.close()
    count = 0
    for id in match_ids:
        id = id.strip()
        url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{id}"
        data = json.loads(requests.get(url, headers = {"X-Riot-Token" : token}).text) #data of match
        
        # writes data to json file
        f = open("match_data.json", "a")
        if (count == 0):
            f.write('{\n')
        elif (count == len(match_ids) - 1):
            f.write('}\n')
        f.write(f',"{data["metadata"]["matchId"]}": {json.dumps(data, indent=2)}\n') 
        f.close()

        count += 1
        print(f'{count} is the current index of match_ids')
        time.sleep(1.3)

make_match_data()

# example of how to read json file
# with open('match_data.json') as f:
#     file_stuff = f.read()

# parsed_data = json.loads(file_stuff)
# print(parsed_data['NA1_4647099839'])