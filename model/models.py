from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from persistence.database import Base

class Dog(Base):
    __tablename__ = 'dog'
    id = Column(Integer, primary_key=True)
    fname = Column(String(50), unique=False)
    age = Column(Integer, unique=False)
    weight = Column(Integer, unique=False)
    breeder_id = Column(Integer, ForeignKey("breeder.id"))


    breeder = relationship("Breeder")

    def __init__(self, fname=None,age=0,weight=0):
        self.fname = fname
        self.age = age
        self.weight = weight

    def __repr__(self):
        return '<Dog id = %d,name = %r,age= %d weight= %d breeder=%r>' % (self.id,self.fname,self.age,self.weight,self.breeder.fname)

class Breeder(Base):
    __tablename__ = 'breeder'
    id = Column(Integer, primary_key=True)
    fname = Column(String(50), unique=False)

    def __init__(self, fname=None):
        self.fname = fname

    def __repr__(self):
        return '<Breeder id = %d name=%r>' % (self.id,self.fname)