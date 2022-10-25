from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import author_model

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(DATABASE).query_db(query)
        all_books = []
        for row_from_db in results:
            book_instance = cls(row_from_db)
            all_books.append(book_instance)
        return all_books

    @classmethod
    def get_one_book_favorites(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            book_instance = cls(results[0])
            authors_list = []
            for row_from_db in results:
                author_data = {
                    'id': row_from_db['authors.id'],
                    'first_name': row_from_db['first_name'],
                    'last_name': row_from_db['last_name'],
                    'created_at': row_from_db['authors.created_at'],
                    'updated_at': row_from_db['authors.updated_at'],
                }
                author_instance = author_model.Author(author_data)
                authors_list.append(author_instance)
            book_instance.favorites = authors_list
            return book_instance
        return results

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        books = []
        results = connectToMySQL(DATABASE).query_db(query,data)
        for row in results:
            books.append(cls(row))
        return books

    @classmethod
    def create(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL(DATABASE).query_db(query,data)