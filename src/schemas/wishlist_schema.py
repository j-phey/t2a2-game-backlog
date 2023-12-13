from main import ma
from marshmallow import fields
# Ensure field length is >0, OneOf pre-defined fields, matches Regexp
from marshmallow.validate import OneOf

# Constants for valid values
VALID_PRIORITIES = ('Low', 'Medium', 'High')

# creating the Wishlist Schema with Marshmallow for serialisation. Coverting the data into JSON.
class WishlistSchema(ma.Schema):
    priority = fields.String(required=True, validate=OneOf(VALID_PRIORITIES))

    class Meta:
        # Fields to expose
        fields = ("id", "priority", "date_added", "user", "game_id", "game")
    user =  fields.Nested("UserSchema", only=("email",))
    game =  fields.Nested("GameSchema", only=("title", "platform"))

# Single wishlist schema, when one game needs to be retrieved
wishlist_single_schema = WishlistSchema()

# Multiple wishlist schema, when many games need to be retrieved
wishlist_many_schema = WishlistSchema(many=True)