CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
);

CREATE TABLE films (
    id SERIAL PRIMARY KEY, 
    filmname TEXT, 
    filmyear INTEGER, 
    filmdirector TEXT, 
    filmgenre TEXT, 
    filmrating INTEGER
    );