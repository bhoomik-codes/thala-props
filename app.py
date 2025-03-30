from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_user:your_password@localhost/flask_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model (table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", methods=["POST"])
def submit():
    # Get data from the form
    username = request.form.get("username")
    email = request.form.get("email")
    age = request.form.get("age")

    # Create a new User object and add it to the database
    new_user = User(username=username, email=email, age=age)
    db.session.add(new_user)
    db.session.commit()

    return f"User added: Name: {username}, Email: {email}, Age: {age}. <br><a href='/'>Go back</a>"

@app.route("/view_users")
def view_users():
    users = User.query.all()
    user_list = [f"ID: {user.id}, Name: {user.username}, Email: {user.email}, Age: {user.age}" for user in users]
    return "<br>".join(user_list)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/buynow")
def buynow():
    return render_template("buynow.html")

if __name__ == "__main__":
    app.run()

