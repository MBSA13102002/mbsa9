from flask import Flask,render_template,request,redirect
from firebase import Firebase
app = Flask(__name__)
def handle_catch(caller, on_exception):
    try:
         return caller()
    except:
         return on_exception

config = {
    "apiKey": "AIzaSyCiLNaJMak6yrWdYfg-LqAz1EbBPmDmPXs",
   "authDomain": "todowebflaskapp.firebaseapp.com",
    "databaseURL": "https://todowebflaskapp-default-rtdb.firebaseio.com",
    "projectId": "todowebflaskapp",
    "storageBucket": "todowebflaskapp.appspot.com",
    "messagingSenderId": "817348374426",
    "appId": "817348374426",
    "measurementId": "G-K2EZGZZCZT"
}
firebase = Firebase(config)
db = firebase.database()

@app.route('/',methods =['GET','POST'])
def started():
    if request.method=='POST':
        htmldata = request.form.get('htmldata')
        db.child("MAIN").set({"DATA":htmldata})
        return render_template('index.html',htmldata_from_firebase=htmldata,handle_catch=handle_catch)
    htmldata_from_firebase = db.child("MAIN").child("DATA").get().val()   
    return render_template('index.html',htmldata_from_firebase=htmldata_from_firebase,handle_catch=handle_catch)




