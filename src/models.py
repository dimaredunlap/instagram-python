import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    mediatype = Column(Enum)
    url = Column(String)
    post = relationship(Post)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    post = relationship(Post)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')