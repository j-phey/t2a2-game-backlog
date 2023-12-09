from flask import Flask
from flask_sqlalchemy import SQLAlchemy # Importing ORM
from flask_marshmallow import Marshmallow # Importing for serialisation
from flask_bcrypt import Bcrypt # Importing for password hashing
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity # Required for JWT token actions

# Creating required objects for Marshmallow, bcrypt, JWTManager etc.
ma = Marshmallow()
# Creating the database object 'db'
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    # Create the Flask app object 
    app = Flask(__name__)

    # Configure our app with config file:
    app.config.from_object("config.app_config")

    # Create our database object 'db' to utilise ORM
    db.init_app(app)

    # Create the Marshmallow object to allow the use of schemas
    ma.init_app(app)

    # Create the JWT and bcrypt objects for authentication
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Importing the controllers and activating the blueprints
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)    

    return app


# -- MODELS --
# Create the models, which are classes that allow object creation and creates the structure that will be used as a table and its rows in the database.

# # Game() model
# class Game(db.Model):
#     # Defining the table name for the db
#     __tablename__= "games"
#     # Setting the primary key and defining each attribute as a column in the db table using the 'db' object earlier
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String())
#     description = db.Column(db.String())
#     release_date = db.Column(db.Date())
#     platform = db.Column(db.String())
#     genre = db.Column(db.String())

# # User() model
# class User(db.Model):
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(), nullable=False, unique=True)
#     password = db.Column(db.String(), nullable=False)
#     admin = db.Column(db.Boolean(), default=False)


# -- SCHEMAS --






# -- CLI COMMANDS --

# # CLI command that creates the database (db)
# @app.cli.command("create")
# def create_db():
#     db.create_all()
#     print("Game and User tables created")

# # Seed game entries into the 'games' table
# @app.cli.command("seed")
# def seed_db():
#     # from datetime import date
#     # Creating the first game object
#     game1 = Game(
#       # Setting the attributes, but excluding the id as SQLAlchemy manages that
#       title = "World of Warcraft",
#       description = "A massive online game set in Azeroth",
#       release_date = "2004-11-23",
#       platform = "PC",
#       genre = "MMORPG"
#     )
#     # Adding the object as a new row to the 'games' table
#     db.session.add(game1)
    
#     # Creating the second game object
#     game2 = Game(
#       title = "Rainbow Six Siege",
#       description = "Online tactical shooter",
#       release_date = "2015-12-01",
#       platform = "PS4",
#       genre = "FPS"
#     )
#     # Adding the object as a new row to the 'games' table
#     db.session.add(game2)

#     # Commiting the changes
#     db.session.commit()
#     print("Game table seeded")

#     # Seeding the initial users - one admin and one non-admin
#     admin_user = User(
#         email = "admin@email.com",
#         # Encrypt the password with bcrypt
#         password = bcrypt.generate_password_hash("123456").decode("utf-8"),
#         admin = True
#     )
#     db.session.add(admin_user)

#     user1 = User(
#         email = "user1@email.com",
#         password = bcrypt.generate_password_hash("123456").decode("utf-8")
#     )
#     db.session.add(user1)
    
#     db.session.commit()
#     print("User table seeded") 


# # CLI Command for dropping the tables 

# @app.cli.command("drop")
# def drop_db():
#     db.drop_all()
#     print("All tables dropped") 

# # -- ROUTES --

# # Route: Root / home page (may not be required)

# @app.route("/")
# def hello():
#   return "Hello World!"


