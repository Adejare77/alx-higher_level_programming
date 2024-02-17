#!/usr/bin/python3
""" Writes a Python file similar to model_state.py named model_city.py
that contains the class definition of a 'City'
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = sessionmaker(engine)()

    data = session.query(City.name.label('city_name'),
                         City.id,
                         State.name.label('states_name'),
                         ).join(City).order_by(City.id.asc()).all()

    for row in data:
        print(f'{row.states_name}: ({row.id}) {row.city_name}')
