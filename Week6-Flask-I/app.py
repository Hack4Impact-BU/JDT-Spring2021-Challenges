from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Hey world, its great to be alive!!!'