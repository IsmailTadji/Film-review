from app import app
from db import db
import films
from flask import render_template, request, session, redirect
from sqlalchemy import text
import users
import verification


@app.route("/")
def index():
    film_list = films.get_films()
    return render_template("index.html", film_list=film_list)

@app.route("/register", methods=["GET", "POST"])
def register():
    
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]

        if password != password2:
            return render_template("error.html", message="Passwords don't match")
        if not verification.verify_username(username):
            return render_template("error.html", message="Username must contain between 3 and 12 characters and only include letters, numbers, hyphens, and underscores.")
        if not verification.verify_password(password):
            return render_template("error.html", message="Password must contain atleast 8 characters, 1 upper case and 1 lower case character.")
        if not users.register(username, password):
            return render_template("error.html", message="User already exists")
        return redirect("/")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not users.login(username, password):
            return render_template("error.html", message="Invalid credentials")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/addfilm", methods=["POST"])
def addfilm():

    name = request.form["filmname"]
    year = request.form["filmyear"]
    director = request.form["filmdirector"]
    genre = request.form["filmgenre"]
    rating =request.form["filmrating"]

    films.add_film(name,year,director,genre,rating)
    return redirect("/")

