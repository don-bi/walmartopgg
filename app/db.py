import sqlite3
import random, os, ujson as json, time, pprint as pp
from collections import Counter
import requests

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
               onMyWayPings INT,participantId INT,pentaKills INT,perks BLOB,physicalDamageDealt INT,physicalDamageDealtToChampions INT,physicalDamageTaken INT,
               profileIcon INT,pushPings INT,puuid TEXT,quadraKills INT,riotIdName TEXT,riotIdTagline TEXT,role TEXT,
               sightWardsBoughtInGame INT,spell1Casts INT,spell2Casts INT,spell3Casts INT,spell4Casts INT,summoner1Casts INT,summoner1Id INT,summoner2Casts INT,summoner2Id INT,
               summonerId TEXT,summonerLevel INT,summonerName TEXT,teamEarlySurrendered INT,teamId INT,teamPosition TEXT,timeCCingOthers INT,timePlayed INT,totalAllyJungleMinionsKilled INT,
               totalDamageDealt INT,totalDamageDealtToChampions INT,totalDamageShieldedOnTeammates INT,totalDamageTaken INT,totalEnemyJungleMinionsKilled INT,totalHeal INT,totalHealsOnTeammates INT,totalMinionsKilled INT,
               totalTimeCCDealt INT,totalTimeSpentDead INT,totalUnitsHealed INT,tripleKills INT,trueDamageDealt INT,trueDamageDealtToChampions INT,trueDamageTaken INT,turretKills INT,turretTakedowns INT,
               turretsLost INT,unrealKills INT,visionClearedPings INT,visionScore INT,visionWardsBoughtInGame INT,wardsKilled INT,wardsPlaced INT,win INT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS champions(championName TEXT, role TEXT, winRate INT, kills INT, deaths INT, assists INT, commonSpell1 INT, commonSpell2 INT,
    item1 INT, item2 INT, item3 INT, item4 INT, item5 INT, item6 INT, gameDuration INT, cs INT, dmgTaken INT, dmgDealt INT, runes BLOB)''')
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
        print(matchId)
    db_close()

def insert_match_data():
    c = db_connect()
    for matchId in parsed_data:
        match_data = parsed_data[matchId]['info']
        query = "INSERT INTO matches VALUES (" + '?,' * 14 + '?)'
        c.execute(query, [str(matchId), match_data['gameDuration'], match_data['teams'][0]['win'], match_data['teams'][0]['objectives']['champion']['kills'], match_data['teams'][0]['objectives']['baron']['kills'], match_data['teams'][0]['objectives']['dragon']['kills'], match_data['teams'][0]['objectives']['inhibitor']['kills'], match_data['teams'][0]['objectives']['riftHerald']['kills'], match_data['teams'][0]['objectives']['tower']['kills'], match_data['teams'][1]['objectives']['champion']['kills'], match_data['teams'][1]['objectives']['baron']['kills'], match_data['teams'][1]['objectives']['dragon']['kills'], match_data['teams'][1]['objectives']['inhibitor']['kills'], match_data['teams'][1]['objectives']['riftHerald']['kills'], match_data['teams'][1]['objectives']['tower']['kills']])
    db_close()
    


# print sqlite table
def print_sqlite_table(table_name):
    c = db_connect()
    c.execute('SELECT * FROM ' + table_name)
    data = c.fetchall()
    db_close()
    return data

# get list of all champ names in db
def get_champ_names():
    c = db_connect()
    c.execute('SELECT DISTINCT championName FROM participants;')
    data = list(map(''.join, c.fetchall()))
    db_close()
    return data

# get winrate for a champ by role. Use sql query to find average of win column
def champ_wr_specific(champion, role):
    c = db_connect()
    c.execute('''SELECT AVG(win) FROM participants 
             WHERE championName=? AND individualPosition=?''', (champion, role))
    wr = c.fetchone()[0]
    return wr * 100 if wr else None
# get most common item build for a champ by role
def most_common_items_specific(champion, role):
    c = db_connect()
    c.execute('''SELECT item1, item2, item3, item4, item5, item6 FROM participants 
             WHERE championName=? AND individualPosition=?''', (champion, role))
    items = c.fetchall()
    counter = Counter(item for row in items for item in row)
    return [i[0] for i in counter.most_common(6)] + [None] * (6 - len(counter))

#get most common summoner spells for a champ by role
def most_common_spells_specific(champion, role):
    c = db_connect()
    c.execute('''SELECT summoner1Id, summoner2Id FROM participants 
             WHERE championName=? AND individualPosition=?''', (champion, role))
    spells = c.fetchall()
    counter = Counter(spell for row in spells for spell in row)
    return [i[0] for i in counter.most_common(2)] + [None] * (2 - len(counter))

#get most common runes for a champ by role
def most_common_runes_specific(champion, role):
    c = db_connect()
    c.execute('''SELECT perks FROM participants 
             WHERE championName=? AND individualPosition=?''', (champion, role))
    ret = c.fetchall()
    counter = Counter(item for row in ret for item in row)
    return counter.most_common(1)[0][0] if counter else None

#get kda for a champ by role
def champ_kda_specific(champion, role):
    c = db_connect()
    c.execute('''SELECT AVG(kills), AVG(deaths), AVG(assists) FROM participants 
             WHERE championName=? AND individualPosition=?''', (champion, role))
    return c.fetchone()

#get average game duration for a champ by role
def avg_game_duration_specific(champion, role):
    c = db_connect()
    c.execute('''SELECT AVG(timePlayed) FROM participants 
             WHERE championName=? AND individualPosition=?''', (champion, role))
    return c.fetchone()[0]

#calculate cs for a champ by role
def get_cs_specific(champion, role):
    c = db_connect()
    c.execute('''SELECT SUM(totalMinionsKilled) FROM participants 
             WHERE championName=? AND individualPosition=?''', (champion, role))
    minionsKilled = c.fetchone()[0]

    c.execute('''SELECT SUM(timePlayed) FROM participants 
             WHERE championName=? AND individualPosition=?''', (champion, role))
    time = c.fetchone()[0]
    if minionsKilled == None or time == None: return None
    return minionsKilled / time

# get avg dmgtaken for a champ by role
def avg_dmgtaken_specific(champion, role):
    c = db_connect()
    c.execute('''SELECT AVG(totalDamageTaken) FROM participants 
             WHERE championName=? AND individualPosition=?''', (champion, role))
    return c.fetchone()[0]

# get avg taken for a champ disregarding role
def avg_dmgtaken(champion):
    c = db_connect()
    c.execute('''SELECT AVG(totalDamageTaken) FROM participants 
             WHERE championName=?''', [champion])
    return c.fetchone()[0]

# get avg dmgdealt for a champ by role
def avg_dmgdealt_specific(champion, role):
    c = db_connect()
    c.execute('''SELECT AVG(totalDamageDealtToChampions) FROM participants 
             WHERE championName=? AND individualPosition=?''', (champion, role))
    return c.fetchone()[0]

# get avg dmgdealt for a champ disregarding role
def avg_dmgdealt(champion):
    c = db_connect()
    c.execute('''SELECT AVG(totalDamageDealtToChampions) FROM participants 
             WHERE championName=?''', [champion])
    return c.fetchone()[0]


#calculate cs for a champ disregarding role
def get_cs(champion):
    c = db_connect()
    c.execute('''SELECT SUM(totalMinionsKilled) FROM participants 
             WHERE championName=?''', [champion])
    minionsKilled = c.fetchone()[0]

    c.execute('''SELECT SUM(timePlayed) FROM participants 
             WHERE championName=?''', [champion])
    time = c.fetchone()[0]
    if minionsKilled == None or time == None: return None
    return minionsKilled / time

# get winrate for a champ regardless of role
def champ_wr(champion):
    c = db_connect()
    c.execute('''SELECT AVG(win) FROM participants 
             WHERE championName=?''', [champion])
    wr = c.fetchone()[0]
    return wr * 100 if wr else None


# get most common item build for a champ regardless of role
def most_common_items(champion):
    c = db_connect()
    c.execute('''SELECT item1, item2, item3, item4, item5, item6 FROM participants 
             WHERE championName=?''', [champion])
    ret = c.fetchall()
    counter = Counter(item for row in ret for item in row)
    return [i[0] for i in counter.most_common(6)] + [None] * (6 - len(counter))


# get most common summoner spells for a champ regardless of role
def most_common_spells(champion):
    c = db_connect()
    c.execute('''SELECT summoner1Id, summoner2Id FROM participants 
             WHERE championName=?''', [champion])
    ret = c.fetchall()
    counter = Counter(item for row in ret for item in row)
    return [i[0] for i in counter.most_common(2)] + [None] * (2 - len(counter))

# get most common runes for a champ regardless of role
def most_common_runes(champion):
    c = db_connect()
    c.execute('''SELECT perks FROM participants 
             WHERE championName=?''', [champion])
    ret = c.fetchall()
    counter = Counter(item for row in ret for item in row)
    return counter.most_common(1)[0][0] if counter else None

# get kda for a champ regardless of role
def champ_kda(champion):
    c = db_connect()
    c.execute('''SELECT AVG(kills), AVG(deaths), AVG(assists) FROM participants 
             WHERE championName=?''', [champion])
    return c.fetchone()

# get average game duration for a champ regardless of role
def avg_game_duration(champion):
    c = db_connect()
    c.execute('''SELECT AVG(timePlayed) FROM participants 
             WHERE championName=?''', [champion])
    return c.fetchone()[0]


#insert general champion data into database
def insert_champ_data():
    lst = get_champ_names()
    for champ in lst:
        items = most_common_items(champ)
        winrate = champ_wr(champ)
        spells = most_common_spells(champ)
        runes = most_common_runes(champ)
        kda = champ_kda(champ)
        game_duration = avg_game_duration(champ)
        c = db_connect()
        query = "INSERT INTO champions VALUES (" + '?,' * 18 + '?)'
        c.execute(query, (champ, 'ALL', winrate, kda[0], kda[1], kda[2], spells[0], spells[1], items[0], items[1], items[2], items[3], items[4], items[5], game_duration, get_cs(champ), avg_dmgtaken(champ), avg_dmgdealt(champ), runes))
        db_close()
    

#insert champion data into database
def insert_champ_data_by_roles():
    lst = get_champ_names()
    for champ in lst:
         for role in ['TOP', 'JUNGLE', 'MIDDLE', 'BOTTOM', 'UTILITY']:
            items = most_common_items_specific(champ, role)
            winrate = champ_wr_specific(champ, role)
            spells = most_common_spells_specific(champ, role)
            runes = most_common_runes_specific(champ, role)
            kda = champ_kda_specific(champ, role)
            game_duration = avg_game_duration_specific(champ, role)
            cs = get_cs_specific(champ, role)
            dmgtaken = avg_dmgtaken_specific(champ, role)
            dmgdealt = avg_dmgdealt_specific(champ, role)
            c = db_connect()
            query = "INSERT INTO champions VALUES (" + '?,' * 18 + '?)'
            c.execute(query, (champ, role, winrate, kda[0], kda[1], kda[2], spells[0], spells[1], items[0], items[1], items[2], items[3], items[4], items[5], game_duration, cs, dmgtaken, dmgdealt, runes))
            db.commit()
            db_close()
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
        pos = participant['teamPosition'] 
        if pos == "TOP":
            key_string += "Top"
        elif pos == "JUNGLE":
            key_string += "Jungle"
        elif pos == "MIDDLE":
            key_string += "Middle"
        elif pos == "BOTTOM":
            key_string += "Bottom"
        elif pos == "UTILITY":
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

def convert_item_id(item_id):
    # Make a request to the Data Dragon to get the item data
    url = 'http://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/item.json'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        item_data = data['data']
        if str(item_id) in item_data:
            item_info = item_data[str(item_id)]
            item_name = item_info['name']
            image_link = f"http://ddragon.leagueoflegends.com/cdn/13.9.1/img/item/{item_id}.png"
            return (item_name, image_link)
        else:
            return None, None
    else:
        return None, None

def get_spell_images():
    # Make a request to the Data Dragon to get the summoner spell data
    url = 'http://ddragon.leagueoflegends.com/cdn/13.9.1/data/en_US/summoner.json'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        temp_data = data['data']
        spell_data = {}
        for key in temp_data:
            spell_data[temp_data[key]['key']] = temp_data[key]['image']['full']
        return spell_data
    else:
        return None

def get_champ_names_fast():
    c = db_connect()
    c.execute('SELECT DISTINCT championName FROM champions;')
    data = list(map(''.join, c.fetchall()))
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