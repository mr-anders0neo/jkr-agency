from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

class Contact(db.Model):
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), primary_key=True)
    mobile = db.Column(db.BigInteger, nullable=False)
    subject = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return '<Contact %r>' % self.email

@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/about-us.html")
def about():
    return render_template("about-us.html")

@app.route("/contact-us.html", methods=['POST', 'GET'])
def contact():
    msg=''
    fname=''
    if request.method == 'POST':
        fname = request.form['jkr-fname']
        try:
            db.session.add(Contact(
                first_name=fname,
                last_name=request.form['jkr-lname'],
                email=request.form['jkr-mail'],
                mobile=request.form['jkr-phone'],
                subject=request.form['jkr-issue']
            ))
            db.session.commit()
            msg='Thank you for reaching out to us!'
        except Exception as e:
            msg= 'Please provide unique email'
    
    return render_template("contact-us.html", msg=msg, fname=fname)

@app.route("/services.html")
def services():
    return render_template("services.html")


if __name__ == "__main__":
    app.run(debug=True)