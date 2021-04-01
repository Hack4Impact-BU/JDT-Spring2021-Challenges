from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def helloWorld():
    return render_template('index.html')

@app.route('/formSubmit', methods=["POST"])
def formSubmit():
    firstName = request.form.get("fname")
    lastName = request.form.get("lname")
    print(firstName)
    print(lastName)
    return render_template('result.html', fname = firstName, lname = lastName)