from main import db

# Create the user models, which are classes that allow object creation and creates the structure that will be used as a table and its rows in the database

# User() model
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)

    # Relationship with currently_playing
    currently_playing = db.relationship(
        "CurrentlyPlaying",
        back_populates="user",
        cascade="all, delete"
    )

    # Relationship with backlog
    backlog = db.relationship(
        "Backlog",
        back_populates="user",
        cascade="all, delete"
    )