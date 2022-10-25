from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja


@app.route('/')
@app.route('/dojos')
def hello_world():
    all_dojos = Dojo.get_all()
    return render_template("all_dojos.html", all_dojos = all_dojos)

@app.route('/dojos/<int:id>')
def get_one(id):
    data = { 'id': id }
    dojo = Dojo.get_one(data)
    # dojo = dojo.get_one({ 'id': id })
    return render_template("one_dojo.html", dojo=dojo)

@app.route('/dojos/new') # Route to render dojos
def new_dojo_form():
    return render_template("dojos_new.html")

@app.route('/dojos/create', methods=['POST']) # route to process new dojo
def create_dojo():
    Dojo.create(request.form)
    return redirect('/')


@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"