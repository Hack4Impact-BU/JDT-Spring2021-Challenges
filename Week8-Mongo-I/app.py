from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDB"
mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def home():
    query = {}
    todos = mongo.db.todos.find(query)
    return render_template("index.html", todos=todos)

@app.route("/formSubmit", methods=["POST"])
def formSubmit():
    todo = request.form["todo"]
    document = {"todo":todo}
    mongo.db.todos.insert(document)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=4000)