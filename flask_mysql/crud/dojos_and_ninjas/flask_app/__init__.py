from flask import Flask
app = Flask(__name__)
app.secret_key = "Ravioli, Ravioli, give me the Formuoli"

DATABASE = "dojos_and_ninjas_schema"