from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash
from app import db
from app.models import User

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        
        # Check if email exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered")
            return redirect(url_for("auth.register"))
        
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully!")
        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth.route("/login")
def login():
    return render_template("login.html")
