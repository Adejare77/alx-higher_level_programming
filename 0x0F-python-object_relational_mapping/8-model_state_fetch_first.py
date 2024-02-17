#!/usr/bin/python3
"""prints the first 'State' object from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3360/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = sessionmaker(engine)()

    rows = session.query(State).filter_by(id=1).all()

    for row in rows:
        print(f'{row.id}: {row.name}')

    session.close()
