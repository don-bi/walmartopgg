import sqlite3
import random, os, json, time

global DB_FILE
DB_FILE = "database.db"

# parse data from json
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'match_data.json')

with open(file_path) as f:
    file_stuff = f.read()
global parsed_data 
parsed_data = json.loads(file_stuff)

def make_database():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()


    for match in parsed_data:
        c.execute("CREATE TABLE IF NOT EXISTS matches(MATCH_ID TEXT, \
        GAME_DURATION INTEGER, WIN INTEGER, BLUE_CHAMP_KILLS INTEGER, BLUE_BARON_KILLS INTEGER, \
        BLUE_DRAGON_KILLS INTEGER, BLUE_INHIB_KILLS INTEGER, BLUE_TOWER_KILLS INTEGER, \
        BLUE_HERALD_KILLS INTEGER, BLUE_TOWER_KILLS INTEGER, RED_CHAMP_KILLS, RED_BARON_KILLS INTEGER, \
        RED_DRAGON_KILLS INTEGER, RED_INHIB_KILLS INTEGER, RED_TOWER_KILLS INTEGER, \
        RED_HERALD_KILLS INTEGER, RED_TOWER_KILLS INTEGER);")

        c.execute("CREATE TABLE IF NOT EXISTS participants(matchId TEXT, \
        assists INTEGER, baronKills INTEGER, bountyLevel INTEGER, champExperience INTEGER, champLevel INTEGER, \
        championId INTEGER, championName TEXT, consumablesPurchased INTEGER, damageDealtToBuildings INTEGER, \
        damageDealtToObjectives INTEGER, damageDealtToTurrets INTEGER, damageSelfMitigated INTEGER, deaths INTEGER, \
        detectorWardsPlaced INTEGER, doubleKills INTEGER, dragons INTEGER, firstBloodAssist INTEGER, \
        firstBloodKill INTEGER, firstTowerAssist INTEGER, firstTowerKill INTEGER, gameEndedInEarlySurrender INTEGER, \
        gameEndedInSurrender INTEGER, goldEarned INTEGER, goldSpent INTEGER, individualPosition STRING, inhibKills INTEGER, \
        inhibTakedowns INTEGER, inhibsLost INTEGER, item0 INTEGER, item1 INTEGER, item2 INTEGER, item3 INTEGER, item4 INTEGER, \
        item5 INTEGER, item6 INTEGER, itemsPurchased INTEGER, killingSprees INTEGER, kills INTEGER, lane STRING, largestCrit INTEGER, \
        largestKillingSpree INTEGER, largestMultikill INTEGER, longestTimeAlive INTEGER, magicDamageDealt INTEGER, \
        magicDamageDealtToChampions INTEGER, magicDamageTaken INTEGER, neutralMinionsKilled INTEGER, nexusKills INTEGER, \
        nexusTakedowns INTEGER, nexusLost INTEGER, objectivesStolen INTEGER, objectivesStolenAssists INTEGER, participantId INTEGER, \
        penta INTEGER, perks BLOB, physDmgDealt INTEGER, physDmgTaken INTEGER, profileIcon INTEGER, puuid STRING, quadKills INTEGER, \
        riotIdName STRING, riotIdTagline STRING, role STRING, sightWardsBought INTEGER, spell1Casts INTEGER, \
        spell2Casts INTEGER, spell3Casts INTEGER, spell4Casts INTEGER, summoner1Casts INTEGER, summoner1Id INTEGER, \
        summoner2Casts INTEGER, summoner2Id INTEGER, summonerId STRING, summonderLevel INTEGER, summonerName STRING, \
        teamEarlySurrender INTEGER, teamId INTEGER, teamPosition STRING, timeCcingOthers INTEGER, timePlayed INTEGER, \
        totalDamageDealt INTEGER, totalDamageDealtToChampions INTEGER, totalDamageShieldedOnTeammates INTEGER, totalDamageTaken INTEGER, \
        totalHeal INTEGER, totalHealsOnTeammates INTEGER, totalMinionsKilled INTEGER, totalTimeCcDealt INTEGER, \
        totalTimeSpentDead INTEGER, totalUnitsHealed INTEGER, tripleKills INTEGER, trueDamageDealt INTEGER, \
        trueDamageDealtToChampions INTEGER, trueDamageTaken INTEGER, turretKills INTEGER, turretTakedowns INTEGER, turretsLost INTEGER, \
        unrealKills INTEGER, visionScore INTEGER, visionWardsBoughtInGame INTEGER, wardsKilled INTEGER, \
        wardsPlaced INTEGER, win INTEGER);")

        c.execute('''CREATE TABLE participants (MATCH_ID TEXT,
                   allInPings INT,assistMePings INT,assists INT,baitPings INT,baronKills INT,basicPings INT,bountyLevel INT,challenges INT,
                   champExperience INT,champLevel INT,championId INT,championName VARCHAR(255),championTransform INT,commandPings INT,consumablesPurchased INT,
                   damageDealtToBuildings INT,damageDealtToObjectives INT,damageDealtToTurrets INT,damageSelfMitigated INT,dangerPings INT,deaths INT,detectorWardsPlaced INT,doubleKills INT,
                   dragonKills INT,eligibleForProgression INT,enemyMissingPings INT,enemyVisionPings INT,firstBloodAssist INT,firstBloodKill INT,firstTowerAssist INT,
                   firstTowerKill INT,gameEndedInEarlySurrender INT,gameEndedInSurrender INT,getBackPings INT,goldEarned INT,goldSpent INT,holdPings INT,
                   individualPosition VARCHAR(255),inhibitorKills INT,inhibitorTakedowns INT,inhibitorsLost INT,item0 INT,item1 INT,item2 INT,
                   item3 INT,item4 INT,item5 INT,item6 INT,itemsPurchased INT,killingSprees INT,kills INT,lane VARCHAR(255),largestCriticalStrike INT,
                   largestKillingSpree INT,largestMultiKill INT,longestTimeSpentLiving INT,magicDamageDealt INT,magicDamageDealtToChampions INT,magicDamageTaken INT,needVisionPings INT,
                   neutralMinionsKilled INT,nexusKills INT,nexusLost INT,nexusTakedowns INT,objectivesStolen INT,objectivesStolenAssists INT,
                   onMyWayPings INT,participantId INT,pentaKills INT,perks VARCHAR(255),physicalDamageDealt INT,physicalDamageDealtToChampions INT,physicalDamageTaken INT,
                   profileIcon INT,pushPings INT,puuid VARCHAR(255),quadraKills INT,riotIdName VARCHAR(255),riotIdTagline VARCHAR(255),role VARCHAR(255),
                   sightWardsBoughtInGame INT,spell1Casts INT,spell2Casts INT,spell3Casts INT,spell4Casts INT,summoner1Casts INT,summoner1Id INT,summoner2Casts INT,summoner2Id INT,
                   summonerId INT,summonerLevel INT,summonerName VARCHAR(255),teamEarlySurrendered INT,teamId INT,teamPosition VARCHAR(255),timeCCingOthers INT,timePlayed INT,totalAllyJungleMinionsKilled INT,
                   totalDamageDealt INT,totalDamageDealtToChampions INT,totalDamageShieldedOnTeammates INT,totalDamageTaken INT,totalEnemyJungleMinionsKilled INT,totalHeal INT,totalHealsOnTeammates INT,totalMinionsKilled INT,
                   totalTimeCCDealt INT,totalTimeSpentDead INT,totalUnitsHealed INT,tripleKills INT,trueDamageDealt INT,trueDamageDealtToChampions INT,trueDamageTaken INT,turretKills INT,turretTakedowns INT,
                   turretsLost INT,unrealKills INT,visionClearedPings INT,visionScore INT,visionWardsBoughtInGame INT,wardsKilled INT,wardsPlaced INT,win VARCHAR(255))''')
    db.commit()
    c.close()

def make_champion_data():
    c.execute('''CREATE TABLE champion_stats (championName TEXT, )''')

def db_connect():
    global db
    db = sqlite3.connect(DB_FILE)
    return db.cursor()

def db_close():
    db.commit()
    db.close()


def get_participant_data_names():
    lst = []
    for data in parsed_data['NA1_4642365867']['info']['participants'][0]:
        lst.append(data)
    print(lst)

# get random matchId from database
def get_random_id():
    c = db_connect()
    c.execute('SELECT matchId FROM match_data ORDER BY RANDOM() LIMIT 1;')
    data = c.fetchone()
    db_close()
    return data

# get participant info for specific match
def get_participant_data(matchId):
    c = db_connect()
    c.execute('SELECT * FROM participants WHERE matchId = ?;', (matchId,))
    data = c.fetchall()
    db_close()
    return data

# get match info for specifc match
def get_match_data(matchId):
    c = db_connect()
    c.execute('SELECT * FROM matches WHERE matchId = ?;', (matchId,))
    data = c.fetchall()
    db_close()
    return data

# def create_user(username, password):
#     c = db_connect()
#     c.execute('INSERT INTO users(username, password, Did_Questions) VALUES (?, ?, ?);', (username, password, False))
#     c.execute('INSERT INTO grassmeter(Quiz_Grass, Grass, Game_Grass) VALUES (?, ?, ?);', (0, 0, 0))
#     db.commit()
#     #db_close() Dont know what exactly the problem is but dont uncomment this for signup to work