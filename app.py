from flask import Flask
from flask import request
from flask import render_template
app=Flask(__name__)

@app.route("/")
def home():
  if request.method=="POST":
      pass
   return render_template("main.html")
