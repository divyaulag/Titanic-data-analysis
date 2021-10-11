from flask import Flask,render_template,url_for,request,jsonify
import pickle
import numpy as np
model = pickle.load(open('titanic.pkl','rb'))
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import random
pymysql.install_as_MySQLdb()

df = pd.read_sql_table('prediction','mysql://root:''@localhost:3307/test')
print(df)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3307/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Prediction(db.Model):
    __tablename__ = 'prediction'
    PassengerId = db.Column(db.Integer, primary_key=True,autoincrement=True)
    Gender = db.Column(db.Integer)
    Age = db.Column(db.Integer)
    Class = db.Column(db.Integer)
    Parch = db.Column(db.Integer)
    Sib = db.Column(db.Integer)
    survival = db.Column(db.Integer)
    def __init__(self,gender,age,clas,parch,sib,sur):
      self.Gender = gender
      self.Age= age
      self.Class = clas
      self.Parch = parch
      self.Sib = sib
      self.survival = sur
@app.route('/')
def man():
   return render_template('index.html')


@app.route('/process',methods=['POST'])
def process():
   data1 = request.form['Class']
   data2 = request.form['age']
   data3 = request.form['sib']
   data4 = request.form['pch']
   data5 = request.form['Gender']
   arr = np.array([[data1, data2, data3, data4, data5]])
   pred = model.predict(arr)
   new = Prediction(data5, data2, data1, data4, data3, pred[0])
   db.session.add(new)
   db.session.commit()
   if pred[0]==0:
      return jsonify({'state':'Died'})
   else:
      return jsonify({'state':'Survived'})



if __name__=="__main__":
    app.run(debug=True)

