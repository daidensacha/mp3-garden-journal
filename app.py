
import os
import pandas as pd
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from forms import ContactForm
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
# app.config.from_object('config.Config')

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.context_processor
def inject_user():
    username = ""
    if 'user' in session:
        username = session["user"]
        user = mongo.db.users.find_one({"username": session["user"]})
        user.pop("password")
        return dict(username=username, user=user)
    else:
        username = ""
        user = ""
        return dict(username=username, user=user)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if request.method == "POST":
        if not form.validate_on_submit():
            flash("Failed validation", "error")
            return render_template('contact.html', form=form)
        if form.validate_on_submit():
            firstname = form.firstname.data
            lastname = form.lastname.data
            email = form.email.data
            message = form.message.data

            form_message = {
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "message": message,
                "created_at": datetime.now()
            }
            mongo.db.messages.insert_one(form_message)
            flash("Message has been sent.", "success")
            return redirect(url_for("contact"))

    return render_template('contact.html', form=form)


@app.route("/messages")
def messages():
    if "user" in session and session["user"] == "admin":
        messages = list(mongo.db.messages.find().sort("created_at"))
        return render_template('messages.html', messages=messages)
    else:
        flash("Please log in to view page.", "error")
        return redirect(url_for("login"))


@app.route("/delete_message/<message_id>")
def delete_message(message_id):
    messages = list(mongo.db.messages.find().sort("created_at"))
    mongo.db.messages.remove({"_id": ObjectId(message_id)})
    flash("Message Successfuly Deleted", "success")
    return redirect(url_for("messages", messages=messages))


@app.route("/get_garden_events")
def get_garden_events():
    if "user" in session:
        # define the empty list first
        garden_events = []
        plants = []
        categories = []
        events_months = []
        # distinguish if admin or normal user
        if session["user"] == "admin":
            garden_events = list(
                mongo.db.garden_events.find().sort("occurs_at"))
            plants = list(mongo.db.plants.find())
            categories = list(
                mongo.db.categories.find().sort("category", 1))
            events_months = list(
                mongo.db.garden_events.find().sort("month"))
        else:
            garden_events = list(
                mongo.db.garden_events.find(
                    {"created_by": session["user"]}).sort("occurs_at"))
            plants = list(mongo.db.plants.find(
                {"created_by": session["user"]}))
            categories = list(
                mongo.db.categories.find(
                    {"created_by": session["user"]}).sort("category"))
            events_months = list(
                mongo.db.garden_events.find(
                    {"created_by": session["user"]}).sort("month"))
        if not garden_events:
            flash(
                "Add plants, categories and events to populate this page.",
                "info")
        return render_template("journal.html", plants=plants,
                               garden_events=garden_events,
                               categories=categories,
                               events_months=events_months)
    else:
        flash("Please log in to view page.", "error")
        return redirect(url_for("login"))


@app.route("/get_plants")
def get_plants():
    if "user" in session:
        plants = []
        # distinguish if admin or normal user
        if session["user"] == "admin":
            plants = list(mongo.db.plants.find().sort("type"))
        else:
            plants = list(mongo.db.plants.find(
                {"created_by": session["user"]}).sort("type"))
        if not plants:
            flash("Add plants to populate this page.", "info")
        return render_template("plants.html", plants=plants)
    else:
        flash("Please log in to view page.", "error")
        return redirect(url_for("login"))


@app.route("/search", methods=["GET", "POST"])
def search():
    if "user" in session:
        query = request.form.get("query")
        categories = list(mongo.db.categories.find(
            {"$text": {"$search": query}}))
        plants = list(mongo.db.plants.find(
            {"$text": {"$search": query}}))
        garden_events = list(mongo.db.garden_events.find(
            {"$text": {"$search": query}}).sort("occurs_at"))

        return render_template("journal.html",
                               garden_events=garden_events,
                               categories=categories,
                               plants=plants)
    else:
        flash("Please log in to view page.", "error")
        return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username"),
            "firstname": request.form.get("firstname"),
            "lastname": request.form.get("lastname"),
            "email": request.form.get("email"),
            "registered": datetime.now(),
            "password": generate_password_hash(
                request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!", "success")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get(
                        "password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    existing_user["firstname"]), "default")
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password", "error")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password", "error")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    if "user" in session:
        users = list(mongo.db.users.find().sort("username"))
        user_profile = []
        for user in users:
            # check if user logged in, and matches user logged in.
            if "user" in session and (user["username"] == session["user"]):
                user_profile.append(user)
        # get session users username from db
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        if session["user"]:
            return render_template("profile.html", username=username,
                                   user_profile=user_profile)
    else:
        flash("Please log in for access.", "error")
        return redirect(url_for("login", ))


@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    if "user" in session:
        existing_user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if request.method == "POST":
            if existing_user:
                if check_password_hash(
                            existing_user["password"], request.form.get(
                                "old_password")):
                    # flash("Password validation passed", "success")
                    email = request.form.get("email")
                    if email is not None:
                        update = {
                            "email": request.form.get("email"),
                            "firstname": request.form.get("firstname"),
                            "lastname": request.form.get("lastname"),
                        }
                        mongo.db.users.update_one(
                            {"_id": ObjectId(user_id)}, {"$set": update})
                        flash("The information has been updated successfully.",
                              "success")
                        return redirect(url_for(
                            "profile", username=session["user"]))
                else:
                    flash("Please confirm the correct password.", "error")
                    return redirect(url_for("edit_profile", user_id=user_id))
        return render_template(
            "edit_profile.html", existing_user=existing_user)
    else:
        flash("Please log in for access.", "error")
        return redirect(url_for("login", ))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out", "default")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    if "user" in session:
        if request.method == "POST":
            date_string = request.form.get("occurs_at")
            date_object = pd.to_datetime(date_string)
            event_plant_id = request.form.get("event_plant_id")
            month = date_object.strftime("%B")

            event = {
                "category": request.form.get("category"),
                "event_plant_id": ObjectId(event_plant_id),
                "name": request.form.get("name"),
                "repeats": request.form.get("repeats"),
                "occurs_at": date_object,
                "month": month,
                "notes": request.form.get("notes"),
                "created_by": session["user"]
            }
            mongo.db.garden_events.insert_one(event)
            flash("Event Successfully Added", "success")
            return redirect(url_for("get_garden_events"))

        plants = []
        categories = []
        # distinguish if admin or normal user
        if session["user"] == "admin":
            plants = list(mongo.db.plants.find().sort("type"))
            categories = mongo.db.categories.find().sort("category", 1)
        else:
            plants = list(mongo.db.plants.find(
                {"created_by": session["user"]}).sort("type"))
            categories = list(mongo.db.categories.find(
                {"created_by": session["user"]}).sort("category"))
            # Check if categories and plants to create event
            if not categories and not plants:
                flash("Please enter categories and"
                      " plants before entering an event", "info")
            if categories and not plants:
                flash("Please enter plants before entering an event", "info")
            if plants and not categories:
                flash("Please enter categories before"
                      " entering an event", "info")
                return render_template(
                    "add_event.html", categories=categories, plants=plants)

        return render_template(
            "add_event.html", categories=categories, plants=plants)
    else:
        flash("Please log in to view page", "error")
        return redirect(url_for("login"))


@app.route("/edit_event/<event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    if "user" in session:
        if request.method == "POST":
            date_string = request.form.get("occurs_at")
            date_object = pd.to_datetime(date_string)
            month = date_object.strftime("%B")
            # Store plant ObjectId string in variable
            event_plant_id = request.form.get("event_plant_id")

            submit = {
                "category": request.form.get("category"),
                # Creates an object from the string to send to collection
                "event_plant_id": ObjectId(event_plant_id),
                "name": request.form.get("name"),
                "repeats": request.form.get("repeats"),
                "occurs_at": date_object,
                "month": month,
                "notes": request.form.get("notes"),
                "created_by": session["user"]
            }
            mongo.db.garden_events.update({"_id": ObjectId(event_id)}, submit)
            flash("Event Successfully Updated", "success")
            return redirect(url_for("get_garden_events"))

        garden_event = mongo.db.garden_events.find_one(
            {"_id": ObjectId(event_id)})

        garden_events = list(mongo.db.garden_events.find().sort("occurs_at"))

        plants = []
        categories = []
        # distinguish if admin or normal user to populate list accordingly
        if session["user"] == "admin":
            plants = list(mongo.db.plants.find().sort("type"))
            categories = mongo.db.categories.find().sort("category", 1)
        else:
            plants = list(mongo.db.plants.find(
                {"created_by": session["user"]}).sort("type"))
            categories = list(mongo.db.categories.find(
                {"created_by": session["user"]}).sort("category"))

        if not plants:
            flash("Create plants to populate this page.", "info")

        return render_template(
            "edit_event.html", plants=plants, garden_events=garden_events,
            garden_event=garden_event, categories=categories)
    else:
        flash("Please log in to view page", "error")
        return redirect(url_for("login"))


@app.route("/delete_event/<event_id>")
def delete_event(event_id):
    if "user" in session:
        mongo.db.garden_events.remove({"_id": ObjectId(event_id)})
        flash("Event Successfuly Deleted", "success")
        return redirect(url_for("get_garden_events"))
    else:
        flash("Please log in to view page.", "error")
        return redirect(url_for("login"))


@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    if "user" in session:
        if request.method == "POST":
            sowing_date_string = request.form.get("sow_at")
            planting_date_string = request.form.get("plant_at")
            harvest_from_string = request.form.get("harvest_from")
            harvest_to_string = request.form.get("harvest_to")
            if sowing_date_string == "":
                sowing_date_object = sowing_date_string
            else:
                sowing_date_object = pd.to_datetime(sowing_date_string)

            if planting_date_string == "":
                planting_date_object = planting_date_string
            else:
                planting_date_object = pd.to_datetime(planting_date_string)
            if harvest_from_string == "":
                harvest_from_object = harvest_from_string
            else:
                harvest_from_object = pd.to_datetime(harvest_from_string)
            if harvest_to_string == "":
                harvest_to_object = harvest_to_string
            else:
                harvest_to_object = pd.to_datetime(harvest_to_string)
            # harvest_from_object = pd.to_datetime(harvest_from_string)
            # harvest_to_object = pd.to_datetime(harvest_to_string)

            plant = {
                "type": request.form.get("type"),
                "name": request.form.get("name"),
                "sow_at": sowing_date_object,
                "plant_at": planting_date_object,
                "harvest_from": harvest_from_object,
                "harvest_to": harvest_to_object,
                "fertilise": request.form.get(
                    "fertilise"),
                "fertiliser": request.form.get("fertiliser"),
                "notes": request.form.get("notes"),
                "created_by": session["user"]
            }
            mongo.db.plants.insert_one(plant)
            flash("Plant Successfully Added", "success")
            return redirect(url_for("get_plants"))

        return render_template("add_plant.html")
    else:
        flash("Please log in to view page", "error")
        return redirect(url_for("login"))


@app.route("/edit_plant/<plant_id>", methods=["GET", "POST"])
def edit_plant(plant_id):
    if "user" in session:
        if request.method == "POST":
            sowing_date_string = request.form.get("sow_at")
            planting_date_string = request.form.get("plant_at")
            harvest_from_string = request.form.get("harvest_from")
            harvest_to_string = request.form.get("harvest_to")
            if sowing_date_string == "":
                sowing_date_object = sowing_date_string
            else:
                sowing_date_object = pd.to_datetime(sowing_date_string)
            if planting_date_string == "":
                planting_date_object = planting_date_string
            else:
                planting_date_object = pd.to_datetime(planting_date_string)
            if harvest_from_string == "":
                harvest_from_object = harvest_from_string
            else:
                harvest_from_object = pd.to_datetime(harvest_from_string)
            if harvest_to_string == "":
                harvest_to_object = harvest_to_string
            else:
                harvest_to_object = pd.to_datetime(harvest_to_string)
            # harvest_from_object = pd.to_datetime(harvest_from_string)
            # harvest_to_object = pd.to_datetime(harvest_to_string)

            submit = {
                "type": request.form.get("type"),
                "name": request.form.get("name"),
                "sow_at": sowing_date_object,
                "plant_at": planting_date_object,
                "harvest_from": harvest_from_object,
                "harvest_to": harvest_to_object,
                "fertilise": request.form.get(
                    "fertilise"),
                "fertiliser": request.form.get("fertiliser"),
                "notes": request.form.get("notes"),
                "created_by": session["user"]
            }
            mongo.db.plants.update({"_id": ObjectId(plant_id)}, submit)
            flash("Plant Successfully Updated", "success")
            return redirect(url_for("get_plants"))

        plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})

        plants = list(mongo.db.plants.find().sort("type"))
        return render_template("edit_plant.html", plants=plants, plant=plant)
    else:
        flash("Please log in to view page.", "error")
        return redirect(url_for("login"))


@app.route("/delete_plant/<plant_id>")
def delete_plant(plant_id):
    check_events = mongo.db.garden_events.find_one(
                        {"event_plant_id": ObjectId(plant_id)})
    if not check_events:
        if "user" in session:
            mongo.db.plants.remove({"_id": ObjectId(plant_id)})
            flash("Plant Successfuly Deleted", "success")
            return redirect(url_for("get_plants"))
        else:
            flash("Please log in to view page.", "error")
            return redirect(url_for("login"))
    else:
        flash("Plants with related events cannot be deleted", "error")
        return redirect(url_for("get_plants"))


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if "user" in session:
        if request.method == "POST":
            new_category = {
                "category": request.form.get("category"),
                "created_by": session["user"]
            }
            mongo.db.categories.insert_one(new_category)
            flash("New Category Successfully Added", "success")
            return redirect(url_for("add_category"))

        # Define the empty list first
        categories = []
        # Distinguish if admin or normal user and filter list accordingly
        if session["user"] == "admin":
            categories = list(mongo.db.categories.find().sort(
                              "category"))
        else:
            categories = list(mongo.db.categories.find(
                              {"created_by": session["user"]}).sort(
                                  "category"))
        if not categories:
            flash("Add event categories to populate this list.", "info")
        return render_template(
            "add_category.html", categories=categories)
    else:
        flash("Please log in to view page", "error")
        return redirect(url_for("login"))


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if "user" in session:
        if request.method == "POST":
            submit = {
                "category": request.form.get("category"),
                "created_by": session["user"]
            }
            mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
            flash("Category Successfully Updated", "success")
            return redirect(url_for("add_category"))

        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})

        # Get list of all categories filtered by session user
        categories = list(mongo.db.categories.find(
                            {"created_by": session["user"]}).sort("category"))

        return render_template(
            "edit_category.html", categories=categories, category=category)
    else:
        flash("Please log in to view page.", "error")
        return redirect(url_for("login"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    # get category from categories
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    # Check if garden events uses this category
    check_events = mongo.db.garden_events.find_one(
                        {"category": category["category"]})
    # if variable is empty, run function, otherwise stop deletion. 
    if not check_events:
        if "user" in session:
            mongo.db.categories.remove({"_id": ObjectId(category_id)})
            flash("Category Successfuly Deleted", "success")
            return redirect(url_for("add_category"))
        else:
            flash("Please log in to view page.", "error")
            return redirect(url_for("login"))
    else:
        flash("Categories with related events cannot be deleted", "error")
        return redirect(url_for("add_category"))


@app.errorhandler(404)
def page_not_found(error):
    flash("Error, the page was not found.", "danger")
    return render_template("404.html"), 404


@app.errorhandler(405)
def method_not_allowed(error):
    flash("Method Not Allowed.", "danger")
    return render_template("405.html"), 405


@app.errorhandler(500)
def server_error(error):
    flash("Server Error", "danger")
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
