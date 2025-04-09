from flask import render_template 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db
from model import db, User

app = Flask(__name__)

# Configuration de la base de données SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app)

@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/cameras")
def cameras():
    categories = {
        "Amateur": [
            {"marque": "Canon", "modele": "EOS 2000D", "date": "2019", "score": 3},
            {"marque": "Nikon", "modele": "D3500", "date": "2020", "score": 4}
        ],
        "Amateur sérieux": [
            {"marque": "Sony", "modele": "Alpha 6400", "date": "2021", "score": 4}
        ],
        "Professionnel": [
            {"marque": "Canon", "modele": "EOS R5", "date": "2022", "score": 5}
        ]
    }
    return render_template('cameras.html', categories=categories)


@app.route('/telescopes')
def telescopes():
    categories = {
        "Enfants": [
            {"marque": "Celestron", "modele": "FirstScope", "date": "2018", "score": 3}
        ],
        "Automatisés": [
            {"marque": "SkyWatcher", "modele": "Virtuoso", "date": "2021", "score": 4}
        ],
        "Complets": [
            {"marque": "Orion", "modele": "XT10", "date": "2020", "score": 5}
        ]
    }
    return render_template('telescopes.html', categories=categories)


@app.route('/photographies')
def photos():
    photos = [
        {"titre": "Photo 1", "auteur": "Mehdi", "année": "2021"},
        {"titre": "Le Soleil", "auteur": "Terry Davis", "année": "2022"},
    ]
    return render_template('photos.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route('/add')
def add_data():
    # Ajouter un utilisateur
    user = User(username='john_doe', email='john@example.com', password='12345')
    db.session.add(user)

    # Valider les ajouts dans la base
    db.session.commit()
    return 'Data added!'




