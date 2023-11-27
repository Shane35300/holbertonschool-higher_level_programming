#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create the connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], "", sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects and print the results
    states = session.query(State).order_by(State.id).all()
    trap = 0
    for state in states:
        trap += 1
        if trap == 1:
            print("{}: {}".format(state.id, state.name))
    if trap == 0:
        print("Nothing")

    # Close the session
    session.close()
