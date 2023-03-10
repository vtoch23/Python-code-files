from flask import Flask, redirect, render_template, request
from database import dbcon

db = dbcon()
app = Flask(__name__) #makes this a Flask program
FLASK_APP="database.py"
# defines a route
@app.route("/")

# renders the index.html template
def index():
    return render_template("index.html")


#creates a route, if the route is not found it will give 404 error
@app.route("/greet", methods=["POST", "GET"])

# responds to the greet function call in the html, renders the gree.html template
def greet():
    
    name=request.form.get("name") # get function
    age=request.form.get("age")   
    db.execute('INSERT INTO names (name, age) VALUES(?,?)', (name, age))
    return render_template("greet.html", name=name, age=age)

@app.route("/people", methods=["POST", "GET"])
def people():
    people = db.execute("SELECT * FROM names")
    return render_template("names.html", names=people)

@app.route("/deregister", methods=["POST"])
def deregister():
    #Forget registrant
    if id:
        db.execute("DELETE FROM names WHERE name = ?", name)
    return redirect("/names")


#render this file every time, gives the name from the user changing it in the browser url manually
#def index():
   # name = request.args.get("name") #gets the name from browser url typed in manually
   # return render_template("index.html", name_of_person=name) #variable needs to match the plugged-in value in html file

