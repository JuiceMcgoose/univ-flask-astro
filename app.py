from flask import render_template, request, flash, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from user_file import users  


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/cameras")
def cameras():
    categories = {
        "Amateur": [
            {"marque": "SonyV2", "modele": "Mehdi c'est bien", "date": "1975", "score": 3},

        ],
        "Amateur sérieux": [
            {"marque": "Sony", "modele": " SonyBX", "date": "2021", "score": 4}
        ],
        "Professionnel": [
            {"marque": "Canon", "modele": "c'est canon", "date": "2022", "score": 5}
        ]
    }
    return render_template('cameras.html', categories=categories)


@app.route('/telescopes')
def telescopes():
    categories = {
        "Enfants": [
            {"marque": "Sony", "modele": "Sony1", "date": "2018", "score": 4}
        ],
        "Automatisés": [
            {"marque": "sdfsdfsdf", "modele": "Samsung2", "date": "2021", "score": 4}
        ],
        "Complets": [
            {"marque": "Samsung", "modele": "1", "date": "2020", "score": 2}
        ]
    }
    return render_template('telescopes.html', categories=categories)


@app.route('/photos', methods=['GET'])
def photos():

    return render_template('photos.html')

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            flash("Your account has beed found !")
        else:
            flash("No account found...")
            render_template('login.html', username=username)
        
    return render_template("login.html")


@app.route("/register",methods=['GET','POST'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash("User already exists!")
        else:
            users[username] = password

            with open("user_file.py", "w") as f:
                f.write(f"users = {users}")
    
            flash(f"Votre compte: {username} avec le mdp {password} a bien ete fait!")
    
    return render_template("register.html")

import sqlite3
from flask import g 
# g est une variable de contexte

DATABASE = 'mydb.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def read_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

