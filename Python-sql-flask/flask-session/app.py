from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__) #makes this a Flask program

#Configure session
app.config("SESSION_PERMANENT") = False
app.config("SESSION_TYPE") = "filesystem"
Session(app)

app = Flask(__name__) #makes this a Flask program


# defines a route
@app.route("/")
# renders the index.html template if logged in
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html")

# defines a login route
@app.route("/login", methods=["GET", "POST"])
# renders the login.html template if logged in

def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

@aoo.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")