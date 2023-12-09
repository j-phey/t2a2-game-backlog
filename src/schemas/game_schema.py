from main import ma

# creating the Game Schema with Marshmallow for serialisation. Coverting the data into JSON.

class GameSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description", "release_date", "platform", "genre")

# Single game schema, when one game needs to be retrieved
game_schema = GameSchema()

# Multiple game schema, when many games need to be retrieved
games_schema = GameSchema(many=True)