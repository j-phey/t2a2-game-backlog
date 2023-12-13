from flask import Blueprint, jsonify, request, abort
from main import db
from models.backlog import Backlog
from models.users import User
from schemas.backlog_schema import backlog_single_schema, backlog_many_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

backlog = Blueprint('backlog', __name__, url_prefix="/backlog")

# - CURRENTLY PLAYING ROUTES -

# Route: GET list of /backlog

@backlog.route("/", methods=["GET"])
def get_backlog():
    # Get all the backlog entries from the database
    stmt = db.select(Backlog)
    backlog = db.session.scalars(stmt)
    # Converting the entries from the database into a JSON format and storing them in 'result'
    result = backlog_many_schema.dump(backlog)
    # Returning the result in JSON format
    return jsonify(result)

# Route: GET a single backlog entry
@backlog.route("/<int:id>/", methods=["GET"])
def get_single_backlog(id):
    stmt = db.select(Backlog).filter_by(id=id)
    backlog = db.session.scalar(stmt)
    # Returns an error if the entry doesn't exist
    if not backlog:
        return abort(400, description= "Game does not exist")
    # Convert the backlogs from the database into a JSON format and store them in result
    result = backlog_single_schema.dump(backlog)
    # return the data in JSON format
    return jsonify(result)


#  Route: POST Create a new backlog entry

@backlog.route("/", methods=["POST"])
@jwt_required()
def backlog_create():
    #Create a backlog entry
    backlog_fields = backlog_single_schema.load(request.json)
    user_id = get_jwt_identity()
    new_backlog = Backlog()
    new_backlog.status = backlog_fields["status"]
    new_backlog.date_added = date.today()

    # Use that user id to set the ownership of the entry
    new_backlog.user_id = user_id

    # Allow Game ID to be added to body 
    game_id = backlog_fields["game_id"]
    new_backlog.game_id = game_id

    # Add to the database and commit
    db.session.add(new_backlog)
    db.session.commit()
    # Return the backlog in the response
    return jsonify(backlog_single_schema.dump(new_backlog))


# Route: Update a backlog entry
 
@backlog.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_backlog(id):
    # Create a new backlog
    backlog_fields = backlog_single_schema.load(request.json)

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
    stmt = db.select(Backlog).filter_by(id=id)
    backlog = db.session.scalar(stmt)
    # Return an error if the backlog doesn't exist
    if not backlog:
        return abort(400, description= "Game does not exist")
    # Update the backlog with the given values
    backlog.status = backlog_fields["status"]
    backlog.date_added = date.today()
    # Add to the database and commit
    db.session.commit()
    # Return the backlog in the response
    return jsonify(backlog_single_schema.dump(backlog))


# Route: Delete a backlog entry

# /<int:id> lets the server know what backlog entry we want to delete 
@backlog.route("/<int:id>", methods=["DELETE"])
@jwt_required()
# Include the id parameter
def backlog_delete(id):
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

    # Find the backlog id
    stmt = db.select(Backlog).filter_by(id=id)
    backlog = db.session.scalar(stmt)
    # Return an error if the backlog id doesn't exist
    if not backlog:
        return abort(400, description= "Game doesn't exist")
    #D elete the backlog from the database and commit the change
    db.session.delete(backlog)
    db.session.commit()
    # Return the backlog as the response
    return jsonify(backlog_single_schema.dump(backlog))