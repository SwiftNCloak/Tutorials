from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello testing <h1>HELLO</h1>"

@app.route("/<name>") # grab the value
def user(name): # pass to this perimeter
    return f"HELLO {name}" # displays value

@app.route("/admin") # redirect
def admin():
    return redirect(url_for("home")) #name of function inside string

if __name__ == "__main__":
    app.run()