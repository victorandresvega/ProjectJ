from django.shortcuts import redirect
from flask import Flask, render_template,request,redirect
import pymongo
import os



app = Flask(__name__)
# MongoDB
# client = pymongo.MongoClient("mongodb+srv://admin:" + os.environ["MONGO_APPOINTMED_PWD"] +
#                              "@cluster0.vsmni.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client = pymongo.MongoClient( "mongodb+srv://SDS:" + os.environ.get("MONGO_PW")+ "@cluster0.zc52h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = client.test
time_slots = ["8:00am", "8:30am", "9:00am", "9:30am", "10:00am", "10:30am", "11:00am", "11:30am", "12:00pm", "12:30pm",
              "1:00pm", "1:30pm", "2:00pm", "2:30pm", "3:00pm", "3:30pm", "4:00pm", "4:30pm"]


@app.route("/")
@app.route("/home")
def home():
    pass


@app.route("/Schedule", methods=["GET", "POST"])
def schedule():
    day=''
    if request.form == 'POST':
        day=request.form['day']
        return redirect("/"+day)
    else:
        return render_template("appointment.html",day=day,time_slots=time_slots)
@app.route("/Schedule/<day>", methods=["GET", "POST"])
def scheduleTime(day):
    return render_template("appointment.html",day=day,time_slots=time_slots)



@app.route("/seed_db")
def seed_db():
    pass
