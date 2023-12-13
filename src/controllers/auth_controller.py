from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt
from models.users import User
from schemas.user_schema import user_schema #, users_schema
from datetime import timedelta
from flask_jwt_extended import create_access_token
from werkzeug.exceptions import BadRequest # Handle BadRequests from Flask
from marshmallow.exceptions import ValidationError # Handles Marshmallow ValidationErrors

auth = Blueprint('auth', __name__, url_prefix="/auth")

# - USER ROUTES -

# Route: Register new User

@auth.route("/register", methods=["POST"])
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

@auth.route("/login", methods=["POST"])
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

# -- ERROR HANDLING --

# Attaching a handler to the blueprint (errorhandler method) to catch KeyError exceptions raised
@auth.errorhandler(KeyError)
def key_error(e):
    # Convert the description of the error to JSON
    return jsonify({'error': f'The field {e} is required'}), 400
    # JSON e.g.: "error": "The field 'email' is required"

# Handle BadRequest errors from Flask (e.g. when request is not JSON)
@auth.errorhandler(BadRequest)
def default_error(e):
    return jsonify({'error': e.description}), 400

# Handles Marshmallow Validation errors (e.g. field left empty)
@auth.errorhandler(ValidationError)
def validation_error(e):
    return jsonify(e.messages), 400 # messages has dictionary of errors