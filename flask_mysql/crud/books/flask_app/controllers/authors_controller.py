from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book

@app.route('/')
def all_authors():
    all_authors = Author.get_all()
    return render_template("all_authors.html", all_authors = all_authors)

@app.route('/authors/<int:id>')
def get_one(id):
    data = { 'id': id }
    author = Author.get_one_with_favorites(data)
    exclude = Book.unfavorited_books(data)
    book = Book.get_all()
    return render_template("one_author.html", author = author, book = book, exclude = exclude)

@app.route('/authors/create', methods=['POST']) # route to process new dojo
def create_author():
    id = Author.create(request.form)
    return redirect(f'/authors/{id}')

@app.route('/join/books', methods=['POST'])
def join_books():
    Author.add_favorite(request.form)
    id = request.form['author_id']
    return redirect(f'/authors/{id}')

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Sorry! No response. Try again.</h1>"