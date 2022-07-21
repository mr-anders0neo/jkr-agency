from flask import Flask
from flask import render_template
from . import app

@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/about-us.html")
def about():
    return render_template("about-us.html")

@app.route("/contact-us.html")
def contact():
    return render_template("contact-us.html")

@app.route("/services.html")
def services():
    return render_template("services.html")
