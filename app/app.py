from flask import Flask, redirect, render_template, request
import mods
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/investment")
def investment():
    return render_template("investment.html")

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/records")
def records():
    return render_template("CourseRecords.html")

@app.route("/files")
def files():
    return render_template("files.html")

@app.route("/links")
def links():
    return render_template("links.html")

@app.route("/link-short", methods=["GET", "POST"])
def link_short():
    link = request.args.get("link")
    link = mods.link_short(link)
    return render_template("link-short.html", link=link)

@app.route("/words")
def words():
    return render_template("words.html")

@app.route("/orders")
def orders():
    return render_template("orders.html")

@app.route("/employees")
def employees():
    return render_template("employees.html")

@app.route("/password")
def password():
    return render_template("password.html")

@app.route("/lottery")
def lottery():
    return render_template("lottery.html")

@app.route("/products")
def products():
    return render_template("products.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)    