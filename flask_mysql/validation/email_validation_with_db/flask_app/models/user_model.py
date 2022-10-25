from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_users = []
        for row_from_db in results:
            all_users.append( cls(row_from_db) )
        return all_users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) > 0:
            return cls(results[0])
        return False

    @staticmethod
    def validator(user):
        is_valid = True
        user_in_db = User.get_by_email({'email':user['email']})
        if user_in_db:
            flash("Email already registered!", "email")
            is_valid = False
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Email is not valid!", "email")
            is_valid = False
        return is_valid


    @classmethod
    def delete(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)