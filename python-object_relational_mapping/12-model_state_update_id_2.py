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

    # Recherchez l'objet State où id = 2
    search_id_2 = session.query(State).filter_by(id=2).first()

    # Vérifiez si l'objet existe
    if search_id_2:
        # Modifiez le nom de l'objet State
        search_id_2.name = "New Mexico"

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
