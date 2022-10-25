from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL(DATABASE).query_db(query,data)


    @staticmethod
    def validator(potential_dojo):
        print(potential_dojo)
        is_valid = True
        if len(potential_dojo['name']) < 1:
            is_valid = False
            flash("Name is required.", "name")
        if len(potential_dojo['comment']) < 10:
            is_valid = False
            flash("Comment must be at least 10 characters.", "comment")
        if (potential_dojo['location'] == "Choose..."):
            is_valid = False
            flash("Please choose a location.", "location")
        if (potential_dojo['language'] == "Choose..."):
            is_valid = False
            flash("Please choose a language.", "language")

        return is_valid