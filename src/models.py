import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum 

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    ID = Column(Integer, primary_key=True)
    username = Column(String(30))
    firstname = Column(String(30))
    lastname = Column(String(30))
    email = Column(String(50), unique=True)

class Post(Base):
    __tablename__ = "post"
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user_relationship = relationship(User)

class Comment(Base):
    __tablename__ = "comment"
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(100))
    author_id = Column(Integer, ForeignKey("user.id"))
    user_relationship = relationship(User)
    post_id = Column(Integer, ForeignKey("post.id"))
    post_relationship = relationship(Post)

class Media(Base):
    __tablename__ = "media"
    ID = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String(100))
    post_id = Column(Integer, ForeignKey("post.id"))
    user_relationship = relationship(Post)

class Follower(Base):
    __tablename__ = "follower"
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))
    user_relationship = relationship(User)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
