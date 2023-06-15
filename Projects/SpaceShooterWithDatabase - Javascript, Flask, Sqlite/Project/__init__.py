from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from datetime import timedelta

app = Flask(__name__)


app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.permanent_session_lifetime = timedelta(minutes=30)

app.config["SECRET_KEY"] = "SECRET"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Session(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from Project import routes