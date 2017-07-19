import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash


app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'database'),
))

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

@app.route('/')
def index():
    try:
        page = request.args['page']
    except:
        page = 'login.html'
    return render_template('base.html', page='static/{}'.format(page))

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/login_page')
def login_page():
    return render_template('login.html')


# start the app
if __name__ == '__main__':
    app.run()
