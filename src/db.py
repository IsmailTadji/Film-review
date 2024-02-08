from app import app
from dotenv import find_dotenv, load_dotenv
from flask_sqlalchemy import SQLAlchemy
from os import getenv


load_dotenv(find_dotenv())
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)