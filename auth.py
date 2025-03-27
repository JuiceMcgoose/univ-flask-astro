from flask import Blueprint, render_template, request, redirect, url_for,request_finished,flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = email.form['email']
        password = request.form['password']
        

    return render_template('login.html')


@auth.route("/signup") 
def signup():
    return render_template('signup.html')

@auth.route('/signup',methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    new_user = User(email=email, name=name, password=generate_password_hash(password,method='sha256'))

    if user:
        flash("Email address already exists")
        return redirect(url_for('auth.signup'))

    db.session.add(new_user)
    db.seesion.commit()



@auth.route('/logout')
def logout():
    return 'Logout!'