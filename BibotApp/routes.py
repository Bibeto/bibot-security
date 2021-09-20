from flask import render_template, url_for, flash, redirect, request
from BibotApp.forms import RegistrationForm, LoginForm
from BibotApp import app, db, bcrypt 
from BibotApp.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
def home(): 
    return render_template("home.html")

@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up(): 
    if current_user.is_authenticated: 
        redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit(): 
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created !", "success") 
        return redirect(url_for("sign_in"))
    return render_template("sign_up.html", form=form)


@app.route("/sign_in", methods=['POST', 'GET'])
def sign_in(): 
    if current_user.is_authenticated: 
        redirect(url_for("home"))
    form= LoginForm()
    if form.validate_on_submit(): 
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data) 
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else : 
            flash("Login unsuccesful", "danger")
    return render_template("sign_in.html", form=form)


@app.route ("/logout")
def logout(): 
    logout_user()
    return redirect(url_for("home"))


@app.route("/account") 
@login_required
def account(): 
    return render_template("account.html")
