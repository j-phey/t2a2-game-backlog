from main import ma

# creating the Backlog Schema with Marshmallow for serialisation. Coverting the data into JSON.

class BacklogSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "status", "date_added")

# Single backlog schema, when one game needs to be retrieved
backlog_single_schema = BacklogSchema()

# Multiple backlog schema, when many games need to be retrieved
backlog_many_schema = BacklogSchema(many=True)