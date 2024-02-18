#!/usr/bin/python3
"""Creates the State 'California' with the City 'San Francisco'
from the database 'hbtn_0e_100_usa
"""

from sys import argv
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)
    session = sessionmaker(bind=engine)()

    new_object = [
        State(name='California'),
        City(name='San Francisco')
    ]

    new_object[0].cities.append(new_object[1])
    session.add_all(new_object)
    session.commit()

    session.close()
