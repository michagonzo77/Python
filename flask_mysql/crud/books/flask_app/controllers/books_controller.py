from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book

@app.route("/books/new")
def all_books():
    all_books = Book.get_all()
    return render_template("all_books.html", all_books = all_books)

@app.route('/books/create', methods=['POST'])
def created_book():
    Book.create(request.form)
    return redirect('/books/new')

@app.route('/books/<int:id>')
def get_one_book(id):
    data = { 'id': id }
    book = Book.get_one_book_favorites(data)
    author = Author.get_all()
    exclude = Author.unfavorited_authors(data)
    return render_template("one_book.html", book = book, author = author, exclude = exclude)

@app.route('/join/author', methods=['POST'])
def join_author():
    Author.add_favorite(request.form)
    id = request.form['book_id']
    return redirect(f'/books/{id}')