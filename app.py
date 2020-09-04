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


@app.route("/myRecipes")
def myRecipes():
    user = session['user']
    recipes = list(mongo.db.recipes.find({"created_by": user}))
    return render_template("recipes.html", recipes=recipes, user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"user_name": request.form.get("user_name")
             })
        if existing_user:
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("user_name")
                flash("Welcome, {}".format(
                    request.form.get("user_name")))
                return redirect(url_for(
                    "profile", user=session["user"]))

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

    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

    return render_template("recipes.html", types=types, recipes=recipes)


@app.route("/recipe_list/<recipe_type>")
def recipe_list(recipe_type):

    recipe_type = recipe_type

    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

    return render_template("recipe_list.html", recipes=recipes, recipe_type=recipe_type)


@app.route("/view_recipe/<recipe_id>", methods=["GET", "POST"])
def view_recipe(recipe_id):

    recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    user = session['user']
    user_id = mongo.db.users.find_one({"user_name": user})
    return render_template("view_recipe.html", recipe_id=recipe_id,
                           recipes=recipes, user_id=user_id)


@app.route("/add_recipe")
def add_recipe():

    types = list(mongo.db.type.find().sort("type", 1))
    return render_template("add_recipe.html", types=types)


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"user_name": request.form.get("user_name").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirm = request.form.get("confirm")
        if password != confirm:
            flash("Passwords do not match")
            return redirect(url_for("register"))

        register = {

            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email"),
            "user_name": request.form.get("user_name"),
            "password": generate_password_hash(request.form.get("password")),
            "saved_recipes": [],

        }
        mongo.db.users.insert_one(register)

        # put new user in session cookie
        session["user"] = request.form.get("user_name")
        flash("Registration Successful!")
        return redirect(url_for(
            "profile", user=session["user"]))
    return render_template("landing.html")


@app.route("/profile/<user>", methods=["GET", "POST"])
def profile(user):

    user = user
    users = mongo.db.users.find().sort("user_name", 1)
    # grab session users username from database

    return render_template("profile.html", users=users, user=user)


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
            "rating_count": 0,
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(new)
        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))

    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
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
            "rating_count": 0,
            "created_by": session["user"]
        }
        mongo.db.recipes.update(new)
        flash("RECIPE SUCCESSFULLY UPDATED")
        return redirect(url_for("recipes'"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    return render_template("edit_recipe.html", recipe=recipe, recipes=recipes)


@app.route("/save_recipe/<recipe_id>", methods=["GET", "POST"])
def save_recipe(recipe_id):
    user = session["user"]
    recipe_id = recipe_id
    mongo.db.users.update(
        {"user_name": user},
        {'$addToSet': {'saved_recipes': recipe_id}})
    flash("RECIPE SAVED SUCCESSFULLY")

    return redirect(url_for("view_recipe", recipe_id=recipe_id))

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipes"))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
