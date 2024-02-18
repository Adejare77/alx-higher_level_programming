#!/usr/bin/python3
"""lists all City objects from the database 'hbtn_0e_101_usa'"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = sessionmaker(engine)()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(city.id, city.name, sep=': ', end="")
        state = city.state
        print(' ->', state.name)

    session.close()
