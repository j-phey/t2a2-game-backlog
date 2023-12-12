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
    app.json.sort_keys = False # Ensures right sort instead of alphabetically

    # Create our database object 'db' to utilise ORM
    db.init_app(app)

    # Create the Marshmallow object to allow the use of schemas
    ma.init_app(app)

    # Create the JWT and bcrypt objects for authentication
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Importing the CLI commands from the commands.py file
    from commands import db_commands
    app.register_blueprint(db_commands)

    # Importing the controllers and activating the blueprints
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)    

    return app