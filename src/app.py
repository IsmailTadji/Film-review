from dotenv import find_dotenv, load_dotenv
from flask import Flask
from os import getenv



app = Flask(__name__)
load_dotenv(find_dotenv())
app.secret_key = getenv("SECRET_KEY")

import routes
