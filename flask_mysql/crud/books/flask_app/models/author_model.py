from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import book_model


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL(DATABASE).query_db(query)
        all_authors = []
        for row_from_db in results:
            author_instance = cls(row_from_db)
            all_authors.append(author_instance)
        return all_authors

    @classmethod
    def get_one_with_favorites(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            author_instance = cls(results[0])
            books_list = []
            for row_from_db in results:
                book_data = {
                    'id': row_from_db['books.id'],
                    'title': row_from_db['title'],
                    'num_of_pages': row_from_db['num_of_pages'],
                    'created_at': row_from_db['books.created_at'],
                    'updated_at': row_from_db['books.updated_at'],
                }
                book_instance = book_model.Book(book_data)
                books_list.append(book_instance)
            author_instance.favorites = books_list
            return author_instance
        return results

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL(DATABASE).query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def create(cls,data):
        query = "INSERT INTO authors (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)


    # @classmethod
    # def get_one(cls,data):
    #     query = "SELECT * FROM authors WHERE id = %(id)s"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     if len(results) > 0:
    #         return cls(results[0])
    #     return False