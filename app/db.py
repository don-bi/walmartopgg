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

        c.execute('''CREATE TABLE table_name (
                all_in_pings INTEGER,
                assist_me_pings INTEGER,
                assists INTEGER,
                bait_pings INTEGER,
                baron_kills INTEGER,
                basic_pings INTEGER,
                bounty_level INTEGER,
                challenges BLOB,
                champ_experience INTEGER,
                champ_level INTEGER,
                champion_id INTEGER,
                champion_name TEXT,
                champion_transform TEXT,
                command_pings INTEGER,
                consumables_purchased INTEGER,
                damage_dealt_to_buildings INTEGER,
                damage_dealt_to_objectives INTEGER,
                damage_dealt_to_turrets INTEGER,
                damage_self_mitigated INTEGER,
                danger_pings INTEGER,
                deaths INTEGER,
                detector_wards_placed INTEGER,
                double_kills INTEGER,
                dragon_kills INTEGER,
                eligible_for_progression INTEGER,
                enemy_missing_pings INTEGER,
                enemy_vision_pings INTEGER,
                first_blood_assist INTEGER,
                first_blood_kill INTEGER,
                first_tower_assist INTEGER,
                first_tower_kill INTEGER,
                game_ended_in_early_surrender INTEGER,
                game_ended_in_surrender INTEGER,
                get_back_pings INTEGER,
                gold_earned INTEGER,
                gold_spent INTEGER,
                hold_pings INTEGER,
                individual_position TEXT,
                inhibitor_kills INTEGER,
                inhibitor_takedowns INTEGER,
                inhibitors_lost INTEGER,
                item0 INTEGER,
                item1 INTEGER,
                item2 INTEGER,
                item3 INTEGER,
                item4 INTEGER,
                item5 INTEGER,
                item6 INTEGER,
                items_purchased INTEGER,
                killing_sprees INTEGER,
                kills INTEGER,
                lane TEXT,
                largest_critical_strike INTEGER,
                largest_killing_spree INTEGER,
                largest_multi_kill INTEGER,
                longest_time_spent_living INTEGER,
                magic_damage_dealt INTEGER,
                magic_damage_dealt_to_champions INTEGER,
                magic_damage_taken INTEGER,
                need_vision_pings INTEGER,
                neutral_minions_killed INTEGER,
                nexus_kills INTEGER,
                nexus_lost INTEGER,
                nexus_takedowns INTEGER,
                objectives_stolen INTEGER,
                objectives_stolen_assists INTEGER,
                on_my_way_pings INTEGER,
                participant_id INTEGER,
                penta_kills INTEGER,
                perks TEXT,
                physical_damage_dealt INTEGER,
                physical_damage_dealt_to_champions INTEGER,
                physical_damage_taken INTEGER,
                profile_icon INTEGER,
                push_pings INTEGER,
                puuid TEXT,
                quadra_kills INTEGER,
                riot_id_name TEXT,
                riot_id_tagline TEXT,
                role TEXT,
                sight_wards_bought_in_game INTEGER,
                spell1_casts INTEGER,
                spell2_casts INTEGER,
                spell3_casts INTEGER,
                spell4_casts INTEGER,
                summoner1_casts INTEGER,
                summoner1_id INTEGER,
                summoner2_casts INTEGER,
                summoner2_id INTEGER,
                summoner_id TEXT,
                summoner_level INTEGER,
                summoner_name TEXT,
                team_early_surrendered INTEGER,
                team_id INTEGER,
                team_position TEXT,
                time_ccing_others INTEGER,
                time_played INTEGER,
                total_ally_jungle_minions_killed INTEGER,
                total_damage_dealt INTEGER,
                total_damage_dealt_to_champions INTEGER,
                total_damage_shielded_on_teammates INTEGER,
                total_damage_taken INTEGER,
                total_enemy_jungle_minions_killed INTEGER,
                total_heal INTEGER,
                total_heals_on_teammates INTEGER,
                total_minions_killed INTEGER,
                total_time_cc_dealt INTEGER,
                total_time_spent_dead INTEGER,
                total_units_healed INTEGER,
                triple_kills INTEGER,
                true_damage_dealt INTEGER,
                true_damage_dealt_to_champions INTEGER,
                true_damage_taken INTEGER,
                turret_kills INTEGER,
                turret_takedowns INTEGER,
                turrets_lost INTEGER,
                unreal_kills INTEGER,
                vision_cleared_pings INTEGER,
                vision_score INTEGER,
                vision_wards_bought_in_game INTEGER,
                wards_killed INTEGER,
                wards_placed INTEGER,
                win TEXT)''')
    db.commit()
    c.close()

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
    

get_participant_data_names()

# def create_user(username, password):
#     c = db_connect()
#     c.execute('INSERT INTO users(username, password, Did_Questions) VALUES (?, ?, ?);', (username, password, False))
#     c.execute('INSERT INTO grassmeter(Quiz_Grass, Grass, Game_Grass) VALUES (?, ?, ?);', (0, 0, 0))
#     db.commit()
#     #db_close() Dont know what exactly the problem is but dont uncomment this for signup to work