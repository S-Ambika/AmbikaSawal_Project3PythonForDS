from email import message
from enum import unique
import os
from crypt import methods
from pickle import NONE
from zlib import Z_BEST_COMPRESSION
from flask import Flask,jsonify,render_template,request
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import redirect


app_view = Blueprint('main_app', __name__)


app = Flask(__name__)
pwd="FSDAmbika@9"
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:{pwd}@localhost:3306/loan_approval_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
   
    def __init__(self,id , username, password, comments):
        self.id = id
        self.username = username
        self.password = password
        self.comments = comments


# db.create_all()


@app.route("/")
def index():

        return render_template("home.html")

@app.route("/login")
def login():
    return render_template('login.html')
 
@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/register_user",methods=['POST'])
def registerUser():
    # output=request.form.to_dict()
    # username=output['username']
    username=request.form.get("username")
    # password=request.form.get("password")
    return render_template("predict.html",message="successfully registered")












if __name__ == "__main__":
    app.run(debug=True,port=8001)

