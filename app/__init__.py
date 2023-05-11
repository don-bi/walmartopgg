from flask import Flask, request, session, redirect, render_template
import db

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/random', methods=['GET', 'POST'])
def random():
    id = db.get_random_id()
    return redirect('/match/' + str(id))
    

@app.route('/match/<match_id>', methods=['POST'])
def match(match_id):
    match_data = db.get_match_data(match_id)
    participant_data = db.get_participant_data(match_id)
    return render_template('match.html', match_id=match_id match_data=match_data, participant_data=participant_data)


if __name__ == '__main__':
    app.debug = True
    app.run()