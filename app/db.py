import sqlite3
import random

DB_FILE = "database.db"

db = None
db = sqlite3.connect(DB_FILE)
c = db.cursor()

# parse data from json
with open('match_data.json') as f:
    file_stuff = f.read()
parsed_data = json.loads(file_stuff)

for match in parsed_data:
    

# dataset
c.execute("CREATE TABLE if not Exists users(ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, Did_Questions BOOLEAN);")

c.execute("CREATE TABLE if not Exists game(ID INTEGER, Game TEXT, Game_Username TEXT);")
its = ["You probably live in your parents' basement@@", "Looks like all the grass you have touched were digital!@@", "This could go either way, what are you really?@@", "Are you too poor to afford a computer? Or are you lying on the quizes?@@", "You green as nature!@@"]
c.execute('INSERT or IGNORE INTO insult(lv5, lv4, lv3, lv2, lv1) VALUES (?, ?, ?, ?, ?);', (its[0], its[1], its[2], its[3],its[4]))
db.commit()
c.close()

def db_connect():
    global db
    db = sqlite3.connect(DB_FILE)
    return db.cursor()

def db_close():
    db.commit()
    db.close()

# def create_user(username, password):
#     c = db_connect()
#     c.execute('INSERT INTO users(username, password, Did_Questions) VALUES (?, ?, ?);', (username, password, False))
#     c.execute('INSERT INTO grassmeter(Quiz_Grass, Grass, Game_Grass) VALUES (?, ?, ?);', (0, 0, 0))
#     db.commit()
#     #db_close() Dont know what exactly the problem is but dont uncomment this for signup to work