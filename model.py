from flask_sqlalchemy import SQLAlchemy


#configuration de la base de donnees
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


#initialise notre db
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"