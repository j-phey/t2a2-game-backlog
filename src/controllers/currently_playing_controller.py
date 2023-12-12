from flask import Blueprint, jsonify, request, abort
from main import db
from models.currently_playing import CurrentlyPlaying
from models.users import User
from models.games import Game
from schemas.currently_playing_schema import currently_playing_single_schema, currently_playing_many_schema
from schemas.user_schema import user_schema, users_schema
from schemas.game_schema import game_schema, games_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

currently_playing = Blueprint('currently_playing', __name__, url_prefix="/currently_playing")

# - CURRENTLY PLAYING ROUTES -

# Route: GET list of /currently_playing

@currently_playing.route("/", methods=["GET"])
def get_currently_playing():
    # Get all the currently playing entries from the database
    stmt = db.select(CurrentlyPlaying)
    currently_playing = db.session.scalars(stmt)
    # Converting the entries from the database into a JSON format and storing them in 'result'
    result = currently_playing_many_schema.dump(currently_playing)
    # Returning the result in JSON format
    return jsonify(result)

# Route: GET a single currently playing 
@currently_playing.route("/<int:id>/", methods=["GET"])
def get_single_currently_playing(id):
    stmt = db.select(CurrentlyPlaying).filter_by(id=id)
    currently_playing = db.session.scalar(stmt)
    # Returns an error if the entry doesn't exist
    if not currently_playing:
        return abort(400, description= "Game does not exist")
    # Convert the currently_playings from the database into a JSON format and store them in result
    result = currently_playing_single_schema.dump(currently_playing)
    # return the data in JSON format
    return jsonify(result)


#  Route: POST Create a new currently playing entry

@currently_playing.route("/", methods=["POST"])
@jwt_required()
def currently_playing_create():
    # Create a currently_playing entry
    currently_playing_fields = currently_playing_single_schema.load(request.json)
    # Get the id from jwt
    user_id = get_jwt_identity()
    new_currently_playing = CurrentlyPlaying()
    new_currently_playing.progress = currently_playing_fields["progress"]
    new_currently_playing.date_added = date.today()

    # Use that user id to set the ownership of the entry
    new_currently_playing.user_id = user_id

    # Allow Game ID to be added to body 
    game_id = currently_playing_fields["game_id"]
    new_currently_playing.game_id = game_id

    # Add to the database and commit
    db.session.add(new_currently_playing)
    db.session.commit()
    # Return the currently_playing in the response
    return jsonify(currently_playing_single_schema.dump(new_currently_playing))


# Route: Update a currently playing entry
 
@currently_playing.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_currently_playing(id):
    # Create a new currently_playing
    currently_playing_fields = currently_playing_single_schema.load(request.json)

    # Get the user id by invoking get_jwt_identity
    user_id = get_jwt_identity()
    # Find the user in the db
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    # Make sure the user is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")
    # Find the entry
    stmt = db.select(CurrentlyPlaying).filter_by(id=id)
    currently_playing = db.session.scalar(stmt)
    # Return an error if the currently_playing doesn't exist
    if not currently_playing:
        return abort(400, description= "Game does not exist")
    # Update the currently_playing with the given values
    currently_playing.progress = currently_playing_fields["progress"]
    currently_playing.date_added = date.today()
    # Add to the database and commit
    db.session.commit()
    # Return the currently_playing in the response
    return jsonify(currently_playing_single_schema.dump(currently_playing))


# Route: Delete a currently playing entry

# /<int:id> lets the server know what currently playing entry we want to delete 
@currently_playing.route("/<int:id>", methods=["DELETE"])
@jwt_required()
# Include the id parameter
def currently_playing_delete(id):
    # Get the user id by invoking get_jwt_identity()
    user_id = get_jwt_identity()
    # Find the user in the db
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    # Make sure the user is in the database
    if not user:
        return abort(401, description="Invalid user")
    # Prevents the request if the user is not an admin
    if not user.admin:
        return abort(401, description="Unauthorised user")

    # Find the currently_playing id
    stmt = db.select(CurrentlyPlaying).filter_by(id=id)
    currently_playing = db.session.scalar(stmt)
    # Return an error if the currently_playing id doesn't exist
    if not currently_playing:
        return abort(400, description= "Game doesn't exist")
    #D elete the currently_playing from the database and commit the change
    db.session.delete(currently_playing)
    db.session.commit()
    # Return the currently_playing as the response
    return jsonify(currently_playing_single_schema.dump(currently_playing))

# GET a user's currently playing games
@currently_playing.route("/users", methods=["GET"])
def get_users():
    # Get the user from the database table
    stmt = db.select(User)
    users_list = db.session.scalars(stmt)
    # Convert the users from the database into a JSON format and store them in result
    result = users_schema.dump(users_list)
    # return the data in JSON format
    return jsonify(result)