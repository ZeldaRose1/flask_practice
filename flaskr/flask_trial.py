#!/bin/python

# testing flask
# Imports
from flask import Flask

app = Flask(__name__)

# Decorator tells flask to run code in the function block
# whenever the user visits the root of the webpage.
@app.route("/")
def hello_world():
    return "<title>Flask test</title>\n<p>Hello, World!</p>"

app.run(host="0.0.0.0", port=5000)

@app.route("/")
def index():
    return "Index Page"

@app.route("/hello/")
def hello():
    return "Hello World"

