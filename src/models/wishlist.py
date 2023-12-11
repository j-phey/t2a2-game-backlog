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