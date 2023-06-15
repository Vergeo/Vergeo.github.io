import os
import secrets
from PIL import Image

from flask import render_template, url_for, redirect, flash
from flask_login import login_user, current_user, logout_user, login_required

from werkzeug.security import generate_password_hash, check_password_hash

from Project import app, db
from Project.forms import RegistrationForm, LoginForm#, UpdateProfileForm
from Project.models import User

@app.route("/")
@app.route("/home")
def home() :
	return render_template("home.html")

@app.route("/register", methods=['GET', 'POST'])
def register() :
	form = RegistrationForm()

	if form.validate_on_submit() :
		hashed_password = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=16)
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()

		flash(f"Account created for {form.username.data}!", "success")
		return redirect(url_for("login"))

	return render_template("register.html", title="Register",form=form)

@app.route("/login", methods=['GET', 'POST'])
def login() :
	form = LoginForm()

	if form.validate_on_submit() :
		user = User.query.filter_by(username=form.username.data).first()
		if user and check_password_hash(user.password, form.password.data) :
			login_user(user, remember=form.remember.data)
			flash(f"Logged in as {form.username.data}!", "success")
			return redirect(url_for("home"))
		flash("Incorrect Username or Password!", "danger")

	return render_template("login.html", form=form)

@app.route("/logout")
def logout() :
	logout_user()
	return redirect(url_for("home"))

@app.route("/about")
def about() :
	return render_template("about.html")

@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile() :
	return render_template("profile.html", title="Profile")

@app.route("/play")
def play() :
	return render_template("game.html")