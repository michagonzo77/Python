from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo_model import Dojo

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_user():
    if not Dojo.validator(request.form):
        return redirect('/')
    Dojo.create(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')         
def show_info():
    return render_template("results.html")