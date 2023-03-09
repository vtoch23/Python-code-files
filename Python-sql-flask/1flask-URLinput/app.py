from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") #default page on the web app
def index():
    name = request.args.get("name") #define a variable, ask flask to go into the arguments in the current request and get the value
    return render_template("index.html", name_of_person=name)#the name of the variable I want to give to the template, and the actual variable I want to get the value from

#this is if we add the query to the end of the URL after the route /
#https://vtoch23-obscure-space-trout-665q9g9qr5525pr-5000.preview.app.github.dev/?name=Vanya