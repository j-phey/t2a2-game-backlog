from flask import Blueprint, jsonify, request, abort
from main import db
from models.currently_playing import CurrentlyPlaying
from models.users import User
from schemas.currently_playing_schema import currently_playing_single_schema, currently_playing_many_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

currently_playing = Blueprint('currently_playing', __name__, url_prefix="/currently_playing")

# - CURRENTLY PLAYING ROUTES -

# Route: GET list of /currently_playing

@currently_playing.route("/", methods=["GET"])
def get_currently_playing():
    # Get all the currently playing games from the database
    stmt = db.select(CurrentlyPlaying)
    currently_playing = db.session.scalars(stmt)
    # Converting the entries from the database into a JSON format and storing them in 'result'
    result = currently_playing_many_schema.dump(currently_playing)
    # Returning the result in JSON format
    return jsonify(result)

#  Route: POST Create a new currently playing entry

@currently_playing.route("/", methods=["POST"])
@jwt_required()
def currently_playing_create():
    #Create a game entry
    currently_playing_fields = currently_playing_single_schema.load(request.json)

    new_currently_playing = CurrentlyPlaying()
    new_currently_playing.progress = currently_playing_fields["progress"]
    new_currently_playing.date_added = date.today()

    # Add to the database and commit
    db.session.add(new_currently_playing)
    db.session.commit()
    # Return the game in the response
    return jsonify(currently_playing_single_schema.dump(new_currently_playing))