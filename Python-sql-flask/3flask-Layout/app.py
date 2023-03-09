from flask import Flask, render_template, request, redirect
import sqlite3

db = sqlite3.connect('names.db', check_same_thread=False)
app = Flask(__name__)
cur = db.cursor()

@app.route("/") #default page on the web app
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    name = request.args.get("name")
    age = request.args.get("age")
    cur.execute('insert into names (name, age) values(?,?)', (name, age))
    return render_template("greet.html", name=name, age=age)
@app.route("/view")
def view():
    names = cur.execute("select * from names")
    return render_template("names.html", names=names)

@app.route("/delete", methods = ["POST"]) #currently not working, everything else works
def delete():
    if name:
        cur.execute("delete from names where name like ?", name)
    return redirect("/view")