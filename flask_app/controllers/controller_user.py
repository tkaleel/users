from flask_app import app, render_template, request, redirect
from flask_app.models.model_user import User

@app.route("/")
def index():
    return redirect('/users')

@app.route("/users")
def users():
    return render_template("users.html", users= User.get_all())

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/show/<int:id>")
def show(id):
    data= {"id":id}
    return render_template("show.html", user= User.get_one(data))

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

@app.route("/edit/<int:id>")
def edit(id):
    data = {"id":id}
    return render_template("edit.html", user= User.get_one(data))

@app.route('/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route("/destroy/<int:id>")
def destroy(id):
    data ={'id': id}
    User.destroy(data)
    return redirect('/users')
