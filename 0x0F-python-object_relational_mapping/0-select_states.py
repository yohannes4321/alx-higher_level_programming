#!/usr/bin/python3
from sqlalchemy import create_engine,Column,CHAR,String,asc,Integer,or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username="john"
password='1111'
database="hbtn_0e_0_usa"

engine=create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")
Session=sessionmaker(bind=engine)

session=Session()
Base=declarative_base()
class states(Base):
    __tablename__='states'
    id=Column(Integer,primary_key=True)
    name=Column(String(256))

students=session.query(states).order_by(asc(states.id)).all()
for s in students:
    print(s.id,s.name)