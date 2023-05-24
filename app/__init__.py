from flask import Flask, request, session, redirect, render_template
import db
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',champ_names = sorted(db.get_champ_names_fast()))

@app.route('/champ/<champ_name>', methods=['GET', 'POST'])
def champ(champ_name): 
    return render_template('champ.html', champ_name=champ_name, 
                           champ_text = db.get_champion_text(champ_name),
                           champ_image = db.get_champion_image(champ_name, 10),
                           champ_data=db.get_champ_data(champ_name),
                           convert_item_id = db.convert_item_id,
                           spell_data = db.get_spell_images(),
                           str = str, round = round,
                           winrates = db.get_avg_winrate(champ_name),
                           rune_data = db.get_rune_data(db.get_champ_data(champ_name)))

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
    position_names = ['Top', 'Jungle', 'Middle', 'Bottom', 'Support']
    return render_template('match.html',str=str, match_id=match_id, match_data=match_data,
     participant_data=participant_data, positions=positions, position_names=position_names,
     convert_item_id = db.convert_item_id, spell_data = db.get_spell_images(),
     champ_data = db.get_total_champ_data())


if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)
    db_path = os.path.join(current_dir, 'database.db')
    if not os.path.exists(db_path):
        db.make_database()
        db.insert_participant_data()
        db.insert_match_data()
        db.insert_champ_data()
        # db.insert_champ_data_by_roles()
    app.debug = True
    app.run(host='0.0.0.0')
