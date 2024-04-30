from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello main page <h1>hello</h1>"

@app.route("/<name>")
def user(name):return f"heloooo {name}"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))

@app.route("/admin")
def admin():
    return redirect(url_for("user",name = "hariiis"))

if __name__ =="__main__":
    app.run()

