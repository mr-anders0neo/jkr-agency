from flask import Flask
from flask import render_template
from . import app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about-us/")
def about():
    return render_template("about-us.html")

@app.route("/contact-us/")
def contact():
    return render_template("contact-us.html")

@app.route("/services/")
def services():
    return render_template("services.html")
