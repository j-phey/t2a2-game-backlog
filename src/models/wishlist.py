from main import db

# Create the game model, which are classes that allow object creation and creates the structure that will be used as a table and its rows in the database

# Wishlist() model
class Wishlist(db.Model):
    # Defining the table name for the db
    __tablename__= "wishlist"
    # Setting the primary key and defining each attribute as a column in the db table using the 'db' object earlier
    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.String())
    date_added = db.Column(db.Date())

    # Create Foreign Key for User
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship(
        "User",
        back_populates="wishlist"
    )

    # Create Foreign Key for Game
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable=False)
    game = db.relationship(
        "Game",
        back_populates="wishlist"
    )