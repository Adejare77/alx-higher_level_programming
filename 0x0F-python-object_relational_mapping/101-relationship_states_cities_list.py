#!/usr/bin/python3
"""lists all State objects, and corresponding City objects,
contained in the database 'hbtn_0e_101_usa'
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(engine)()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'    {city.id}: {city.name}')

    session.close()
