
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
        user = mongo.db.users.find_one({"user_name": session["user"]})
        user.pop("user_password")
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
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            message = form.message.data
            
            form_message = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "message": message,
                "date_time": datetime.now()
            }
            mongo.db.messages.insert_one(form_message)
            flash("Message has been sent.", "success")
            # return first_name + "<br /> " + last_name + "<br /> " + email + "<br /> " + message
            return redirect(url_for("contact"))

    return render_template('contact.html', form=form)


@app.route("/messages")
def messages():
    if "user" in session and session["user"] == "admin":
        messages = list(mongo.db.messages.find().sort("date_time"))
        return render_template('messages.html', messages=messages)
    else:
        flash("Please log in to view page.", "error")
        return redirect(url_for("login"))


@app.route("/delete_message/<message_id>")
def delete_message(message_id):
    messages = list(mongo.db.messages.find().sort("date_time"))
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
                mongo.db.garden_events.find().sort("event_month"))
            plants = list(mongo.db.plants.find())
            categories = list(
                mongo.db.categories.find().sort("event_category", 1))
            events_months = list(
                mongo.db.garden_events.find().sort("event_months"))
        else:
            garden_events = list(
                mongo.db.garden_events.find(
                    {"created_by": session["user"]}).sort("event_date"))
            plants = list(mongo.db.plants.find(
                {"created_by": session["user"]}))
            categories = list(
                mongo.db.categories.find(
                    {"created_by": session["user"]}).sort("event_category"))
            events_months = list(
                mongo.db.garden_events.find(
                    {"created_by": session["user"]}).sort("event_month"))

        if not garden_events:
            flash(
                "Create events and event categories to populate this page.",
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
            plants = list(mongo.db.plants.find().sort("plant_type"))
        else:
            plants = list(mongo.db.plants.find(
                {"created_by": session["user"]}).sort("plant_type"))
 
        if not plants:
            flash("Create plants to populate this page.", "info")

        return render_template("plants.html", plants=plants)
    else:
        flash("Please log in to view page.", "error")
        return redirect(url_for("login"))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    categories = list(mongo.db.categories.find(
        {"$text": {"$search": query}}))
    plants = list(mongo.db.plants.find(
        {"$text": {"$search": query}}))
    garden_events = list(mongo.db.garden_events.find(
        {"$text": {"$search": query}}).sort("event_date"))

    return render_template("journal.html",
                           garden_events=garden_events,
                           categories=categories,
                           plants=plants)
                 

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
            "user_name": request.form.get("username"),
            "user_firstname": request.form.get("firstname"),
            "user_lastname": request.form.get("lastname"),
            "user_email": request.form.get("email"),
            "user_joined": datetime.now(),
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
    if "user" in session:
        users = list(mongo.db.users.find().sort("user_name"))
        user_profile = []
        for user in users:
            # check if user logged in, and matches user logged in. 
            if "user" in session and (user["user_name"] == session["user"]):
                user_profile.append(user)
        # get session users username from db
        username = mongo.db.users.find_one(
            {"user_name": session["user"]})["user_name"]
        if session["user"]:
            return render_template("profile.html", username=username,
                                   user_profile=user_profile)
    else:
        flash("Please log in for access.", "error")
        return redirect(url_for("login", ))


@app.route("/edit_profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):

    existing_user = mongo.db.users.find_one({"_id": ObjectId(user_id)})

    if request.method == "POST":

        if existing_user:
            if check_password_hash(
                        existing_user["user_password"], request.form.get(
                            "old_password")):
                # flash("Password validation passed", "success")

                user_email = request.form.get("email")
                if user_email is not None:
                    update = {
                        "user_email": request.form.get("email"),
                        "user_firstname": request.form.get("firstname"),
                        "user_lastname": request.form.get("lastname"),
                    }
                    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update})
                    flash("The information has been updated successfully.", "success")
                    return redirect(url_for("profile", username=session["user"]))

            else:
                flash("Please confirm the correct password.", "error")
                return redirect(url_for("edit_profile", user_id=user_id))
     
    return render_template(
        "edit_profile.html", existing_user=existing_user)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    if "user" in session:
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

        plants = []
        categories = []
        # distinguish if admin or normal user
        if session["user"] == "admin":
            plants = list(mongo.db.plants.find().sort("plant_type"))
            categories = mongo.db.categories.find().sort("event_category", 1)
        else:
            plants = list(mongo.db.plants.find(
                {"created_by": session["user"]}).sort("plant_type"))
            categories = list(mongo.db.categories.find(
                {"created_by": session["user"]}).sort("event_category"))

        return render_template(
            "add_event.html", categories=categories, plants=plants)
    else:
        flash("Please log in to view page", "error")
        return redirect(url_for("login"))


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
        return redirect(url_for("get_garden_events"))

    garden_event = mongo.db.garden_events.find_one(
        {"_id": ObjectId(event_id)})

    garden_events = list(mongo.db.garden_events.find().sort("event_date"))

    plants = []
    categories = []
    # distinguish if admin or normal user to populate list accordingly
    if session["user"] == "admin":
        plants = list(mongo.db.plants.find().sort("plant_type"))
        categories = mongo.db.categories.find().sort("event_category", 1)
    else:
        plants = list(mongo.db.plants.find(
            {"created_by": session["user"]}).sort("plant_type"))
        categories = list(mongo.db.categories.find(
            {"created_by": session["user"]}).sort("event_category"))

    if not plants:
        flash("Create plants to populate this page.", "info")

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
    if "user" in session:
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
    else:
        flash("Please log in to view page", "error")
        return redirect(url_for("login"))


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
        return redirect(url_for("get_plants"))

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
    if "user" in session:
        if request.method == "POST":
            new_category = {
                "event_category": request.form.get("event_category"),
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
                              "event_category"))
        else:
            categories = list(mongo.db.categories.find(
                              {"created_by": session["user"]}).sort(
                                  "event_category"))

        if not categories:
            flash("Create event categories to populate this list.", "info")

        return render_template(
            "add_category.html", categories=categories)
    else:
        flash("Please log in to view page", "error")
        return redirect(url_for("login"))


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "event_category": request.form.get("event_category"),
            "created_by": session["user"]
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated", "success")
        return redirect(url_for("add_category"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})

    # Get list of all categories filtered by session user
    categories = list(mongo.db.categories.find({"created_by": session["user"]}).sort("event_category"))

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
