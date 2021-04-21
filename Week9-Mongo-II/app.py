from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Users"
mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    form = request.form
    user = mongo.db.user.find_one({"email":form["email"],"password":form["password"]})
    if user:
        name = user["name"]
        dob = user["DOB"]
        email = form["email"]
        return render_template("profile.html", message = "Success! Here is your profile",name = name, dob=dob, email=email)
    else:
        return render_template("login.html", error = "Wrong credentials!")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    form = request.form
    print(mongo.db.user.find_one({"email" : form["email"]}))
    if mongo.db.user.find_one({"email" : form["email"]}):
        error = "User already exists!"
        return render_template("signup.html", error=error)
    mongo.db.user.insert({"email":form["email"], "name":form["name"], "DOB":form["DOB"], "password":form["password"]})
    return render_template("login.html", message="Success! Login to confirm")

if __name__ == "__main__":
    app.run(debug=True, port=4000)