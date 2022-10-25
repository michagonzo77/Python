from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user_model import User
from flask import flash

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_user():
    if not User.validator(request.form):
        return redirect('/')
    User.create(request.form)
    session['email'] = request.form['email']
    return redirect('/success')

@app.route("/success")
def success():
    # call the get all classmethod to get all users
    all_users = User.get_all()
    print(all_users)
    return render_template("success.html", all_users = all_users)


@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = { 'id' : id }
    User.delete(data)
    return redirect('/success')