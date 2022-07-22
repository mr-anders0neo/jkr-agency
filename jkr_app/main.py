from fnmatch import fnmatchcase
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_BINDS'] = {
    'sell': 'sqlite:///sell.db',
    'user': 'sqlite:///user.db'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

class Contact(db.Model):
    contactId = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    mobile = db.Column(db.BigInteger, nullable=False)
    subject = db.Column(db.String(500), nullable=False)

class Sell(db.Model):
    __bind_key__ = 'sell'
    sellId = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    mobile = db.Column(db.BigInteger, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    area = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class User(db.Model):
    __bind_key__ = 'user'    
    userId = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

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
            msg='Sorry, our system is currently offline'
    
    return render_template("contact-us.html", msg=msg, fname=fname)

@app.route("/services.html", methods=['POST', 'GET'])
def services():
    msg=''
    fname=''
    if request.method == 'POST':
        fname = request.form['jkr-fname']
        try:
            db.session.add(Sell(
                first_name=fname,
                last_name=request.form['jkr-lname'],
                email=request.form['jkr-mail'],
                mobile=request.form['jkr-phone'],
                address=request.form['jkr-address'],
                area=request.form['jkr-area'],
                price=request.form['jkr-price'],
                year=request.form['jkr-year']
            ))
            db.session.commit()
            msg='We will give you a call back with the estimated price'
        except Exception as e:
            msg='Sorry, our system is currently offline'
    
    return render_template("services.html", msg=msg, fname=fname)

@app.route("/login", methods=['POST', 'GET'])
def login():
    msg=''
    fname=''
    if request.method == 'POST':
        try:
            get_user = User.query.filter_by(email=request.form['jkr-mail']).first()
            if get_user:
                fname = get_user.first_name
                return render_template('index.html', fname=fname)

        except:
            msg='User not found'
        
    return render_template('index.html', msg=msg, fname=fname)


@app.route("/register", methods=['POST', 'GET'])
def register():
    fname=''
    if request.method == 'POST':
        fname = request.form['jkr-fname']
        try:
            db.session.add(User(
                first_name=fname,
                last_name=request.form['jkr-lname'],
                email=request.form['jkr-mail'],
                password=request.form['jkr-password']
            ))
            db.session.commit()
        except:
            return 'There was an issue with registration'

    return render_template("index.html", fname=fname)

if __name__ == "__main__":
    app.run(debug=True)