from main import ma
from marshmallow import fields # Allows fields to be nested
# Ensure field length is >0, OneOf pre-defined fields, matches Regexp
from marshmallow.validate import OneOf

# Constants for valid values
VALID_PROGRESS = ('Ongoing', '25%', '50%', '75%', '100%')

# creating the Currently Playing Schema with Marshmallow for serialisation. Coverting the data into JSON.

class CurrentlyPlayingSchema(ma.Schema):
    progress = fields.String(required=True, validate=OneOf(VALID_PROGRESS)) # Value is OneOf the above constants

    class Meta:
        ordered = True # Sets the right order instead of alphabetically
        # Fields to expose
        fields = ("id", "progress", "date_added", "user", "game_id", "game")
    user =  fields.Nested("UserSchema", only=("email",))
    game =  fields.Nested("GameSchema", only=("title",))


# Single currently_playing schema, when one game needs to be retrieved
currently_playing_single_schema = CurrentlyPlayingSchema()

# Multiple currently_playing schema, when many games need to be retrieved
currently_playing_many_schema = CurrentlyPlayingSchema(many=True)