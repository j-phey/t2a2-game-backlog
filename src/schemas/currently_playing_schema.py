from main import ma

# creating the Currently Playing Schema with Marshmallow for serialisation. Coverting the data into JSON.

class CurrentlyPlayingSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "progress", "date_added")

# Single currently_playing schema, when one game needs to be retrieved
currently_playing_single_schema = CurrentlyPlayingSchema()

# Multiple currently_playing schema, when many games need to be retrieved
currently_playing_many_schema = CurrentlyPlayingSchema(many=True)