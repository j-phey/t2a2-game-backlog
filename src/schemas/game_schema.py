from main import ma
from marshmallow import fields
# Ensure field length is >0, OneOf pre-defined fields, matches Regexp
from marshmallow.validate import Length, OneOf, Regexp, And

# Constants for valid values
VALID_PLATFORM = ('PC', 'PS4', 'PS5', 'Nintendo Switch', 'Xbox')

# creating the Game Schema with Marshmallow for serialisation. Coverting the data into JSON.

class GameSchema(ma.Schema):
    title = fields.String(required=True, validate=Length(min=1, error='Title cannot be blank')) # Ensure title is >0 and is required
    platform = fields.String(required=True, validate=OneOf(VALID_PLATFORM)) # Value is OneOf the above constants
    genre = fields.String(required=True, validate=And(Length(min=1), Regexp('^[a-zA-Z0-9 ]+$'))) # Ensure genre only has letters, digits or spaces
 
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description", "release_date", "platform", "genre")

# Single game schema, when one game needs to be retrieved
game_schema = GameSchema()

# Multiple game schema, when many games need to be retrieved
games_schema = GameSchema(many=True)