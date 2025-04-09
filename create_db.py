from app import app
from model import db

# Créer une instance de l'application Flask
app = app()

# Crée les tables dans la base de données
with app.app_context():
    db.create_all()

print("Database and tables created!")

