from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')         
def landing():
    if "uuid" in session:
        return redirect('/dashboard')
    if "uuid" not in session:
        return render_template("index.html")

@app.route('/users/register', methods=['POST'])
def create_user():
    if not User.validator(request.form):
        return redirect('/')
    hashed = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hashed
    }
    new_id = User.create(data)
    session['uuid'] = new_id
    return redirect('/dashboard')

@app.route('/users/login', methods=['POST'])
def login_user():
    data = {
        'email' : request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Credentials", "log")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Credentials **", "log")
        return redirect('/')
    session['uuid'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dash():
    if not "uuid" in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/users/logout')
def logout():
    del session['uuid']
    return redirect ('/')