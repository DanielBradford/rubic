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


@app.errorhandler(404)
def not_found(e):
    user = session.get('user', 'Guest')
    return render_template("404.html", user=user), 404


@app.route("/")
def home():
    """takes visitor to landing page"""
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    users = list(mongo.db.users.find().sort("user_name", 1))
    session['user'] = "Guest"
    return render_template("landing.html", types=types,
                           recipes=recipes, users=users)


@app.route("/search", methods=["POST"])
def search():
    """function to allow user to search for recipes based
    on recipe_name and ingredients index"""
    search = request.form.get("search")
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find({"$text": {"$search": search}}))
    flash("{} Results for '{}'".format(len(recipes), search))
    return render_template("recipes.html", recipes=recipes, types=types)


@app.route("/search_saved", methods=["GET", "POST"])
def search_saved():
    """function to allow user to search for recipes based
    on recipe_name and ingredients index"""
    user = session.get('user', 'Guest')
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


@app.route("/my_recipes")
def my_recipes():
    """displays recipes only created by current user"""
    # prevent users to cross to other clients recipe page
    user = session.get('user', 'Guest')
    if user != 'Guest':
        this_user = mongo.db.users.find_one({"user_name": user})
        recipes = list(mongo.db.recipes.find({"created_by": user}))

        return render_template("my_recipes.html",
                               recipes=recipes, this_user=this_user)
    else:
        types = list(mongo.db.type.find().sort("type_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
        users = list(mongo.db.users.find().sort("user_name", 1))
        # warning message to non admin users
        flash("MEMBERS ONLY! PLEASE REGISTER OR LOGIN FOR FULL ACCESS!")
        return render_template('landing.html',
                               types=types, recipes=recipes, users=users)


@app.route("/products")
def products():
    """function displays amazon products recommended, 
    Scope for monetising the app, 
    discount code only shown to logged in users"""
    user = session.get('user', 'Guest')
    if user != "Guest":
        products = list(
            mongo.db.products.find().sort("product_name", 1))
        tools = list(mongo.db.tools.find().sort("name", 1))

        return render_template("products.html", tools=tools, products=products)
    else:
        types = list(mongo.db.type.find().sort("type_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
        users = list(mongo.db.users.find().sort("user_name", 1))
        # warning message to non admin users
        flash("MEMBERS ONLY! PLEASE REGISTER OR LOGIN FOR FULL ACCESS!")
        return render_template('landing.html',
                               types=types, recipes=recipes, users=users)


@ app.route("/manage")
def manage():
    """Presents a dashboard/suite for the admin user to manage data"""
    # prevents non admin users accessing management template
    user = session.get('user', 'Guest')
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
                           users=users, recipes=recipes, types=types,
                           products=products, tools=tools)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Logs the user into their profile and allows full access"""
    user = session.get('user', 'Guest')
    if user == "Guest":
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
                    if session["user"] == "admin":
                        return redirect(url_for("manage",
                                                user=session["user"]))
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
    # Defensive programming if user is logged in already
    else:
        flash("YOU WERE ALREADY LOGGED IN!")
        return redirect(url_for('profile'))

# logs user out of appplication


@app.route('/logout')
def logout():
    # remove user session from cookies
    session.pop("user")
    flash("You have been logged out")
    return redirect(url_for("home"))


@app.route("/register")
def register():
    """takes user to registrating page"""
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
    """Presents a full recipe to user. The option to save, rate, edit and delete,
    varies upon the user accessing the recipe"""
    user = session.get('user', 'Guest')
    if session['user']:
        # checks recipe id is valid
        if len(recipe_id) == 24:
            recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
            recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
            types = list(mongo.db.type.find().sort("type_name", 1))
            user = session['user']
            guest = "Guest"
            user_id = mongo.db.users.find_one({"user_name": user})
            saved_list = list(mongo.db.users.distinct(
                "saved_recipes", {"user_name": user}))
            products = list(mongo.db.products.find().sort("product_name", 1))

            return render_template("view_recipe.html",
                                   recipe=recipe, recipes=recipes,
                                   user_id=user_id, user=user,
                                   saved_list=saved_list,
                                   types=types, products=products,
                                   guest=guest)
        else:
            flash("Sorry. The recipe you are looking for does not exist.")
            return redirect(url_for('recipes'))

    user = "Guest"
    recipe_id = recipe_id
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    types = list(mongo.db.type.find().sort("type_name", 1))
    user_id = mongo.db.users.find_one({"user_name": user})
    saved_list = list(mongo.db.users.distinct(
        "saved_recipes", {"user_name": user}))
    products = list(mongo.db.products.find().sort("product_name", 1))

    return render_template("view_recipe.html", recipe=recipe,
                           recipes=recipes, user_id=user_id,
                           user=user, saved_list=saved_list,
                           types=types, products=products)


@app.route("/add_recipe")
def add_recipe():
    """routes user to the add recipe form template"""
    user = session.get('user', 'Guest')
    if user != "Guest":
        types = list(mongo.db.type.find().sort("type_name", 1))
        products = list(mongo.db.products.find().sort("product_name", 1))
        return render_template("add_recipe.html",
                               types=types, products=products)
    else:
        flash("MEMBERS ONLY! PLEASE REGISTER OR LOGIN FOR FULL ACCESS!")
        return redirect(url_for('home'))


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    """adds new user to users collection in db"""
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
            "password": generate_password_hash(request.form.get
                                               ("password")),
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
            flash("Username should be under 15 characters")
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


@app.route("/profile")
def profile():
    user = session.get('user', 'Guest')
    if user != "Guest":
        this_user = mongo.db.users.find_one({"user_name": user})

        return render_template("profile.html", this_user=this_user)
    else:
        flash("MEMBERS ONLY! PLEASE REGISTER OR LOGIN FOR FULL ACCESS!")
        return redirect(url_for('home'))


@app.route("/add_new_recipe", methods=["GET", "POST"])
def add_new_recipe():
    # add new recipe to the database
    user = session.get('user', 'Guest')
    if user != "Guest":
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

            # form validation
            recipe_name = request.form.get("recipe_name")
            if len(recipe_name) > 30:
                flash("Recipe name cannot be longer than 30 characters")
                return redirect(url_for('add_new_recipe'))
            if len(recipe_name) == 0:
                flash("Recipe name must be filled for registration")
                return redirect(url_for("add_recipe"))
            ingredients = request.form.get("ingredients")
            if len(ingredients) > 100:
                flash("""Ingredients over 100 character limit.
            Please condense and re-submit""")
                return redirect(url_for("recipes"))
            method = request.form.get("method")
            if len(method) > 200:
                flash("""Method over 200 character limit.
                Please condense and re-submit""")
                return redirect(url_for("recipes"))

            # increments the contribution count of user
            mongo.db.users.update({"user_name": session["user"]},
                                  {"$inc": {"contributed": 1}}
                                  )
            this_type = request.form.get("type")
            # increments recipe type count
            mongo.db.type.update({"type_name": this_type},
                                 {"$inc": {"count": 1}})
            # adds new recipe to recipes collection
            mongo.db.recipes.insert_one(new)
            flash("Recipe Successfully Added")
            return redirect(url_for("recipes"))
        return render_template("add_recipe.html")
    else:
        # warning message to non admin users
        flash("MEMBERS ONLY! PLEASE REGISTER OR LOGIN FOR FULL ACCESS!")
        return redirect(url_for('home'))



@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """function to edit the chosen recipe"""
    user = session.get('user', 'Guest')
    if user != "Guest":

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
            recipe_name = request.form.get("recipe_name")
            if len(recipe_name) > 30:
                flash("Recipe name cannot be longer than 30 characters")
                return redirect(url_for('edit_recipe'))
            if len(recipe_name) == 0:
                flash("Recipe name must be filled for registration")
                return redirect(url_for("edit_recipe"))
            ingredients = request.form.get("ingredients")
            if len(ingredients) > 150:
                flash(
                    """Ingredients over 150 character limit.
                    Please condense and re-submit""")
                return redirect(url_for("recipes"))
            method = request.form.get("method")
            if len(method) > 200:
                flash("""Method over 200 character limit.
                Please condense and re-submit""")
                return redirect(url_for("recipes"))
            ingredients = request.form.get("ingredients"),
            if len(ingredients) > 100:
                flash(
                    """Ingredients over 100 character limit.
                    Please condense and re-submit""")
                return redirect(url_for("recipes"))
            vegan = vegan,
            method = request.form.get("method"),
            if len(method) > 250:
                flash("Method over 250 character limit. Please condense")
                return redirect(url_for("recipes"))
            # check recipe exists if not 404 page

            mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, new)
            flash("RECIPE SUCCESSFULLY UPDATED")
            return redirect(url_for("recipes"))
        return render_template("edit_recipe.html", recipe=recipe,
                               recipes=recipes, types=types,
                               recipe_id=recipe_id, products=products)
    else:
        types = list(mongo.db.type.find().sort("type_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
        # warning message to non admin users
        flash("MEMBERS ONLY! PLEASE REGISTER OR LOGIN FOR FULL ACCESS!")
        return redirect(url_for('home'))



@app.route("/save_recipe/<recipe_id>", methods=["GET", "POST"])
def save_recipe(recipe_id):
    """function to allow user to save chosen recipe"""
    # gets current user
    user = session.get('user', 'Guest')
    # appends the chosen recipe_id to current user document in db
    mongo.db.users.update(
        {"user_name": user},
        {'$addToSet': {'saved_recipes': ObjectId(recipe_id)}})
    flash("RECIPE SAVED SUCCESSFULLY")
    return redirect(url_for("view_recipe", recipe_id=recipe_id))


@app.route("/saved_recipes", methods=["GET", "POST"])
def saved_recipes():
    """function to view all saved recipes of current user"""
    # checks current user
    user = session.get('user', 'Guest')
    # checks if user is guest or registered member
    if user != "Guest":
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
        return render_template("saved_recipes.html", recipes=recipes,
                               user=user, this=this, check_list=check_list,
                               size=size)
    else:
        flash("MEMBERS ONLY! PLEASE REGISTER OR LOGIN FOR FULL ACCESS!")
        return redirect(url_for('home'))


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """deletes the chosen recipe entirely from the database"""
    # backend check the user is logged in
    user = session.get('user', 'Guest')
    if user != "Guest":
        recipe = mongo.db.recipes.distinct("created_by",
                                           {"_id": ObjectId(recipe_id)})
        for i in recipe:
            if str(i) == user:
                types = mongo.db.recipes.distinct(
                    "type", {"_id": ObjectId(recipe_id)})
                for i in types:
                    mongo.db.type.update({"type_name": i},
                                         {"$inc": {"count": -1}})
                # javascript confirm confirms this action on frontend
                mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
                # contributed amount is reduced by 1
                mongo.db.users.update({"user_name": user},
                                      {"$inc": {"contributed": -1}})
                flash("Recipe Successfully Deleted")
                # check recipe exists if not 404 page
                # defensive programming verify owner login in required
                if user == "admin":
                    return redirect(url_for('manage'))

                return redirect(url_for("my_recipes"))
            else:
                types = list(mongo.db.type.find().sort("type_name", 1))
                recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
                users = list(mongo.db.users.find().sort("user_name", 1))
                # warning message to non admin users
                flash("This is not your recipe. You cannot delete!")
                return render_template("landing.html",
                                       users=users, recipes=recipes,
                                       types=types)

    else:
        types = list(mongo.db.type.find().sort("type_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
        users = list(mongo.db.users.find().sort("user_name", 1))
        # warning message to non admin users
        flash("MEMBERS ONLY! Authorization denied!")
        return render_template("landing.html",
                               users=users, recipes=recipes, types=types)


@app.route("/remove_recipe/<recipe_id>")
def remove_recipe(recipe_id):
    """removes the recipe from the users saved list"""
    # check if user in session (login check)
    user = session["user"]
    saved_list = list(mongo.db.users.distinct(
        "saved_recipes", {"user_name": user}))

    for item in saved_list:
        if item == ObjectId(recipe_id):
            mongo.db.users.update(
                {"user_name": user},
                {"$pull":  {'saved_recipes': ObjectId(recipe_id)}}
            )

            flash("Recipe successfully removed from saved list")
            return redirect(url_for('saved_recipes', user=user))
        else:
            flash("FAILED TO REMOVE")
            return redirect(url_for('saved_recipes', user=user))

    return redirect(url_for('saved_recipes', user=user))


@app.route("/add_rating/<recipe_id>", methods=["POST", "GET"])
def add_rating(recipe_id):
    """adds rating to the rating array in recipes db"""
    userRating = int(request.form.get("rating"))
    # gets the existing array
    currentRating = list(mongo.db.recipes.distinct(
        "rating", {"_id": recipe_id}))
    # adds to array in db
    mongo.db.recipes.update(
        {"_id": ObjectId(recipe_id)},
        {'$addToSet': {"rating": userRating}})
    flash("RECIPE RATED SUCCESSFULLY")

    return redirect(url_for("view_recipe",
                            recipe_id=recipe_id, currentRating=currentRating))


# filters

@app.route("/vegan")
def vegan_filter():
    """filters so only vegan recipes are shown"""
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find({"vegan": "Yes"}))

    return render_template("recipes.html", types=types,
                           recipes=recipes)


@app.route("/all_recipes")
def all_filter():
    """filters so all recipes are shown"""
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    return render_template("recipes.html",
                           recipes=recipes, types=types)


@app.route("/random")
def random():
    """filters so most popular recipes are shown"""
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.aggregate([{'$sample': {'size': 1}}]))
    return render_template("recipes.html",
                           recipes=recipes, types=types)


# MANAGEMENT FUNCTIONS

@app.route("/delete_recipe_type/<type_id>")
def delete_recipe_type(type_id):
    """delete recipe types"""
    # gets current user
    user = session.get('user', 'Guest')
    if user == "admin":
        types = list(mongo.db.type.find().sort("type_name", 1))
        users = list(mongo.db.users.find().sort("last_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

        # verifies if an item in that category exists and prevents deletion
        checkType = list(mongo.db.type.distinct("count",
                                                {"_id": ObjectId(type_id)}))
        for i in checkType:
            if i == 0:
                mongo.db.type.remove({"_id": ObjectId(type_id)})
                flash("Recipe Type Successfully Deleted")
                return redirect(url_for('manage'))
        flash("RECIPE TYPE CANNOT BE DELETED! RECIPES EXIST WITH THIS TYPE")
        return render_template("management.html", recipes=recipes,
                               types=types, users=users)
    else:
        flash("UNAUTHORISED ACCESS!")
        return redirect(url_for("home"))


@ app.route("/add_recipe_type", methods=["GET", "POST"])
def add_recipe_type():
    """add recipe types"""
    types = list(mongo.db.type.find().sort("type_name", 1))
    users = list(mongo.db.users.find().sort("last_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

    if request.method == "POST":
        new_type = {
            "type_name": request.form.get("type_name"),
            "type_desc": request.form.get("type_desc"),
            "count": 0
        }

        type_name = request.form.get("type_name")
        if len(type_name) == 0:
            flash("Type name must be given")
            return redirect(url_for('add_recipe_type'))
        if len(type_name) > 50:
            flash("Type name too long. Over 50 character limit")
            return redirect(url_for('add_recipe_type'))
        type_desc = request.form.get("type_desc")
        if len(type_desc) == 0:
            flash("Type desctipiton must be given")
            return redirect(url_for('add_recipe_type'))
        if len(type_desc) > 150:
            flash("Type name too long. Over 150 character limit")
            return redirect(url_for('add_recipe_type'))

        mongo.db.type.insert_one(new_type)
        flash("Type Successfully Added")
        return redirect(url_for('manage'))

    flash("Failed to add recipe type")
    return render_template("management.html/",
                           recipes=recipes, types=types, users=users)


@ app.route("/add_tool", methods=["GET", "POST"])
def add_tool():
    """adding tools"""
    user = session.get('user', 'Guest')
    # verifies current user is admin
    if user == "admin":
        types = list(mongo.db.type.find().sort("type_name", 1))
        users = list(mongo.db.users.find().sort("last_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

        if request.method == "POST":
            new_tool = {
                "name": request.form.get("tool_name"),
                "url": request.form.get("url"),
                "image": request.form.get("image_url"),
                "desc": request.form.get("tool_desc"),
                "price": request.form.get("price")
            }

            mongo.db.tools.insert_one(new_tool)
            flash("Tool Successfully Added")
            return redirect(url_for('manage'))

        flash("Failed to add tool")
        return render_template("management.html/", recipes=recipes,
                               types=types, users=users)
    else:
        types = list(mongo.db.type.find().sort("type_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
        users = list(mongo.db.users.find().sort("user_name", 1))
        # warning message to non admin users
        flash("ADMIN ONLY! Authorization denied!")
        return render_template("landing.html",
                               users=users, recipes=recipes, types=types)


@ app.route("/add_product", methods=["GET", "POST"])
def add_product():
    """adding products"""
    # verifies current user is admin
    user = session.get('user', 'Guest')
    if user == "admin":
        types = list(mongo.db.type.find().sort("type_name", 1))
        users = list(mongo.db.users.find().sort("last_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))

        if request.method == "POST":
            new_product = {
                "product_name": request.form.get("product_name"),
                "url": request.form.get("url"),
                "image_url": request.form.get("image_url"),
                "product_desc": request.form.get("product_desc"),
                "price": request.form.get("price")
            }

            mongo.db.products.insert_one(new_product)
            flash("Product Successfully Added")
            return redirect(url_for('manage'))

        flash("Failed to add product")
        return render_template("management.html/",
                               recipes=recipes, types=types, users=users)
    else:
        types = list(mongo.db.type.find().sort("type_name", 1))
        recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
        users = list(mongo.db.users.find().sort("user_name", 1))
        # warning message to non admin users
        flash("ADMIN ONLY! Authorization denied!")
        return render_template("landing.html",
                               users=users, recipes=recipes, types=types)


@ app.route("/user_search", methods=["GET", "POST"])
def user_search():
    """User search function to allow admin to search for users based
    on username and last name"""
    search = request.form.get("search")
    types = list(mongo.db.type.find().sort("type_name", 1))
    recipes = list(mongo.db.recipes.find().sort("recipe_name", 1))
    users = list(mongo.db.users.find({"$text": {"$search": search}}))
    products = list(
        mongo.db.products.find().sort("product_name", 1))
    tools = list(mongo.db.tools.find().sort("name", 1))
    count = len(users)
    # checks if no users match search
    if count == 0:
        flash("NO USERS FOUND")
        return render_template("management.html", users=users, types=types,
                               recipes=recipes, count=count, search=search)
    # returns results that match
    else:
        flash("Search results: {} for '{}'".format(len(users), search))
        return render_template("management.html", users=users, types=types,
                               recipes=recipes, count=count, search=search,
                               tools=tools, products=products)


@ app.route("/delete_user/<username>")
def delete_user(username):
    """deleting records"""
    # validate the user is admin
    user = session.get('user', 'Guest')
    if user == "admin":
        # javascript confirm confirms this action on frontend
        mongo.db.users.remove({"user_name": username})
        flash("User Successfully Deleted")
        # check user exists if not 404 page
        # defensive programming verify admin possibly with password
        return redirect(url_for("manage"))
    else:
        flash("UNAUTHORISED ACCESS!")
        return redirect(url_for("home"))


@ app.route("/delete_product/<product>")
def delete_product(product):
    # validate the user is admin
    user = session.get('user', 'Guest')
    if user == "admin":
        # javascript confirm confirms this action on frontend
        mongo.db.products.remove({"_id": ObjectId(product)})
        flash("Product Successfully Deleted")
        # check user exists if not 404 page
        # defensive programming verify admin possibly with password
        return redirect(url_for("manage"))
    else:
        flash("UNAUTHORISED ACCESS!")
        return redirect(url_for("home"))


@ app.route("/delete_tool/<tool>")
def delete_tool(tool):
    # validate the user is admin
    user = session.get('user', 'Guest')
    if user == "admin":
        # javascript confirm confirms this action on frontend
        mongo.db.tools.remove({"_id": ObjectId(tool)})
        flash("Tool Successfully Deleted")
        # check user exists if not 404 page
        # defensive programming verify admin possibly with password
        return redirect(url_for('manage'))
    flash("UNAUTHORISED ACCESS!")
    return redirect(url_for("home"))


# EDIT RECORDS
@ app.route("/edit_user/<user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    current_user = session.get('user', 'Guest')
    if current_user == "admin":
        # gets chosen user
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if request.method == "POST":
            vegan = "Yes" if request.form.get("vegan") else "No"
            edit = {
                "user_name": request.form.get("user_name"),
                "first_name": request.form.get("first_name"),
                "last_name": request.form.get("last_name"),
                "email": request.form.get("email"),
                "vegan": vegan,
                "password": user["password"],
                # maintains uneffected
                "contributed": user["contributed"],
                "saved_recipes": user["saved_recipes"]
            }

            # validation defensive programming
            existing_user = mongo.db.users.find_one(
                {"user_name": request.form.get("user_name").lower()})

            if existing_user:
                flash("Username taken. Please choose another")
                return redirect("edit_user")

            password = request.form.get("password")
            confirm = request.form.get("confirm")
            if password != confirm:
                flash("Passwords do not match")
                return render_template("edit_user", user=user)
            vegan = vegan,
            mongo.db.users.update({"_id": ObjectId(user_id)}, edit)
            flash("USER SUCCESSFULLY UPDATED")
            return redirect(url_for("manage"))
        return render_template("edit_user.html", user=user)
    else:
        flash("UNAUTHORISED ACCESS!")
        return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
