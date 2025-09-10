from db import db
from sqlalchemy.sql import text

def get_films():
    sql = '''
    SELECT id, filmname, filmyear, filmdirector, filmgenre, filmrating FROM films ORDER BY id
    '''
    result = db.session.execute(text(sql))
    return result.fetchall()

def add_film(name,year,director,genre,rating):
    sql = '''
    INSERT INTO films (filmname, filmyear, filmdirector,filmgenre,filmrating) 
    VALUES (:filmname, :filmyear, :filmdirector, :filmgenre, :filmrating)
    '''
    db.session.execute(text(sql), {"filmname":name, "filmyear":year, "filmdirector":director, "filmgenre":genre, "filmrating":rating})
    db.session.commit()

def add_director(name):
    sql = '''
    INSERT INTO directors (name) 
    VALUES (:name)
    '''
    db.session.execute(text(sql), {"name":name})
    db.session.commit()