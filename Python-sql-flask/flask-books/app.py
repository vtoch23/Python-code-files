from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

#Configure app
app = Flask(__name__) #makes this a Flask program

#Connect to database
db = SQL('sqlite:///store.db')

#Configure session
app.config("SESSION_PERMANENT") = False
app.config("SESSION_TYPE") = "filesystem"
Session(app)

app = Flask(__name__) #makes this a Flask program


# defines a route
@app.route("/")
# renders the index.html template if logged in
def index():
    books = db.execute("SELECT * FROM books")
    return render_template("books.html", books=books)

# defines a cart route
@app.route("/cart", methods=["GET", "POST"])
def cart():

    # Ensure cart exists
    if "cart" not in session:
        session["cart"] = []

    # POST
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["cart"].append(id)
        return redirect("/cart")

    # GET
    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
    return render_template("cart.html", books=books)