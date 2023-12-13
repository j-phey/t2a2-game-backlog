from main import ma
from marshmallow import fields

# creating the Backlog Schema with Marshmallow for serialisation. Coverting the data into JSON.

class BacklogSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "status", "date_added", "user", "game_id", "game")
    user =  fields.Nested("UserSchema", only=("email",))
    game =  fields.Nested("GameSchema", only=("title",))

# Single backlog schema, when one game needs to be retrieved
backlog_single_schema = BacklogSchema()

# Multiple backlog schema, when many games need to be retrieved
backlog_many_schema = BacklogSchema(many=True)