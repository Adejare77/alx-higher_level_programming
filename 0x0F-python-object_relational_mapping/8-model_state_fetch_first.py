#!/usr/bin/python3
"""prints the first 'State' object from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3360/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = sessionmaker(engine)()

    row = session.query(State).limit(1).all()

    for row in row:
        print(f'{row.id}: {row.name}')

    if not row:
        print('Nothing')

    session.close()
