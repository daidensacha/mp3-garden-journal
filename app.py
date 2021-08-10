
import os
import pandas as pd
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/get_garden_events")
def get_garden_events():
    garden_events = list(mongo.db.garden_events.find().sort("event_date"))
    plants = list(mongo.db.plants.find())
    categories = list(mongo.db.categories.find().sort("event_category", 1))
    events_months = list(mongo.db.garden_events.find().sort("event_months"))

    user_garden_events = []
    for garden_event in garden_events:
        if (garden_event["created_by"] == session["user"] or
                session["user"] == "admin"):
            user_garden_events.append(garden_event)

    user_plants = []
    for plant in plants:
        if (plant["created_by"] == session["user"] or
                session["user"] == "admin"):
            user_plants.append(plant)

    user_categories = []
    for category in categories:
        if (category["created_by"] == session["user"] or
                session["user"] == "admin"):
            user_categories.append(category)

    user_event_months = []
    for event_month in events_months:
        if (event_month["created_by"] == session["user"] or
                session["user"] == "admin"):
            user_event_months.append(event_month)

    return render_template("journal.html", user_plants=user_plants,
                           user_garden_events=user_garden_events,
                           user_categories=user_categories,
                           user_event_months=user_event_months)


@app.route("/get_plants")
def get_plants():
    plants = list(mongo.db.plants.find().sort("plant_type"))

    user_plants = []
    for plant in plants:
        if (plant["created_by"] == session["user"] or
                session["user"] == "admin"):
            user_plants.append(plant)

    return render_template("plants.html", user_plants=user_plants)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    user_categories = list(mongo.db.categories.find(
        {"$text": {"$search": query}}))
    user_plants = list(mongo.db.plants.find(
        {"$text": {"$search": query}}))
    user_garden_events = list(mongo.db.garden_events.find(
        {"$text": {"$search": query}}))
    return render_template("journal.html",
                           user_garden_events=user_garden_events,
                           user_categories=user_categories,
                           user_plants=user_plants)


@app.route("/filter", methods=["GET", "POST"])
def filter():

    filter_plant = request.form.getlist("filter_plant")
    filter_month = request.form.getlist("filter_month")
    filter_category = request.form.getlist("filter_category")

    print(filter_plant)
    print(filter_month)

    plants = []
    months = []
    events = []

    if filter_plant != []:
        plants = list(mongo.db.plants.find({"$or": [{"plant_name": x} for x in filter_plant]}))
    else:
        plants = list(mongo.db.plants.find().sort("plant_type"))
        # pass

    if filter_category != []:
        events = list(mongo.db.garden_events.find({"$or": [{"event_category": x} for x in filter_category]}))
    else:
        events = list(mongo.db.garden_events.find().sort("event_date"))

    if filter_month != []:
        months = list(mongo.db.garden_events.find({"$or": [{"event_month": x} for x in filter_month]}))
    else:
        months = list(mongo.db.garden_events.find().sort("event_month"))

    print("\n PLANTS: \n", plants, "\n MONTHS: \n", months, "\n EVENTS: \n", events)

    user_event_months = []
    user_garden_events = []
    user_plants = []
    # plants = list(plants)

    for plant in plants:
        if (plant["created_by"] == session["user"] or
                session["user"] == "admin"):
            user_plants.append(plant)

    # event_months = list(event_months)

    for month in months:
        user_event_months.append(month)

    # garden_events = list(garden_events)

    for garden_event in events:
        if (garden_event["created_by"] == session["user"] or
                session["user"] == "admin"):
            user_garden_events.append(garden_event)

#  this i s printing the selected and filter results to the page to display, but not working in the jija tempalte for some reason.
    print("\n USER_PLANTS: \n", plants, "\n USER_EVENT_MONTHS: \n", months, "\n USER_GARDEN_EVENTS: \n", events)

    # for item in user_event_months:
    #     user_garden_events.append(item)
    #     for item in user_plants:
    #         user_garden_events.append(item)

    # print("\n CONCATENATED LIST:", user_garden_events)

    return render_template("journal.html",
                        #    user_garden_events=[],
                        #    user_event_months=[],
                        #    user_plants=[])
                           user_garden_events=user_garden_events,
                           user_event_months=user_event_months,
                           user_plants=user_plants)
                        

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"user_name": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", "error")
            return redirect(url_for("register"))

        register = {
            "user_name": request.form.get("username").lower(),
            "user_email": request.form.get("email"),
            "user_password": generate_password_hash(
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
            {"user_name": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["user_password"], request.form.get(
                        "password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
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
    # get session users username from db
    username = mongo.db.users.find_one(
        {"user_name": session["user"]})["user_name"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        date_string = request.form.get("event_date")
        date_object = pd.to_datetime(date_string)
        event_plant_id = request.form.get("event_plant_id")
        event_month = date_object.strftime("%B")

        event = {
            "event_category": request.form.get("event_category"),
            "event_plant_id": ObjectId(event_plant_id),
            "event_name": request.form.get("event_name"),
            "event_repeats": request.form.get("event_repeats"),
            "event_date": date_object,
            "event_month": event_month,
            "event_notes": request.form.get("event_notes"),
            "created_by": session["user"]
        }
        mongo.db.garden_events.insert_one(event)
        flash("Event Successfully Added", "success")
        return redirect(url_for("get_garden_events"))

    categories = mongo.db.categories.find().sort("event_category", 1)
    plants = list(mongo.db.plants.find().sort("plant_name"))
    return render_template(
        "add_event.html", categories=categories, plants=plants)


@app.route("/edit_event/<event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    if request.method == "POST":
        date_string = request.form.get("event_date")
        date_object = pd.to_datetime(date_string)
        event_month = date_object.strftime("%B")
        # change plant name variable to plant_id in events collection
        # Also change in edit_events.html and add_events.html
        event_plant_id = request.form.get("event_plant_id")

        submit = {
            "event_category": request.form.get("event_category"),
            # Creates an object from the string to send to collection
            "event_plant_id": ObjectId(event_plant_id),
            "event_name": request.form.get("event_name"),
            "event_repeats": request.form.get("event_repeats"),
            "event_date": date_object,
            "event_month": event_month,
            "event_notes": request.form.get("event_notes"),
            "created_by": session["user"]
        }
        mongo.db.garden_events.update({"_id": ObjectId(event_id)}, submit)
        flash("Event Successfully Updated", "success")

    garden_event = mongo.db.garden_events.find_one(
        {"_id": ObjectId(event_id)})

    garden_events = list(mongo.db.garden_events.find().sort("event_date"))
    categories = mongo.db.categories.find().sort("event_category", 1)
    plants = list(mongo.db.plants.find().sort("plant_type"))
    return render_template(
        "edit_event.html", plants=plants, garden_events=garden_events,
        garden_event=garden_event, categories=categories)


@app.route("/delete_event/<event_id>")
def delete_event(event_id):
    mongo.db.garden_events.remove({"_id": ObjectId(event_id)})
    flash("Event Successfuly Deleted", "success")
    return redirect(url_for("get_garden_events"))


@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    if request.method == "POST":
        sowing_date_string = request.form.get("plant_sowing")
        planting_date_string = request.form.get("plant_planting")
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
        harvest_from_object = pd.to_datetime(harvest_from_string)
        harvest_to_object = pd.to_datetime(harvest_to_string)

        plant = {
            "plant_type": request.form.get("plant_type"),
            "plant_name": request.form.get("plant_name"),
            "plant_sowing": sowing_date_object,
            "plant_planting": planting_date_object,
            "harvest_from": harvest_from_object,
            "harvest_to": harvest_to_object,
            "fertilise_frequency": request.form.get(
                "fertilise_frequency"),
            "fertiliser_type": request.form.get("fertiliser_type"),
            "plant_note": request.form.get("plant_note"),
            "created_by": session["user"]
        }
        mongo.db.plants.insert_one(plant)
        flash("Plant Successfully Added", "success")
        return redirect(url_for("get_plants"))

    return render_template("add_plant.html")


@app.route("/edit_plant/<plant_id>", methods=["GET", "POST"])
def edit_plant(plant_id):
    if request.method == "POST":
        sowing_date_string = request.form.get("plant_sowing")
        planting_date_string = request.form.get("plant_planting")
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
        harvest_from_object = pd.to_datetime(harvest_from_string)
        harvest_to_object = pd.to_datetime(harvest_to_string)

        submit = {
            "plant_type": request.form.get("plant_type"),
            "plant_name": request.form.get("plant_name"),
            "plant_sowing": sowing_date_object,
            "plant_planting": planting_date_object,
            "harvest_from": harvest_from_object,
            "harvest_to": harvest_to_object,
            "fertilise_frequency": request.form.get(
                "fertilise_frequency"),
            "fertiliser_type": request.form.get("fertiliser_type"),
            "plant_note": request.form.get("plant_note"),
            "created_by": session["user"]
        }
        mongo.db.plants.update({"_id": ObjectId(plant_id)}, submit)
        flash("Plant Successfully Updated", "success")

    plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})

    plants = list(mongo.db.plants.find().sort("plant_type"))
    return render_template("edit_plant.html", plants=plants, plant=plant)


@app.route("/delete_plant/<plant_id>")
def delete_plant(plant_id):
    mongo.db.plants.remove({"_id": ObjectId(plant_id)})
    flash("Plant Successfuly Deleted", "success")
    return redirect(url_for("get_plants"))


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        new_category = {
            "event_category": request.form.get("event_category"),
            "created_by": session["user"]
        }
        mongo.db.categories.insert_one(new_category)
        flash("New Category Successfully Added", "success")
        return redirect(url_for("add_category"))

    categories = list(mongo.db.categories.find().sort("event_category"))
    return render_template(
        "add_category.html", categories=categories)


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "event_category": request.form.get("event_category"),
            "created_by": session["user"]
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("New Category Successfully Added", "success")

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})

    categories = list(mongo.db.categories.find().sort("event_category"))
    return render_template(
        "edit_category.html", categories=categories, category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfuly Deleted", "success")
    return redirect(url_for("add_category"))


@app.errorhandler(404)
def page_not_found(error):
    flash("Error, the page was not found.", "danger")
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(error):
    flash("Server Error", "danger")
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
    