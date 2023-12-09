from main import db
from flask import Blueprint
from main import bcrypt
from models.games import Game
from models.users import User
from datetime import date

db_commands = Blueprint("db", __name__)

# -- CLI COMMANDS --

# Create app's cli command named create, seed, drop, etc. and the user can run it in the terminal as "flask db create", "flask db seed", etc.
# Invokes the create_db function

# CLI command that creates the database (db)
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Game and User tables created")

# Seed game entries into the 'games' table
@db_commands.cli.command("seed")
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
    print("Game table seeded")

    # Seeding the initial users - one admin and one non-admin
    admin_user = User(
        email = "admin@email.com",
        # Encrypt the password with bcrypt
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        admin = True
    )
    db.session.add(admin_user)

    user1 = User(
        email = "user1@email.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )
    db.session.add(user1)
    
    db.session.commit()
    print("User table seeded") 


# CLI Command for dropping the tables 

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("All tables dropped") 