from main import db
from flask import Blueprint
from main import bcrypt
from models.games import Game
from models.users import User
from models.backlog import Backlog
from models.currently_playing import CurrentlyPlaying
from models.wishlist import Wishlist
from datetime import date

db_commands = Blueprint("db", __name__)

# -- CLI COMMANDS --

# Create app's cli command named create, seed, drop, etc. and the user can run it in the terminal as "flask db create", "flask db seed", etc.
# Invokes the create_db function

# CLI command that creates the database (db)
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("'games', 'users', 'currently_playing', 'backlog', 'wishlist' tables created")

# Seed game entries into the 'games' table
@db_commands.cli.command("seed")
def seed_db():
    from datetime import date
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
    
    # Creating the second game object, etc.
    game2 = Game(
      title = "Rainbow Six Siege",
      description = "Online tactical shooter",
      release_date = "2015-12-01",
      platform = "PS4",
      genre = "FPS"
    )
    # Adding the object as a new row to the 'games' table
    db.session.add(game2)

    game3 = Game(
      title = "Cyberpunk 2077",
      description = "Action RPG set in a dystopian future",
      release_date = "2020-12-10",
      platform = "PS4",
      genre = "RPG"
    )
    # Adding the object as a new row to the 'games' table
    db.session.add(game3)

    game4 = Game(
      title = "The Legend of Zelda: Breath of the Wild",
      description = "Open-world action-adventure in Hyrule",
      release_date = "2017-03-03",
      platform = "Nintendo Switch",
      genre = "Adventure"
    )
    # Adding the object as a new row to the 'games' table
    db.session.add(game4)

    game5 = Game(
      title = "Hades",
      description = "Action roguelike set in the Underworld",
      release_date = "2020-09-17",
      platform = "Nintendo Switch",
      genre = "Roguelike"
    )
    # Adding the object as a new row to the 'games' table
    db.session.add(game5)

    # Commiting the changes
    db.session.commit()
    print("'games' table seeded")

    # Seeding the initial users - one admin and one non-admin
    user1 = User(
        email = "user1@email.com",
        # Encrypt the password with bcrypt
        password = bcrypt.generate_password_hash("123456").decode("utf-8"),
        admin = True
    )
    db.session.add(user1)

    user2 = User(
        email = "user2@email.com",
        password = bcrypt.generate_password_hash("123456").decode("utf-8")
    )
    db.session.add(user2)
    
    db.session.commit()
    print("'users' table seeded") 


    # Seeding an entry into the backlog
    backlog_game1 = Backlog(
      # Setting the attributes, but excluding the id as SQLAlchemy manages that
      status = "Not played",
      date_added = date.today(),
      user = user1,
      game = game2
    )
    # Adding the object as a new row to the 'backlog' table
    db.session.add(backlog_game1)

    db.session.commit()
    print("'backlog' table seeded")     


    # Seeding an entry into the currently playing games table
    currently_playing1 = CurrentlyPlaying(
      # Setting the attributes, but excluding the id as SQLAlchemy manages that
      progress = "Ongoing",
      date_added = date.today(),
      user = user1,
      game = game1
    )
    # Adding the object as a new row to the 'currently_playing' table
    db.session.add(currently_playing1)

    # Seeding an entry into the currently playing games table
    currently_playing2 = CurrentlyPlaying(
      # Setting the attributes, but excluding the id as SQLAlchemy manages that
      progress = "50%",
      date_added = date.today(),
      user = user1,
      game = game4
    )
    # Adding the object as a new row to the 'currently_playing' table
    db.session.add(currently_playing2)

    db.session.commit()
    print("'currently_playing' table seeded")     


    # Seeding an entry into the wishlist table
    wishlist1 = Wishlist(
      # Setting the attributes, but excluding the id as SQLAlchemy manages that
      priority = "High",
      date_added = date.today()
    )
    # Adding the object as a new row to the 'wishlist' table
    db.session.add(wishlist1)

    db.session.commit()
    print("'wishlist' table seeded")    


# CLI Command for dropping the tables 

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("All tables dropped") 