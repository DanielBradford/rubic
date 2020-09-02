import os
import datetime
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

@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": search}}))
    return render_template("recipes.html", recipes=recipes)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"user_name": request.form.get("user_name").lower()
             })

        if existing_user:
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("user_name").lower()
                flash("Welcome, {}".format(
                    request.form.get("user_name")))
                return redirect(url_for(
                    "profile", username=session["user"]))

                return render_template("profile.html")

            else:
                flash("Incorrect username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route('/logout')
def logout():
        # remove user session from cookies
        flash("You have been logged out")
        session.pop("user")
        return redirect(url_for("login"))

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.type.find().sort("type", 1))
    test = list(mongo.db.recipes.find().sort("test", 1))

    return render_template("recipes.html", recipes=recipes, test=test)


@app.route("/add_recipe")
def add_recipe():

    recipes = list(mongo.db.type.find().sort("type", 1))
    return render_template("add_recipe.html", recipes=recipes)


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        existing_user = mongo.db.users.find_one(
            {"user_name": request.form.get("user_name").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        if password != confirm:
            flash("Passwords do not match.")
            return redirect(url_for("register"))

        register = {

            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email"),
            "user_name": request.form.get("user_name"),
            "password": generate_password_hash(request.form.get("password")),

        }
        mongo.db.users.insert_one(register)

        # put new user in session cookie
        session["user"] = request.form.get("user_name")
        flash("Registration Successful!")
        return redirect(url_for(
            "profile", username=session["user"]))
    return render_template("landing.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab session users username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})['username']

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for('login'))


@app.route("/add_new_recipe", methods=["GET", "POST"])
def add_new_recipe():

    if request.method == "POST":
        new = {
            "recipe_name": request.form.get("recipe_name"),
            "type": request.form.get("type"),
            "using": request.form.get("using"),
            "oven_temperature": request.form.get("oven_temperature"),
            "ingredients": request.form.get("ingredients"),
            "dietary_need": request.form.get("dietary_need"),
            "notes": request.form.get("notes"),
            "method": request.form.get("method"),
            "rating": 0,
            "created_by": session["user"],
            "created_on": datetime.now()
        }
        mongo.db.recipes.insert_one(new)
        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))

    return render_template("add_recipe.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
