from flask import Flask, request, session, redirect, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.debug = True
    app.run()