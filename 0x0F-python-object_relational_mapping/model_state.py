#!/usr/bin/python3
"""Creates a Table Model Called 'state'"""

from sys import argv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Base class definition of a State"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
