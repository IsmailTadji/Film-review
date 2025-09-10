from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text



def register(username, password):
    sql = "SELECT * FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
    if user:
        return False
    hash_value = generate_password_hash(password)
    sql = '''
    INSERT INTO users (username, password) 
    VALUES (:username, :password)
    '''
    db.session.execute(text(sql), {"username":username, "password":hash_value})
    db.session.commit()

    return True

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
    if not user:
        return False
    if not check_password_hash(user.password, password):
        return False
    session["user_id"] = user.id
    session["username"] = username
    return True

def logout():
    del session["user_id"]
    del session["username"]

def user_id():
    return session.get("user_id", 0)
