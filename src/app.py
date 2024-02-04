from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from os import getenv
from dotenv import find_dotenv, load_dotenv
from werkzeug.security import check_password_hash, generate_password_hash



app = Flask(__name__)
load_dotenv(find_dotenv())
app.secret_key = getenv("SECRET_KEY")
print(getenv("DATABASE_URL"))
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():
    sql = '''
    SELECT id, filmname, filmyear, filmdirector, filmgenre, filmrating FROM films ORDER BY id
    '''
    result = db.session.execute(text(sql))
    films = result.fetchall()
    return render_template("index.html", films=films)

@app.route("/register", methods=["GET", "POST"])
def register():
    
    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        hash_value = generate_password_hash(password)
        sql = '''
        INSERT INTO users (username, password) 
        VALUES (:username, :password)
        '''
        db.session.execute(text(sql), {"username":username, "password":hash_value})
        db.session.commit()

    session["username"] = username
    return redirect("/")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        sql = "SELECT id, password FROM users WHERE username=:username"
        result = db.session.execute(text(sql), {"username":username})
        user = result.fetchone()
        if not user:
            return render_template("error.html", message="Log in credentials do not match")
        else:
            hash_value = user.password
            if check_password_hash(hash_value, password):
                session["username"] = username
                return redirect("/")



@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/addfilm", methods=["POST"])
def addfilm():

    filmname = request.form["filmname"]
    filmyear = request.form["filmyear"]
    filmdirector = request.form["filmdirector"]
    filmgenre = request.form["filmgenre"]
    filmrating =request.form["filmrating"]

    sql = '''
    INSERT INTO films (filmname, filmyear, filmdirector,filmgenre,filmrating) 
    VALUES (:filmname, :filmyear, :filmdirector, :filmgenre, :filmrating)
    '''
    db.session.execute(text(sql), {"filmname":filmname, "filmyear":filmyear, "filmdirector":filmdirector, "filmgenre":filmgenre, "filmrating":filmrating})
    db.session.commit()
    return redirect("/")

@app.route("/")
def showfilms():
    sql = '''
    SELECT id, filmname, filmyear, filmdirector, filmgenre, filmrating FROM films ORDER BY id
    '''
    result = db.session.execute(text(sql))
    films = result.fetchall()
    return render_template("index.html", films=films)




if __name__ == "__main__":
    app.run(debug=True)
