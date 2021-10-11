from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb()

df = pd.read_sql_table('prediction','mysql://root:''@localhost:3307/test')
print(df)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3307/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Prediction(db.Model):
    __tablename__ = 'prediction'
    Index = db.Column(db.Integer, primary_key=True)
    Gender = db.Column(db.Integer)
    Age = db.Column(db.Integer)
    Class = db.Column(db.Integer)
    Parch = db.Column(db.Integer)
    Sib = db.Column(db.Integer)
    def __init__(self,gender,age,clas,parch,sib):
      self.Gender = gender
      self.Age= age
      self.Class = clas
      self.Parch = parch
      self.Sib = sib

new = Prediction(1,36,1,1,1)
db.session.add(new)
db.session.commit()

#db.create_all()





