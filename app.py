
import os
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
        date_object = datetime.strptime(date_string, "%B %d, %Y")
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

        # mongo.db.plants.update_one(
        #     {"plant_name": plant_name},
        #     {'$set': {plant}}, upsert=True)
     
        return redirect(url_for("get_garden_events"))

    categories = mongo.db.categories.find().sort("event_category", 1)
    plants = list(mongo.db.plants.find().sort("plant_name"))
    return render_template(
        "add_event.html", categories=categories, plants=plants)


@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    if request.method == "POST":
        sowing_date_string = request.form.get("plant_sowing")
        planting_date_string = request.form.get("plant_planting")
        harvest_from_string = request.form.get("harvest_from")
        harvest_to_string = request.form.get("harvest_to")
        sowing_date_object = datetime.strptime(sowing_date_string, "%B %d, %Y")
        planting_date_object = datetime.strptime(planting_date_string, "%B %d, %Y")
        harvest_from_object = datetime.strptime(harvest_from_string, "%B %d, %Y")
        harvest_to_object = datetime.strptime(harvest_to_string, "%B %d, %Y")

        plant = {
            "plant_type": request.form.get("plant_type").lower(),
            "plant_name": request.form.get("plant_name").lower(),
            "plant_sowing": sowing_date_object,
            "plant_planting": planting_date_object,
            "harvest_from": harvest_from_object,
            "harvest_to": harvest_to_object,
            "fertilise_frequency": request.form.get("fertilise_frequency").lower(),
            "fertiliser_type": request.form.get("fertiliser_type").lower(),
            "plant_note": request.form.get("plant_note").lower(),
            "created_by": session["user"]
        }
        mongo.db.plants.insert_one(plant)
        flash("Plant Successfully Added", "success")

    return render_template("add_plant.html")


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
    return render_template("journal.html", garden_events=garden_events,
                           plants=plants)
                           
                           
@app.route("/get_plants")
def get_plants():
    plants = list(mongo.db.plants.find().sort("plant_type"))
    return render_template("plants.html", plants=plants)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
