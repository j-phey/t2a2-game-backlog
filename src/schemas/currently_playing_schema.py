from main import ma
from marshmallow import fields # Allows fields to be nested

# creating the Currently Playing Schema with Marshmallow for serialisation. Coverting the data into JSON.

class CurrentlyPlayingSchema(ma.Schema):
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