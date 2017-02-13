from sqlalchemy import Column, Integer, String
from libs import encrypt
from database import Base

#Create User Schema
class User(Base) :
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    email = Column(String(320))
    pwd = Column(String(64))
    def __init__(self, name, email, pwd) :
        self.name = name
        self.email = email
        self.pwd = encrypt.hash(pwd)
    def __repr__(self) :
        return "<User({}, {}, {}, {})>"%(id, name, email, pwd)
