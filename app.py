from flask import Flask
from flask import Blueprint, render_template

app = Flask(__name__)

main = Blueprint('main', __name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/another_one")
def another():
    return render_template('another.html')

@app.route("/profile")
def profile_page():
    return render_template('profile.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')
