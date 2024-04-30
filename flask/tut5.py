from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import sqlalchemy

app = Flask(__name__)
app.secret_key="hello"
app.permanent_session_lifetime = timedelta(minutes=45)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method =="POST":
        user = request.form["username"]
        passw = request.form["password"]
        session["username"]= user
        flash("logged in successfully")
        return redirect(url_for("user"))
    else:
        if "username" in session:
            flash("already logged IN!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    if "username" in session:
        user = session["username"]
        if request.method == "POST":
            patient = request.form.get("patient")
            session["patient"] = patient
            flash("Data entered successfully")
            return redirect(url_for("count"))
        else:
            print(session)
            return render_template("user.html", user=user)
    else:
        print(session)
        flash("You are not logged in!")
        return redirect(url_for("login"))

    
@app.route("/count",methods=["GET","POST"])
def count():
    print("helloq")
    print(session)
    if "patient" in session:
        patients = session["patient"]
        user = session
        print(patients,user)
        print("helloqwe")
        return render_template("count.html",patient = patients)
    else:
        print("helqwelo")
        flash("You are not  logged IN!")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    userr = session["username"]
    flash("You have been logged out!","info")
    session.pop("username",None)
    session.pop("patient",None)
    return redirect(url_for("login"))

if __name__ =="__main__":
    app.run(debug=True)
