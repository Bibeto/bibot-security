from flask import Flask
from flask_login.utils import login_required
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

    
app = Flask(__name__)
app.config['SECRET_KEY']='562ccbc224f274f3bfe20fd19c43ac2a'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "sign_in"  # if user not logged in redirects user to home page
login_manager.login_message_category = "info"  # make the not logged in message fancier 

from BibotApp import routes 