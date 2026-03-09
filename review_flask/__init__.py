from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#hashes passwords
#from flask

app = Flask(__name__)


app.config['SECRET_KEY'] = 'PUT YOUR OWN SECRET KEY HERE!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite'  # Use SQLite database

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#setting login route to our functon for login

from review_flask import routes
#placed at bottom because app is a dependency that must be initialized before importing routes