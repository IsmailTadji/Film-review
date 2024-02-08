from app import app
from db import db
import films
from flask import render_template, request, session, redirect
from sqlalchemy import text
import users
import films



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
        if users.register(username, password):
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
