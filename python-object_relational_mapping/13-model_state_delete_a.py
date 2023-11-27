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

    # Recherchez tous les record contenant la lettre "a"
    search_a = session.query(State).filter(State.name.like('%a%')).all()

    # Vérifiez si l'objet existe
    if search_a:
        # supprimer chaque record
        for record in search_a:
            session.delete(record)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
