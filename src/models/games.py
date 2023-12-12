from main import db

# Create the game model, which are classes that allow object creation and creates the structure that will be used as a table and its rows in the database

# Game() model
class Game(db.Model):
    # Defining the table name for the db
    __tablename__= "games"
    # Setting the primary key and defining each attribute as a column in the db table using the 'db' object earlier
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    release_date = db.Column(db.Date())
    platform = db.Column(db.String())
    genre = db.Column(db.String())

    currently_playing_id = db.Column(db.Integer, db.ForeignKey("currently_playing.id"), nullable=False)
    currently_playing = db.relationship(
        "CurrentlyPlaying",
        back_populates="games"
    )