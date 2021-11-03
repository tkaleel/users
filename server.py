from flask import Flask, render_template, request, redirect
from models.model_user import User
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", users = User.get_all())

@app.route("/users")
def users():
    return render_template("users.html", users= User.get_all())

@app.route("/new")
def new():
    return render_template("new.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)
