from flask import Blueprint, render_template, url_for

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template('base.html')

@main.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"

