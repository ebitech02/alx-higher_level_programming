#!/usr/bin/python3
"""
a scripts that list State objects that contain the letter
'a' from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    s = '%a%'
    states = session.query(State).filter(State.name.like(s)).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
