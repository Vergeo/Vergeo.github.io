from flask_login import UserMixin
from Project import db, login_manager

from datetime import datetime

@login_manager.user_loader
def load_user(user_id) :
	# return Uer.query.filter_by(id=int(user_id))
	return User.query.get(user_id)

class User(db.Model, UserMixin) :
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(256), unique=True, nullable=False)
	email = db.Column(db.String(256), unique=True, nullable=False)
	password = db.Column(db.String(256), nullable=False)
	date_signed_up = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	date_updated = db.Column(db.DateTime)
	email_verified = db.Column(db.Boolean, nullable=False, default=False)
	image_file = db.Column(db.String(256), nullable=False, default="default.jpg")

	def __repr__(self) :
		return f"User({self.username} - {self.email} - {self.date_signed_up})"

class Scoreboard(db.Model) :
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	score = db.Column(db.Integer, nullable=False)
	date_achieved = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)