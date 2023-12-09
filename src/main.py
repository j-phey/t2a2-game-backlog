from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy # Importing ORM
from flask_marshmallow import Marshmallow # Importing for serialisation
from marshmallow.validate import Length # Importing for password length
from flask_bcrypt import Bcrypt # Importing for password hashing
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity # Required for JWT token actions
from datetime import timedelta, date # Required for JWT token expiry

# Initialising the app
app = Flask(__name__)

# Creating required objects for Marshmallow, bcrypt, JWTManager etc.
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Creating the database object 'db'
db = SQLAlchemy(app)


def create_app():
    # Create the Flask app object 
    app = Flask(__name__)

    # Configure our app with config file:
    app.config.from_object("config.app_config")

    # Create our database object 'db' to utilise ORM
    db.init_app(app)

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

# creating the Game Schema with Marshmallow for serialisation. Coverting the data into JSON.

class GameSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description", "release_date", "platform", "genre")

# Single game schema, when one game needs to be retrieved
game_schema = GameSchema()

# Multiple game schema, when many games need to be retrieved
games_schema = GameSchema(many=True)

# User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
    fields = ("email", "password", "admin")  
    #set the password's length to a minimum of 6 characters
    password = ma.String(validate=Length(min=6))

user_schema = UserSchema()
users_schema = UserSchema(many=True)


# -- CLI COMMANDS --

# CLI command that creates the database (db)
@app.cli.command("create")
def create_db():
    db.create_all()
    print("Game and User tables created")

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

@app.cli.command("drop")
def drop_db():
    db.drop_all()
    print("All tables dropped") 

# -- ROUTES --

# Route: Root / home page (may not be required)

@app.route("/")
def hello():
  return "Hello World!"


# - USER ROUTES -

# Route: Register new User

@app.route("/auth/register", methods=["POST"])
def auth_register():
    # Loading the request data in a user_schema, which is converted to JSON
    user_fields = user_schema.load(request.json)
    # Find the user by email address first
    stmt = db.select(User).filter_by(email=request.json['email'])
    # Creating the user object
    user = db.session.scalar(stmt)

    # Validate that the email doesn't already exist
    if user:
        # Return an abort message 
        return abort(400, description="Email already registered")
    
    # Create the user object
    user = User()
    # Adding the email attribute
    user.email = user_fields["email"]
    # Adding the password attribute which is hashed by bcrypt
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
    #set the admin attribute to False
    user.admin = False
    # Add the created user to the database and commit the changes
    db.session.add(user)
    db.session.commit()
    # Create a variable that sets an expiry date
    expiry = timedelta(days=1)
    # Create the access token
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    # Return the user email and the access token as a response
    return jsonify({"user": user.email, "token": access_token })


# Route: Authenticate and login user /auth/login

@app.route("/auth/login", methods=["POST"])
def auth_login():
    # Get the user data from the 'request'
    user_fields = user_schema.load(request.json)
    # Find the user by email address 
    stmt = db.select(User).filter_by(email=request.json['email'])
    user = db.session.scalar(stmt)
    # If the user doesn't exist or if the password is incorrect, send an error
    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username and/or password")

    # Creating a variable that sets an expiry date for the JWT token
    expiry = timedelta(days=1) # Expires after 'x' days
    # Creating the access token
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    # Return the user email and the access token as a response
    return jsonify({"user": user.email, "token": access_token })