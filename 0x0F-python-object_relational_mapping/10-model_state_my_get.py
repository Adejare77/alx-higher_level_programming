#!/usr/bin/python3
"""prints the State object with the name passed as argument
from the database 'hbtn_0e_6_usa'
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(engine)()

    rows = session.query(State).filter(State.name == '{}'.format(
        argv[4])).all()

    for row in rows:
        print(row.id)
    if not rows:
        print('Not found')

    session.close()
