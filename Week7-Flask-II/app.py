from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def helloWorld():
    return render_template('index.html')

@app.route('/formSubmit', methods=["POST"])
def formSubmit():
    firstName = request.form.get("fname")
    uniName = request.form.get("uniName")

    url = "http://universities.hipolabs.com/search?"
    payload = {'name': uniName}

    response = requests.get(url, params = payload)
    print(response.url)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(response.headers['content-type'])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(response.content)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(response.text)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    return render_template('result.html', fname = firstName, uniName = uniName, uniContent = response.text)