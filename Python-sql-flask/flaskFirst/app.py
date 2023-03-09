from flask import Flask, redirect, render_template, request


#Configure app
app = Flask(__name__)

db = SQL("sqlite:///froshims.db")


# defines a route
@app.route("/")

# renders the index.html template
def index():
    return render_template("index.html")

#creates a route, if the route is not found it will give 404 error
@app.route("/greet")

# responds to the greet function call in the html, renders the gree.html template
def greet():
    name=request.args.get("name", "world") # get function
    return render_template("greet.html", name=name)



#render this file every time, gives the name from the user changing it in the browser url manually
#def index():
   # name = request.args.get("name") #gets the name from browser url typed in manually
   # return render_template("index.html", name_of_person=name) #variable needs to match the plugged-in value in html file

