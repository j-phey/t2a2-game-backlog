from main import ma
from marshmallow import fields

# creating the Wishlist Schema with Marshmallow for serialisation. Coverting the data into JSON.

class WishlistSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "priority", "date_added", "user", "game_id", "game")
    user =  fields.Nested("UserSchema", only=("email",))
    game =  fields.Nested("GameSchema", only=("title", "platform"))

# Single wishlist schema, when one game needs to be retrieved
wishlist_single_schema = WishlistSchema()

# Multiple wishlist schema, when many games need to be retrieved
wishlist_many_schema = WishlistSchema(many=True)