from flask import Flask, render_template, request, session
from flask_session import Session

app=Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")

feedbacks=[]

@app.route("/feedback",methods=["GET","POST"])
def feedback_function():
    if request.method == "POST":
        my_feedback=request.form.get("feedback")
        feedbacks.append(my_feedback)
    
    return render_template("feedback.html",feedbacks=feedbacks)
 

