CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
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

CREATE TABLE directors (
    id SERIAL PRIMARY KEY,
    director TEXT
);

CREATE TABLE ratings (
    id SERIAL PRIMARY KEY,
    film TEXT,
    rating INTEGER,
    comment TEXT,
    user_id INTEGER REFERENCES users ON DELETE CASCADE
);