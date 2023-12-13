from main import ma
from marshmallow import fields
from marshmallow.validate import Length # For ensuring field length is >0

# creating the Game Schema with Marshmallow for serialisation. Coverting the data into JSON.

class GameSchema(ma.Schema):
    title = fields.String(required=True, validate=Length(min=1, error='Title cannot be blank')) # Ensure title is >0 and is required

    class Meta:
        # Fields to expose
        fields = ("id", "title", "description", "release_date", "platform", "genre")

# Single game schema, when one game needs to be retrieved
game_schema = GameSchema()

# Multiple game schema, when many games need to be retrieved
games_schema = GameSchema(many=True)