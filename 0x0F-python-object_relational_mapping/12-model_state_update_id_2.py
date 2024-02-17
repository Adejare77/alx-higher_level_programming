#!/usr/bin/python3
"""Changes the name of a State object from the
database 'hbtn_0e_6_usa'
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(engine)()

    # update_id_2 = session.query(State).filter_by(id = 2).first()
    # update_id_2.name = 'Paper'
    update_id_2 = session.query(State).filter_by(
        id=2).update({'name': 'New Mexico'})

    session.commit()
    session.close()
