
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
        plant_name = request.form.get("plant_name")

        event = {
            "event_category": request.form.get("event_category"),
            "plant_name": plant_name,
            "event_name": request.form.get("event_name"),
            "event_repeats": request.form.get("event_repeats"),
            "event_date": date_object,
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
        plant_name = request.form.get("plant_name")

        submit = {
            "event_category": request.form.get("event_category"),
            "plant_name": plant_name,
            "event_name": request.form.get("event_name"),
            "event_repeats": request.form.get("event_repeats"),
            "event_date": date_object,
            "event_notes": request.form.get("event_notes"),
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


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get session users username from db
    username = mongo.db.users.find_one(
        {"user_name": session["user"]})["user_name"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/get_garden_events")
def get_garden_events():
    garden_events = list(mongo.db.garden_events.find().sort("event_date"))
    plants = list(mongo.db.plants.find())

    user_garden_events = []
    for garden_event in garden_events:
        if garden_event["created_by"] == session["user"] or session["user"] == "admin":
            user_garden_events.append(garden_event)

    user_plants = []
    for plant in plants:
        if plant["created_by"] == session["user"] or session["user"] == "admin":
            user_plants.append(plant)

    # month = mongo.db.garden_events.find({'$expr': {'$eq': [{'$month': "$event_date"} ,9]}})
    return render_template("journal.html", user_plants=user_plants,
                           user_garden_events=user_garden_events)


@app.route("/get_plants")
def get_plants():
    plants = list(mongo.db.plants.find().sort("plant_type"))

    user_plants = []
    for plant in plants:
        if plant["created_by"] == session["user"] or session["user"] == "admin":
            user_plants.append(plant)

    return render_template("plants.html", user_plants=user_plants)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
