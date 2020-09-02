import os
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONDO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

@app.route("/")
def home():
    return render_template("landing.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")

# @app.route("/categories")
# def categories():

#     types = list(mongo.db.type.find())

#     return render_template("categories.html", types=types)


@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.type.find().sort("type", 1))
    test = list(mongo.db.recipes.find().sort("test", 1))


    return render_template("recipes.html", recipes=recipes, test=test)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
