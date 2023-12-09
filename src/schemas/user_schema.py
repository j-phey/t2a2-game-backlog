from main import ma
from marshmallow.validate import Length # Importing for password length
from models.users import User

# User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
    fields = ("email", "password", "admin")  
    #set the password's length to a minimum of 6 characters
    password = ma.String(validate=Length(min=6))

user_schema = UserSchema()
users_schema = UserSchema(many=True)