from review_flask import db, login_manager
#importing db from __init__.py
from datetime import datetime, timezone
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    # User(db.Model) allows the ability to define columns and relationships.
    id = db.Column(db.Integer, primary_key=True)
    #Creates a row with a distinct ID for each user.
    username = db.Column(db.String(20), unique=True, nullable = False)
    #string limit of 20 placed in db.string(). unique = True means that there can only be one in the database. nullable = False means that there must be a value in this column.
    email = db.Column(db.String(120), unique=True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    #Automatically puts default.jpg as an image_file until the user decides to choose their own.
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref = 'author', lazy=True)
    #Establishes a relationship between a User and a post. backref allows you to access the author of post. lazy=True means related posts load only when they are accessed.
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    #returns user information for debugging (username, email, pfp picture)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #Gives each post a unique ID. 
    title = db.Column(db.String(100), nullable=False)
    #There must be a title for each post. Limit of 100 characters.
    date_posted = db.Column(db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    #Stores the time and date the post was created.
    content = db.Column(db.Text, nullable=False)
    #Stores the actual content in the post. Any length but can't be left empty
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #links each post with their respective user. db.Foreignkey('user.id') does this.
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    #returns post information for debugging. (title and date posted)
