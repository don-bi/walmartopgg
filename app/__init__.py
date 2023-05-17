from flask import Flask, request, session, redirect, render_template
import db
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/random', methods=['POST'])
def random():
    id = db.get_random_id()[0]
    print(id)
    return redirect('/match/' + str(id))
    

@app.route('/match/<match_id>', methods=['GET'])
def match(match_id):
    match_data = db.get_match_data(match_id)
    participant_data = db.get_match_participant_data(match_id)
    positions = [['blueTop', 'blueJungle', 'blueMiddle', 'blueBottom', 'blueSupport'], 
                 ['redTop', 'redJungle', 'redMiddle', 'redBottom', 'redSupport']]
    print(participant_data)
    return render_template('match.html', match_id=match_id, match_data=match_data, participant_data=participant_data, positions=positions)


if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)
    db_path = os.path.join(current_dir, 'database.db')
    if not os.path.exists(db_path):
        db.make_database()
        db.insert_participant_data()
        db.insert_match_data()
    app.debug = True
    app.run(host='0.0.0.0')
