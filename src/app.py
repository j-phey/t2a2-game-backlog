# Adding imports for Flask, SQLAlchemy, etc.
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow # Importing for serialisation

# Initialising the app
app = Flask(__name__)
ma = Marshmallow(app)

# Setting the database URI via SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://dev:123456@localhost:5432/game_tracker"

# Creating the database object 'db'
db = SQLAlchemy(app)

# -- MODELS --
# Create the models, which are classes that allow object creation and creates the structure that will be used as a table and its rows in the database.

class Game(db.Model):
    # Defining the table name for the db
    __tablename__= "games"
    # Setting the primary key and defining each attribute as a column in the db table using the 'db' object earlier
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    release_date = db.Column(db.Date())
    platform = db.Column(db.String())
    genre = db.Column(db.String())

#creating the Game Schema with Marshmallow for serialisation. Coverting the data into JSON.

class GameSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description", "release_date", "platform", "genre")

# Single game schema, when one game needs to be retrieved
card_schema = GameSchema()

# Multiple game schema, when many games need to be retrieved
cards_schema = GameSchema(many=True)

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
    game1 = Game(
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
    game2 = Game(
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

# -- ROUTES --

# Route: Root / home page (may not be required)

@app.route("/")
def hello():
  return "Hello World!"

# Route: GET /games

@app.route("/games", methods=["GET"])
def get_games():
    # Get all the games from the database
    stmt = db.select(Game)
    games = db.session.scalars(stmt)
    # Converting the games from the database into a JSON format and storing them in 'result'
    result = cards_schema.dump(games)
    #returning the result in JSON format
    return jsonify(result)