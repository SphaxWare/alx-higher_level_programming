#!/usr/bin/python3
"""
Script that lists all State objects
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # creating an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Creating a Session class using sessionmaker
    Session = sessionmaker(bind=engine)
    # Creating an instance of the Session class
    session = Session()
    Base.metadata.create_all(engine)
    # Create a new State object
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
