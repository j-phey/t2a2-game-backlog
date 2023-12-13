from main import ma
from marshmallow.validate import Length # Importing for password length
from marshmallow import fields

# User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("email", "password", "admin", "currently_playing")  # Include what the user is currently playing when called
        load_only = ['password', 'admin'] # Setting to load_only so they won't show up when dump is invoked
    #set the password's length to a minimum of 6 characters
    password = ma.String(validate=Length(min=6, error='Password must be at least 6 characters'))
    currently_playing = fields.List(fields.Nested("CurrentlyPlayingSchema", exclude=("user",))) # Allows a user's list of Currently Playing to be exposed (e.g. profile page)

user_schema = UserSchema()
users_schema = UserSchema(many=True)