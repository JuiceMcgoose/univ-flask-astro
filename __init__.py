from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://db.sqlite'

    db.init_app(app)

    #blueprint for auth routes of the app
    from .auth import auth as auth_blueprint

    #blueprint for non-auth part of the app
    from app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #create table when app is launched
    with app.app_context():
        db.create_all()

    return app
