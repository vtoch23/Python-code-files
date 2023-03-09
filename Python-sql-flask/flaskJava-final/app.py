# Searches for shows
from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

db = SQL('sqlite:///database.db')


@app.route("/")

def index():
    return render_template("index.html")

@app.route("/search")

def search():
    shows = db.execute("select * from shows where title like ?", "%" + request.args.get("q") + "%") #because we use like then we need the percent sign
    return render_template("search.html", shows=shows)
