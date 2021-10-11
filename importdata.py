import pandas
from sqlalchemy import Column,Integer,String,Float,Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:''@localhost:3307/test')
Base = declarative_base()

class Titanic(Base):
   __tablename__ = 'titanic'
   __table_args__ = {'schema':'test'}

   PassengerId = Column(Integer,primary_key=True)
   Survived=Column(Integer);
   Pclass=Column(Integer);
   Name=Column(String(50));
   Sex=Column(String(50));
   Age=Column(Integer);
   SibSp=Column(Integer);
   Parch=Column(Integer);
   Ticket=Column(String(50));
   Fare=Column(Float);
   Cabin=Column(String(50));
   Embarked=Column(String(50));

   def __repr__(self):
       return '''<titanic(PassengerId = '{0}',Survived ='{1}'Pclass='{2}],Name='{3}',Sex='{4}',Age='{5}',SibSp='{6}',
       Parch='{7}],Ticket='{8}',Fare='{9}',Cabin='{10}',Embarked='{11}')>'''.format(self.PassengerId,
       self.Survived,self.Pclass,self.Name,self.Sex,self.Age,self.SibSp,self.Parch,self.Ticket,self.Fare,self.Cabin,self.Embarked)



Base.metadata.create_all(engine)
'''

file = 'train.csv'
df = pandas.read_csv(file)
df.to_sql(con=engine,name=Titanic.__tablename__,if_exists='append',index=False)
'''
session = sessionmaker()
session.configure(bind=engine)
s = session()

result = s.query(Titanic).limit(10).all()
for r in result:
      print(r)











