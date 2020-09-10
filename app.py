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
# takes visitor to landing page
def home():
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    users = list(mongo.db.users.find().sort("user_name", 1))

    return render_template("landing.html", types=types,
                           recipes=recipes, users=users)


@app.route("/search", methods=["GET", "POST"])
# function to allow user to search for recipes based
# on recipe_name and ingredients index
def search():
    search = request.form.get("search")
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find({"$text": {"$search": search}}))
    return render_template("recipes.html", recipes=recipes, types=types)

# look at pep8 snake case better

# displays recipes only created by current user


@app.route("/myRecipes")
def myRecipes():
    user = session['user']
    recipes = list(mongo.db.recipes.find({"created_by": user}))

    return render_template("my_recipes.html", recipes=recipes, user=user)

# function logs user into the app


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
                return redirect(url_for(
                    "login"))

            return render_template('login.html')

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

# logs user out of appplication


@app.route('/logout')
def logout():
    # remove user session from cookies
    session.pop("user")
    flash("You have been logged out")
    return redirect(url_for("login"))


# takes user to registrating page
@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/recipes")
def recipes():
    # rating functionality
    # rating = list(mongo.db.recipes.distinct(
    #     "rating", {"_id": ObjectId(recipe_id)}))
    # count = len(rating)
    # if count == 0:
    #     current = "No ratings yet"
    # else:
    #     convert = [int(num) for num in rating]
    #     # gets average from all ratings
    #     current = (round(sum(convert)/len(convert), 1))
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

    return render_template("recipes.html", types=types,
                           recipes=recipes)


@app.route("/recipe_list/<recipe_type>")
def recipe_list(recipe_type):

    recipe_type = recipe_type

    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    types = list(mongo.db.type.find().sort("type_name", 1))

    return render_template("recipe_list.html",
                           recipes=recipes, recipe_type=recipe_type,
                           types=types)


@app.route("/view_recipe/<recipe_id>", methods=["GET", "POST"])
def view_recipe(recipe_id):
    try:
        recipe_id = recipe_id
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
        user = session['user']
        user_id = mongo.db.users.find_one({"user_name": user})
        saved_list = list(mongo.db.users.distinct(
            "saved_recipes", {"user_name": user}))

        return render_template("view_recipe.html", recipe=recipe,
                               recipes=recipes, user_id=user_id, user=user, saved_list=saved_list)

    except:
        flash("PLEASE REGISTER OR LOGIN FOR FULL ACCESS")
        return render_template("guest.html")

# routes user to the add recipe form template


@app.route("/add_recipe")
def add_recipe():
    types = list(mongo.db.type.find().sort("type", 1))
    products = list(mongo.db.products.find().sort("product_name", 1))
    return render_template("add_recipe.html", types=types, products=products)


# adds new user to users collection in db
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

        vegan = "Yes" if request.form.get("vegan") else "No"
        # boolean
        register = {


            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email"),
            "user_name": request.form.get("user_name"),
            "password": generate_password_hash(request.form.get("password")),
            "vegan": vegan,
            "saved_recipes": []

        }

        # defensive programming validation

        mongo.db.users.insert_one(register)

        # put new user in session cookie
        session["user"] = request.form.get("user_name")
        flash("Registration Successful!")
        # log user in
        return redirect(url_for(
            "profile", user=session["user"]))
    return render_template("landing.html")


@app.route("/profile/", methods=["GET", "POST"])
def profile():
    user = session["user"]
    this_user = mongo.db.users.find_one({"user_name": user})
    # users = mongo.db.users.find().sort("user_name", 1)
    # recipes = mongo.db.recipes.find().sort("recipe_name", 1)

    return render_template("profile.html", this_user=this_user)

# add new recipe to the database


@app.route("/add_new_recipe", methods=["GET", "POST"])
def add_new_recipe():
    if request.method == "POST":
        # establishes if vegan switch is selected
        vegan = "Yes" if request.form.get("vegan") else "No"
        new = {
            "recipe_name": request.form.get("recipe_name"),
            "type": request.form.get("type"),
            "appliance": request.form.get("appliance"),
            "temperature": request.form.get("temperature"),
            "cooking_time": request.form.get("time"),
            "ingredients": request.form.get("ingredients"),
            "vegan": vegan,
            "method": request.form.get("method"),
            "created_by": session["user"],
            "rating": []
        }

        # validation defensive programming
        # adds new recipe to recipes collection
        mongo.db.recipes.insert_one(new)
        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))

    return render_template("add_recipe.html")


# function to edit the chosen recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    types = list(mongo.db.type.find().sort("type_name", 1))
    # gets chosen recipe
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    products = list(mongo.db.products.find().sort("product_name", 1))
    # allows curent rating to be accessed and retained
    rating = list(mongo.db.recipes.distinct(
        "rating", {"_id": ObjectId(recipe_id)}
    ))
    if request.method == "POST":
        vegan = "Yes" if request.form.get("vegan") else "No"
        new = {
            "recipe_name": request.form.get("recipe_name"),
            "type": request.form.get("type"),
            "appliance": request.form.get("appliance"),
            "temperature": request.form.get("temperature"),
            "cooking_time": request.form.get("time"),
            "ingredients": request.form.get("ingredients"),
            "vegan": vegan,
            "method": request.form.get("method"),
            "created_by": session["user"],
            # keeps current rating array
            "rating": rating
        }

        # validation defensive programming
        # check recipe exists if not 404 page

        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, new)
        flash("RECIPE SUCCESSFULLY UPDATED")
        return redirect(url_for("recipes"))
    return render_template("edit_recipe.html", recipe=recipe,
                           recipes=recipes, types=types, recipe_id=recipe_id, products=products)


# function to allow user to save chosen recipe
@app.route("/save_recipe/<recipe_id>", methods=["GET", "POST"])
def save_recipe(recipe_id):
    # gets current user
    user = session['user']
    # appends the chosen recipe_id to current user document in db
    mongo.db.users.update(
        {"user_name": user},
        {'$addToSet': {'saved_recipes': ObjectId(recipe_id)}})
    flash("RECIPE SAVED SUCCESSFULLY")
    return redirect(url_for("view_recipe", recipe_id=recipe_id))


# function to view all saved recipes of current user
@app.route("/saved_recipes", methods=["GET", "POST"])
def saved_recipes():
    # checks current user
    user = session["user"]
    # gets user document
    this = mongo.db.users.find_one({"user_name": user})
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    # gets list of all recipe ids saved by user
    saved_list = list(mongo.db.users.distinct(
        "saved_recipes", {"user_name": user}))
    # clears any empty entries
    check_list = []
    for item in saved_list:
        if item == "":
            continue
        else:
            check_list.append(item)
    # length of the list shows the rating count
    size = len(check_list)
    return render_template("saved_recipes.html",
                           recipes=recipes, user=user,
                           this=this, check_list=check_list, size=size)


# deletes the chosen recipe entirely from the database
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # javascript confirm confirms this action on frontend
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    # check recipe exists if not 404 page
    # defensive programming verify owner login in required
    return redirect(url_for("myRecipes"))


# removes the recipe from the users saved list
@app.route("/remove_recipe/<recipe_id>")
def remove_recipe(recipe_id):
    # check if user in session (login check)
    user = session["user"]
    saved_list = list(mongo.db.users.distinct(
        "saved_recipes", {"user_name": user}))
    recipe_id = recipe_id

    for item in saved_list:
        if item == recipe_id:
            # pull?

            flash("Recipe successfully removed from saved list")
            return redirect(url_for('saved_recipes', user=user))
        else:
            flash("FAILED TO REMOVE")
            return redirect(url_for('saved_recipes', user=user))

    return redirect(url_for('saved_recipes', user=user))


# adds rating to the rating array in recipes db
@app.route("/add_rating/<recipe_id>", methods=["POST", "GET"])
def add_rating(recipe_id):
    userRating = int(request.form.get("rating"))
    # gets the existing array
    currentRating = list(mongo.db.recipes.distinct(
        "rating", {"_id": recipe_id}))
    # adds to array in db
    mongo.db.recipes.update(
        {"_id": ObjectId(recipe_id)},
        {'$addToSet': {"rating": userRating}})
    flash("RECIPE RATED SUCCESSFULLY")

    return redirect(url_for("view_recipe", recipe_id=recipe_id, currentRating=currentRating))


# filters

# filters so only vegan recipes are shown
@app.route("/vegan")
def vegan_filter():
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find({"vegan": "Yes"}))

    return render_template("recipes.html", types=types,
                           recipes=recipes)


# # filters so items with most reviews are shown
# @app.route("/most_popular")
# def most_popular_filter():

#     new = list(mongo.db.recipes.find().sort("rating", 1))

#     return render_template("recipes.html",
#                            new=new)


#  filters so all recipes are shown
@app.route("/all_recipes")
def all_filter():
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    return render_template("recipes.html",
                           recipes=recipes, types=types)


#  filters so most popular recipes are shown
@app.route("/random")
def random():
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.aggregate([{'$sample': {'size': 1}}]))
    return render_template("recipes.html",
                           recipes=recipes, types=types)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
