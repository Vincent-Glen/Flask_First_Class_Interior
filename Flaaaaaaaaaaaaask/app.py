import re
from datetime import datetime
from flask import render_template


from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/shop/")
def shop():
    return render_template("shop.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")