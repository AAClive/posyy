from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Table
import socket
import sqlalchemy as db
from sqlalchemy import VARCHAR
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import text
app=Flask(__name__)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
dbs=SQLAlchemy(app)
DB_NAME="database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
meta=db.MetaData()
engine = db.create_engine("postgresql://xbfvemmmdhhzkw:4757f5a5d1372eb80cdc4a99399045244e9fca63cb01fb5d4336115544feb9d3@ec2-54-147-33-38.compute-1.amazonaws.com:5432/dfl1c7euk3sg98")
meta.create_all(engine)
# create a table schema
users = db.Table( 'users', meta,
    Column('user_id', Integer, primary_key=True),
    Column('user_email', VARCHAR),
)
 
@app.route("/",methods=["GET","POST"])
def siginup():
    if request.method=="POST":
        global user
        user=request.form.get("variable")
        users=users(user_email=user)
        db.session.add(users)
        db.session.commit()
        sql=text("SELECT")
        result = engine.execute(sql).fetchall()
        return render_template("main.html",data=db,s=user)
    return render_template("main.html",data=db)
        

if __name__=="__main__":
   app.run()

