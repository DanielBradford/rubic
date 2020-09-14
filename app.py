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
    flash("{} Results for '{}'".format(len(recipes), search))
    return render_template("recipes.html", recipes=recipes, types=types)


@app.route("/search_saved", methods=["GET", "POST"])
# function to allow user to search for recipes based
# on recipe_name and ingredients index
def search_saved():
    user = session['user']
    search = request.form.get("search")
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find({"$text": {"$search": search}}))
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
    return render_template("saved_recipes.html", recipes=recipes, types=types,
                           check_list=check_list, size=size, user=user)

# look at pep8 snake case better


# displays recipes only created by current user


@app.route("/my_recipes")
def my_recipes():
    # prevent users to cross to other clients recipe page
    user = session['user']
    recipes = list(mongo.db.recipes.find({"created_by": user}))

    return render_template("my_recipes.html", recipes=recipes, user=user)


@app.route("/products")
def products():
    products = tools = list(mongo.db.products.find().sort("product_name", 1))
    tools = list(mongo.db.tools.find().sort("name", 1))
    return render_template("products.html", tools=tools, products=products)

# function logs user into the app


@app.route("/manage")
def manage():
    user = session["user"]
    # defensive programming to prevent non admin users accessing management template
    if user == "admin":
        users = list(mongo.db.users.find().sort("last_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
        types = list(mongo.db.type.find().sort("type_name", 1))
        products = list(mongo.db.products.find().sort("product_name"))
        tools = list(mongo.db.tools.find().sort("name"))

        # counts the amount of recipes with this recipe type

    else:
        types = list(mongo.db.type.find().sort("type_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
        users = list(mongo.db.users.find().sort("user_name", 1))
        # warning message to non admin users
        flash("ADMIN ONLY! Authorization denied!")
        return render_template("landing.html",
                               users=users, recipes=recipes, types=types)
    return render_template("management.html",
                           users=users, recipes=recipes, types=types, products=products, tools=tools)


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
        types = list(mongo.db.type.find().sort("type_name", 1))
        user = session['user']
        user_id = mongo.db.users.find_one({"user_name": user})
        saved_list = list(mongo.db.users.distinct(
            "saved_recipes", {"user_name": user}))
        products = list(mongo.db.products.find().sort("product_name", 1))

        return render_template("view_recipe.html", recipe=recipe,
                               recipes=recipes, user_id=user_id,
                               user=user, saved_list=saved_list,
                               types=types, products=products)

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
            "saved_recipes": [],
            "contributed": 0
        }

        # defensive programming validation
        first_name = request.form.get("first_name")
        if len(first_name) > 20:
            flash("First Name should be under 20 characters")
            return redirect(url_for("register"))
        #  checks fields are completed before submission
        if len(first_name) == 0:
            flash("First Name must be filled for registration")
            return redirect(url_for("register"))
        last_name = request.form.get("last_name")
        if len(last_name) > 20:
            flash("Last Name should be under 20 characters")
            return redirect(url_for("register"))
        if len(last_name) == 0:
            flash("Last Name must be filled for registration")
            return redirect(url_for("register"))
        email = request.form.get("email")
        if len(email) > 50:
            flash("Email should be under 50 characters")
            return redirect(url_for("register"))
        if len(email) == 0:
            flash("Email must be filled for registration")
            return redirect(url_for("register"))
        user_name = request.form.get("user_name")
        if len(user_name) > 15:
            flash("Email should be under 15 characters")
            return redirect(url_for("register"))
        if len(user_name) == 0:
            flash("Username must be filled for registration")
            return redirect(url_for("register"))
        # password validaton
        password = generate_password_hash(request.form.get("password"))
        if len(password) == 0:
            flash("Both Password fields must be filled for registration")
            return redirect(url_for("register"))
        mongo.db.users.insert_one(register)
        # put new user in session cookie
        session["user"] = request.form.get("user_name")
        flash("Registration Successful!")
        # log user in and take to profile
        return redirect(url_for(
            "profile", user=session["user"]))
    return render_template("landing.html")


@app.route("/profile", methods=["GET", "POST"])
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

        recipe_name = request.form.get("recipe_name"),
        if len(recipe_name) > 30:
            flash("Recipe name cannot be longer than 30 characters")
            return redirect(url_for('add_new_recipe'))
        if len(recipe_name) == 0:
            flash("Recipe name must be filled for registration")
            return redirect(url_for("add_recipe"))
        ingredients = request.form.get("ingredients")
        if len(ingredients) > 100:
            flash("Ingredients over 100 character limit. Please condense and re-submit")
            return redirect(url_for("recipes"))
        vegan = vegan,
        method = request.form.get("method")
        if len(method) > 200:
            flash("Method over 200 character limit. Please condense and re-submit")
            return redirect(url_for("recipes"))

        # validation defensive programming
        # adds new recipe to recipes collection
        mongo.db.users.update({"user_name": session["user"]},
                              {"$inc": {"contributed": 1}}
                              )
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
        recipe_name = request.form.get("recipe_name"),
        recipe_type = request.form.get("type"),
        appliance = request.form.get("appliance"),
        temperature = request.form.get("temperature"),
        cooking_time = request.form.get("time"),
        ingredients = request.form.get("ingredients"),
        if len(ingredients) > 100:
            flash("Ingredients over 100 character limit. Please condense and re-submit")
            return redirect(url_for("recipes"))
        vegan = vegan,
        method = request.form.get("method"),
        if len(method) > 200:
            flash("Method over 200 character limit. Please condense and re-submit")
            return redirect(url_for("recipes"))
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
    if session['user'] == "admin":
        return redirect(url_for('manage'))

    else:
        return redirect(url_for("my_recipes"))


# removes the recipe from the users saved list
@app.route("/remove_recipe/<recipe_id>")
def remove_recipe(recipe_id):
    # check if user in session (login check)
    user = session["user"]
    saved_list = list(mongo.db.users.distinct(
        "saved_recipes", {"user_name": user}))
    recipe_id = ObjectId(recipe_id)

    for item in saved_list:
        if item == recipe_id:
            # pull?
            mongo.db.users.update(
                {"user_name": user},
                {"$pull":  {'saved_recipes': recipe_id}}
            )

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


# MANAGEMENT FUNCTIONS


# deleting recipe types
@app.route("/delete_recipe_type/<type_id>")
def delete_recipe_type(type_id):
    types = list(mongo.db.type.find().sort("type_name", 1))
    users = list(mongo.db.users.find().sort("last_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

    # # verifies if an item in that category exists and prevents deletion
    # for item in types:
    #     for recipe in recipes:
    #         search = list(mongo.db.recipes.find({recipe["type"]: item['type_name']}))
    #         if len(search) > 0:
    #             flash("THIS TYPE HAS RECIPES. CANNOT DELETE!")
    #             return render_template("management.html/",
    #                                 recipes=recipes, types=types, users=users)
    #         elif len(search) == 0:
    #             mongo.db.type.remove({"_id": ObjectId(type_id)})
    #             flash("Recipe Type Successfully Deleted")
    #             return render_template("management.html/", recipes=recipes,
    #                        types=types, users=users)

    return render_template("management.html/", recipes=recipes,
                           types=types, users=users)


# adding recipe types
@app.route("/add_recipe_type", methods=["GET", "POST"])
def add_recipe_type():
    types = list(mongo.db.type.find().sort("type_name", 1))
    users = list(mongo.db.users.find().sort("last_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

    if request.method == "POST":
        new_type = {
            "type_name": request.form.get("type_name"),
            "type_desc": request.form.get("type_desc")
        }

        type_name = request.form.get("type_name")

        type_desc = request.form.get("type_desc")

        mongo.db.type.insert_one(new_type)
        flash("Type Successfully Added")
        return redirect(url_for('manage'))

    flash("Failed to add recipe type")
    return render_template("management.html/", recipes=recipes, types=types, users=users)


# adding tools
@app.route("/add_tool", methods=["GET", "POST"])
def add_tool():
    types = list(mongo.db.type.find().sort("type_name", 1))
    users = list(mongo.db.users.find().sort("last_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

    if request.method == "POST":
        new_product = {
            "name": request.form.get("tool_name"),
            "url": request.form.get("url"),
            "image": request.form.get("image_url"),
            "desc": request.form.get("tool_desc"),
            "price": request.form.get("price")
        }

        mongo.db.products.insert_one(new_product)
        flash("Product Successfully Added")
        return redirect(url_for('manage'))

    flash("Failed to add tool")
    return render_template("management.html/", recipes=recipes,
                           types=types, users=users)

# adding products


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    types = list(mongo.db.type.find().sort("type_name", 1))
    users = list(mongo.db.users.find().sort("last_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

    if request.method == "POST":
        new_tool = {
            "product_name": request.form.get("product_name"),
            "url": request.form.get("url"),
            "image_url": request.form.get("image_url"),
            "product_desc": request.form.get("product_desc"),
            "price": request.form.get("price")
        }

        mongo.db.tools.insert_one(new_tool)
        flash("Product Successfully Added")
        return redirect(url_for('manage'))

    flash("Failed to add product")
    return render_template("management.html/", recipes=recipes, types=types, users=users)


# searches

@app.route("/user_search", methods=["GET", "POST"])
# function to allow user to search for recipes based
# on recipe_name and ingredients index
def user_search():
    search = request.form.get("search")
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    users = list(mongo.db.users.find({"$text": {"$search": search}}))
    count = len(users)
    # checks if no users match search
    if count == 0:
        flash("NO USERS FOUND")
        return render_template("management.html", users=users, types=types, recipes=recipes, count=count, search=search)
    # returns results that match
    else:
        flash("Search results: {} for '{}'".format(len(users), search))
        return render_template("management.html", users=users, types=types, recipes=recipes, count=count, search=search)


# deleting records
@app.route("/delete_user/<username>")
def delete_user(username):
    # validate the user is admin
    if session['user'] == "admin":
        # javascript confirm confirms this action on frontend
        mongo.db.users.remove({"user_name": username})
        flash("User Successfully Deleted")
        # check user exists if not 404 page
        # defensive programming verify admin possibly with password
        return redirect(url_for("manage"))
    else:
        flash("UNAUTHORISED ACCESS!")
        return redirect(url_for("home"))


@app.route("/delete_product/<product>")
def delete_product(product):
    # validate the user is admin
    if session['user'] == "admin":
        # javascript confirm confirms this action on frontend
        mongo.db.products.remove({"product_name": product})
        flash("Product Successfully Deleted")
        # check user exists if not 404 page
        # defensive programming verify admin possibly with password
        return redirect(url_for("manage"))
    else:
        flash("UNAUTHORISED ACCESS!")
        return redirect(url_for("home"))


@app.route("/delete_tool/<tool>")
def delete_tool(tool):
    # validate the user is admin
    if session['user'] == "admin":
        # javascript confirm confirms this action on frontend
        mongo.db.tools.remove({"_id": ObjectId(tool)})
        flash("Tool Successfully Deleted")
        # check user exists if not 404 page
        # defensive programming verify admin possibly with password
        return redirect(url_for("manage"))
    flash("UNAUTHORISED ACCESS!")
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
