## Package import:
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy


# initialize flask
app = Flask(__name__)

# Configuring the Flask app to connect to the MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://viral_user:B%$RYNGQNq4$kJ%@localhost/viral_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating an instance of the SQLAlchemy class
db = SQLAlchemy(app)

# Landing page
@app.route("/")
def home():
    # Renders templates/home.html
    return render_template("home.html")


# Results page (no SQL yet, just display)
@app.route("/results")
def results():
    # Renders templates/results.html
    return render_template("results.html")


# Your hello route
# @app.route("/hello")
# @app.route("/hello/<name>")
# def hello(name=None):
#     if name:
#         return f"<p>Hello, {name}!</p>"
#     return "<p>This is the site without my name</p>"