from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user_model import User

@app.route("/")
def read_all_users():
    # call the get all classmethod to get all users
    all_users = User.get_all()
    print(all_users)
    return render_template("read_all_users.html", all_users = all_users)

@app.route('/users/new') # Route to create user form
def new_user_form():
    return render_template("create_user.html")

@app.route("/users/create", methods=['POST']) #Route to retrieve information from form on create_user
def create_user():
    id = User.create(request.form)
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>/')
def show_one(id):
    data = { 'id': id }
    user = User.get_one(data)
    return render_template("read_one.html", user = user)

@app.route('/users/<int:id>')
def get_one(id):
    data = { 'id': id }
    user = User.get_one(data)
    return render_template("read_one.html", one_user = user)

@app.route('/users/<int:id>/edit')
def edit_user_form(id):
    data = { 'id': id }
    user = User.get_one(data)
    return render_template('edit_user.html', user = user)

@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        # 'name' = request.form['name']
        **request.form,
        'id': id
    }
    User.update(data)
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = { 'id' : id }
    User.delete(data)
    return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"