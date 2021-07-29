
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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


@app.route("/get_garden_events")
def get_garden_events():
    garden_events = list(mongo.db.garden_events.find())
    user_plants = list(mongo.db.user_plants.find())
    return render_template("journal.html", garden_events=garden_events,
                           user_plants=user_plants)


@app.route("/get_user_plants")
def get_user_plants():
    user_plants = mongo.db.user_plants.find().sort("plant_type")
    return render_template("plants.html", user_plants=user_plants)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)