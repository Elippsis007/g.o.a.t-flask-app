import os
import json
from flask import Flask, render_template

# create an instance of this class
# The first argument of the Flask class, is the name of the application's module - our package.
app = Flask(__name__)

# use the route decorator to tell Flask what URL should trigger the function that follows
# "pie notation"
# When we try to browse to the root directory, as indicated by the "/", then Flask triggers the index function underneath and returns the "Hello, World" text.
@app.route("/")
# a function called "index", which just returns the string, "Hello, World"
def index():
    return render_template("index.html")

@app.route("/goat")
def goat():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("goat.html", page_title="Greatest Of All Time", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")    

# The word 'main' wrapped in double-underscores (__main__) is the name of the default module in Python.
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0, 0, 0, 0"),
        port=int(os.environ.get("PORT", "5000")),
        # Never have debug=True in submission of project
        debug=True)