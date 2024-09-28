<img src="./public/Screenshot 2024-09-28 002937.png" alt="Home" width="400px">

# Walmart OP.GG
Donald Bi (Data+DB), Yat Long Chan (Flask App), David Deng (HTML + JS), Jacob Guo (CSS + Bootstrap)

Desc: This site will have a landing page that shows different graphs of winner stats vs. loser stats so the user can analyze how to win. Then we'll have a button to show a random match, displaying the different participants and also the statistics of the match. There'll be ways to view each participant, and by clicking them, a detailed description of the participant's performance in that game will appear. We're also planning to add a bookmark feature for matches that the user wants to keep. There'll also be a way to search for champion stats based on the matches (first bloods, pentakills, etc...). All the data is gathered using the RIOT api to ensure recency in the dataset.

Riot Api: https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_riotAPI.md

# Launch Codes:

Step 0: Clone our repository 

    git clone git@github.com:don-bi/gwoblins.git

Step 1: Change directory into our repository

    cd gwoblins

Step 2: Run the Flask Server

    python3 app/__init__.py

Step 3: Open the link to the local host

    http://127.0.0.1:5000
or go to\
~~https://lol.ychan.tech~~ (deprecated)

# Data:

Desc: Our dataset contains 17,000+ matches of League of Legends games that contains information such as each team's kills, monster kills, turret kills, etc.

Source: We used the RIOT api to gather this data through Python. Then we parsed the data into a json file.
Final Source: https://www.kaggle.com/datasets/vokainodra/league-of-legends-high-elo-match-data-patch-139
