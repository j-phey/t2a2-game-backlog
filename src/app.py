# Adding imports for Flask, SQLAlchemy, etc.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

# Initialising the app
app = Flask(__name__)
# Setting the database URI via SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://db_dev:123456@localhost:5432/trello_clone_db"

# Creating the database object 'db'
db = SQLAlchemy(app)