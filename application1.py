import os

from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
DATABASE_URL1="postgresql://scjygiiyarbyie:067d04bdec5414ffe3b965e381108102b8f793ebb24abfe2a243753c6a00772a@ec2-184-73-25-2.compute-1.amazonaws.com:5432/d4dqi9ljdf8igd"


if not DATABASE_URL1:
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(DATABASE_URL1)
db = scoped_session(sessionmaker(bind=engine))

#I hope this works

isloggedin=False

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return "Login html file goes here"

@app.route("/register")
def register():
    return "Register html file goes here"

@app.route("/home")
def home():
    return "home html file goes here"