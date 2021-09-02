import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

# create an instance of this class
# The first argument of the Flask class, is the name of the application's module - our package.
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
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
    with open("data/team.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("goat.html", page_title="Greatest Of All Time", team=data)


@app.route("/goat/<player_name>")
def goat_player(player_name):
    player = {}
    with open("data/team.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == player_name:
                player = obj
    return render_template("player.html", player=player)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
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