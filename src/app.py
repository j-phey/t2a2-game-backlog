# Adding imports for Flask, SQLAlchemy, etc.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

# Initialising the app
app = Flask(__name__)
# Setting the database URI via SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://dev:123456@localhost:5432/game_tracker"

# Creating the database object 'db'
db = SQLAlchemy(app)

# -- MODELS --
# Create the models, which are classes that allow object creation and creates the structure that will be used as a table and its rows in the database.
class Games(db.Model):
    # define the table name for the db
    __tablename__= "games"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)
    # Add the rest of the attributes. 
    title = db.Column(db.String())
    description = db.Column(db.String())
    release_date = db.Column(db.Date())
    platform = db.Column(db.String())
    genre = db.Column(db.String())

# -- CLI COMMANDS --

# CLI command that creates the database (db)
@app.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

# Seed game entries into the 'games' table
@app.cli.command("seed")
def seed_db():
    # from datetime import date
    # Creating the first game object
    game1 = Games(
      # Setting the attributes, but excluding the id as SQLAlchemy manages that
      title = "World of Warcraft",
      description = "A massive online game set in Azeroth",
      release_date = "2004-11-23",
      platform = "PC",
      genre = "MMORPG"
    )
    # Adding the object as a new row to the 'games' table
    db.session.add(game1)
    
    # Creating the second game object
    game2 = Games(
      title = "Rainbow Six Siege",
      description = "Online tactical shooter",
      release_date = "2015-12-01",
      platform = "PS4",
      genre = "FPS"
    )
    # Adding the object as a new row to the 'games' table
    db.session.add(game2)

    # Commiting the changes
    db.session.commit()
    print("Table seeded")

# CLI Command for dropping the tables 

@app.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 