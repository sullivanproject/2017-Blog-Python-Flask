#-*- coding: utf-8 -*-
import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from database import Base

#Create Article Schema
class Article(Base) :
    #Set Table Name and Columns.
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    body = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, title, body, writer, tags) :
        self.title = title
        self.body = body
        self.writer = writer
    def __repr__(self) :
        return "<Article({}, {}, {})>"%(self.id, self.title, self.body)
