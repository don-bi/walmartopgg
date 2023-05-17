import sqlite3
import random, os, json, time, pprint as pp

global DB_FILE
current_dir = os.path.dirname(__file__)
DB_FILE = os.path.join(current_dir, 'database.db')

# parse data from json file
file_path = os.path.join(current_dir, 'match_data.json')

with open(file_path) as f:
    file_stuff = f.read()
global parsed_data 
parsed_data = json.loads(file_stuff)

def db_connect():
    global db
    db = sqlite3.connect(DB_FILE)
    return db.cursor()

def db_close():
    db.commit()
    db.close()

def make_database():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()


    c.execute("CREATE TABLE IF NOT EXISTS matches(matchId TEXT, \
    GAME_DURATION INTEGER, WIN INTEGER, BLUE_CHAMP_KILLS INTEGER, BLUE_BARON_KILLS INTEGER, \
    BLUE_DRAGON_KILLS INTEGER, BLUE_INHIB_KILLS INTEGER, \
    BLUE_HERALD_KILLS INTEGER, BLUE_TOWER_KILLS INTEGER, RED_CHAMP_KILLS, RED_BARON_KILLS INTEGER, \
    RED_DRAGON_KILLS INTEGER, RED_INHIB_KILLS INTEGER, \
    RED_HERALD_KILLS INTEGER, RED_TOWER_KILLS INTEGER);")
    
    c.execute('''CREATE TABLE IF NOT EXISTS participants (matchId TEXT,
               allInPings INT,assistMePings INT,assists INT,baitPings INT,baronKills INT,basicPings INT,bountyLevel INT,challenges TEXT,
               champExperience INT,champLevel INT,championId INT,championName TEXT,championTransform INT,commandPings INT,consumablesPurchased INT,
               damageDealtToBuildings INT,damageDealtToObjectives INT,damageDealtToTurrets INT,damageSelfMitigated INT,dangerPings INT,deaths INT,detectorWardsPlaced INT,doubleKills INT,
               dragonKills INT,eligibleForProgression INT,enemyMissingPings INT,enemyVisionPings INT,firstBloodAssist INT,firstBloodKill INT,firstTowerAssist INT,
               firstTowerKill INT,gameEndedInEarlySurrender INT,gameEndedInSurrender INT,getBackPings INT,goldEarned INT,goldSpent INT,holdPings INT,
               individualPosition TEXT,inhibitorKills INT,inhibitorTakedowns INT,inhibitorsLost INT,item0 INT,item1 INT,item2 INT,
               item3 INT,item4 INT,item5 INT,item6 INT,itemsPurchased INT,killingSprees INT,kills INT,lane TEXT,largestCriticalStrike INT,
               largestKillingSpree INT,largestMultiKill INT,longestTimeSpentLiving INT,magicDamageDealt INT,magicDamageDealtToChampions INT,magicDamageTaken INT,needVisionPings INT,
               neutralMinionsKilled INT,nexusKills INT,nexusLost INT,nexusTakedowns INT,objectivesStolen INT,objectivesStolenAssists INT,
               onMyWayPings INT,participantId INT,pentaKills INT,perks TEXT,physicalDamageDealt INT,physicalDamageDealtToChampions INT,physicalDamageTaken INT,
               profileIcon INT,pushPings INT,puuid TEXT,quadraKills INT,riotIdName TEXT,riotIdTagline TEXT,role TEXT,
               sightWardsBoughtInGame INT,spell1Casts INT,spell2Casts INT,spell3Casts INT,spell4Casts INT,summoner1Casts INT,summoner1Id INT,summoner2Casts INT,summoner2Id INT,
               summonerId TEXT,summonerLevel INT,summonerName TEXT,teamEarlySurrendered INT,teamId INT,teamPosition TEXT,timeCCingOthers INT,timePlayed INT,totalAllyJungleMinionsKilled INT,
               totalDamageDealt INT,totalDamageDealtToChampions INT,totalDamageShieldedOnTeammates INT,totalDamageTaken INT,totalEnemyJungleMinionsKilled INT,totalHeal INT,totalHealsOnTeammates INT,totalMinionsKilled INT,
               totalTimeCCDealt INT,totalTimeSpentDead INT,totalUnitsHealed INT,tripleKills INT,trueDamageDealt INT,trueDamageDealtToChampions INT,trueDamageTaken INT,turretKills INT,turretTakedowns INT,
               turretsLost INT,unrealKills INT,visionClearedPings INT,visionScore INT,visionWardsBoughtInGame INT,wardsKilled INT,wardsPlaced INT,win INT)''')

    db.commit()
    c.close()


def insert_participant_data():
    c = db_connect()
    data_keys = get_participant_data_names() #list of all data keys
    
    #insert data for each match
    for matchId in parsed_data: 
        for i in range(len(parsed_data[matchId]['info']['participants'])):
            value_list = []
            for key in data_keys: 
                data_value = parsed_data[matchId]['info']['participants'][i].get(key)
                if (data_value == None):
                    value_list.append(0)
                elif (isinstance(data_value, dict)):
                    value_list.append(str(data_value))
                else:
                    value_list.append(data_value)
            query = "INSERT INTO participants VALUES (" + '?,' * 123 + '?)'
            c.execute(query,[str(matchId)] + value_list)
            
    db_close()

def insert_match_data():
    c = db_connect()
    for matchId in parsed_data:
        match_data = parsed_data[matchId]['info']
        query = "INSERT INTO matches VALUES (" + '?,' * 14 + '?)'
        c.execute(query, [str(matchId), match_data['gameDuration'], match_data['teams'][0]['win'], match_data['teams'][0]['objectives']['champion']['kills'], match_data['teams'][0]['objectives']['baron']['kills'], match_data['teams'][0]['objectives']['dragon']['kills'], match_data['teams'][0]['objectives']['inhibitor']['kills'], match_data['teams'][0]['objectives']['riftHerald']['kills'], match_data['teams'][0]['objectives']['tower']['kills'], match_data['teams'][1]['objectives']['champion']['kills'], match_data['teams'][1]['objectives']['baron']['kills'], match_data['teams'][1]['objectives']['dragon']['kills'], match_data['teams'][1]['objectives']['inhibitor']['kills'], match_data['teams'][1]['objectives']['riftHerald']['kills'], match_data['teams'][1]['objectives']['tower']['kills']])
    db_close()
    

def make_champion_data():
    c.execute('''CREATE TABLE champion_stats (championName TEXT, )''')

# print sqlite table
def print_sqlite_table(table_name):
    c = db_connect()
    c.execute('SELECT * FROM ' + table_name)
    data = c.fetchall()
    db_close()
    return data

# print(print_sqlite_table('participants'))

# get participant data names
def get_participant_data_names():
    lst = []
    for data in parsed_data['NA1_4642365867']['info']['participants'][0]:
        lst.append(data)
    return(lst)


# get random matchId from database
def get_random_id():
    c = db_connect()
    c.execute('SELECT matchId FROM matches ORDER BY RANDOM() LIMIT 1;')
    data = c.fetchone()
    db_close()
    return data

# get participant info for specific match
def get_match_participant_data(matchId):
    c = db_connect()
    db = sqlite3.connect(DB_FILE)
    db.row_factory = sqlite3.Row
    c = db.cursor()
    c.execute('SELECT * FROM participants WHERE matchId = ?;', [matchId])
    data = c.fetchall()
    db_close()
    unfiltered_data = list(map(lambda item:dict(item),data)) #data without team and roles as keys
    filtered_data = {} #data with team and role as keys <team>_<role> (red_support)
    for participant in unfiltered_data:
        # add team to key string
        key_string = ""
        if participant['teamId'] == 100:
            key_string += "blue"
        else:
            key_string += "red"
        
        # add role to key string
        match participant['teamPosition']:
            case "TOP":
                key_string += "Top"
            case "JUNGLE":
                key_string += "Jungle"
            case "MIDDLE":
                key_string += "Middle"
            case "BOTTOM":
                key_string += "Bottom"
            case "UTILITY":
                key_string += "Support"
        
        filtered_data[key_string] = participant
        
    # final output {blueTop: {}, blueJungle: {}, blueBot: {} ...}
    return filtered_data
            
    
    
# get match info for specifc match
def get_match_data(matchId):
    c = db_connect()
    c.execute('SELECT * FROM matches WHERE matchId = ?;', [matchId])
    data = c.fetchall()[0]
    db_close()
    return data

# def create_user(username, password):
#     c = db_connect()
#     c.execute('INSERT INTO users(username, password, Did_Questions) VALUES (?, ?, ?);', (username, password, False))
#     c.execute('INSERT INTO grassmeter(Quiz_Grass, Grass, Game_Grass) VALUES (?, ?, ?);', (0, 0, 0))
#     db.commit()
#     #db_close() Dont know what exactly the problem is but dont uncomment this for signup to work

# make_database()
# insert_match_data()
# insert_participant_data()
# print(get_match_participant_data('NA1_4642365867'))