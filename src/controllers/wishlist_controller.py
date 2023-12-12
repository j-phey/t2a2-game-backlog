from flask import Blueprint, jsonify, request, abort
from main import db
from models.wishlist import Wishlist
from models.users import User
from schemas.wishlist_schema import wishlist_single_schema, wishlist_many_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

wishlist = Blueprint('wishlist', __name__, url_prefix="/wishlist")

# - CURRENTLY PLAYING ROUTES -

# Route: GET list of /wishlist

@wishlist.route("/", methods=["GET"])
def get_wishlist():
    # Get all the wishlist entries from the database
    stmt = db.select(Wishlist)
    wishlist = db.session.scalars(stmt)
    # Converting the entries from the database into a JSON format and storing them in 'result'
    result = wishlist_many_schema.dump(wishlist)
    # Returning the result in JSON format
    return jsonify(result)

# Route: GET a single wishlist entry
@wishlist.route("/<int:id>/", methods=["GET"])
def get_single_wishlist(id):
    stmt = db.select(Wishlist).filter_by(id=id)
    wishlist = db.session.scalar(stmt)
    # Returns an error if the entry doesn't exist
    if not wishlist:
        return abort(400, description= "Game does not exist")
    # Convert the wishlists from the database into a JSON format and store them in result
    result = wishlist_single_schema.dump(wishlist)
    # return the data in JSON format
    return jsonify(result)


#  Route: POST Create a new wishlist entry

@wishlist.route("/", methods=["POST"])
@jwt_required()
def wishlist_create():
    #Create a wishlist entry
    wishlist_fields = wishlist_single_schema.load(request.json)

    new_wishlist = Wishlist()
    new_wishlist.priority = wishlist_fields["priority"]
    new_wishlist.date_added = date.today()

    # Add to the database and commit
    db.session.add(new_wishlist)
    db.session.commit()
    # Return the wishlist in the response
    return jsonify(wishlist_single_schema.dump(new_wishlist))


# Route: Update a wishlist entry
 
@wishlist.route("/<int:id>/", methods=["PUT"])
@jwt_required()
def update_wishlist(id):
    # Create a new wishlist
    wishlist_fields = wishlist_single_schema.load(request.json)

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
    stmt = db.select(Wishlist).filter_by(id=id)
    wishlist = db.session.scalar(stmt)
    # Return an error if the wishlist doesn't exist
    if not wishlist:
        return abort(400, description= "Game does not exist")
    # Update the wishlist with the given values
    wishlist.priority = wishlist_fields["priority"]
    wishlist.date_added = date.today()
    # Add to the database and commit
    db.session.commit()
    # Return the wishlist in the response
    return jsonify(wishlist_single_schema.dump(wishlist))


# Route: Delete a wishlist entry

# /<int:id> lets the server know what wishlist entry we want to delete 
@wishlist.route("/<int:id>", methods=["DELETE"])
@jwt_required()
# Include the id parameter
def wishlist_delete(id):
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

    # Find the wishlist id
    stmt = db.select(Wishlist).filter_by(id=id)
    wishlist = db.session.scalar(stmt)
    # Return an error if the wishlist id doesn't exist
    if not wishlist:
        return abort(400, description= "Game doesn't exist")
    #D elete the wishlist from the database and commit the change
    db.session.delete(wishlist)
    db.session.commit()
    # Return the wishlist as the response
    return jsonify(wishlist_single_schema.dump(wishlist))