from flask import Flask,render_template,request,redirect
from firebase import Firebase
app = Flask(__name__)
def handle_catch(caller, on_exception):
    try:
         return caller()
    except:
         return on_exception

config = {
   "apiKey": "AIzaSyBBXsvkN8KdwcCJlJx7n-plwZ8NLDVyu1I",
    "authDomain": "to-do-om.firebaseapp.com",
    "databaseURL": "https://to-do-om-default-rtdb.firebaseio.com",
    "projectId": "to-do-om",
    "storageBucket": "to-do-om.appspot.com",
    "messagingSenderId": "805281315065",
    "appId": "1:805281315065:web:cd75e2bee2165951f84a28",
    "measurementId": "G-GJ98CQYFCG"
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




