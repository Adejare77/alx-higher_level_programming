#!/usr/bin/python3
""" Writes a Python file similar to model_state.py named model_city.py
that contains the class definition of a 'City'
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Class Definition of City"""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    # the table 'states' that contains the primary key 'id'
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
