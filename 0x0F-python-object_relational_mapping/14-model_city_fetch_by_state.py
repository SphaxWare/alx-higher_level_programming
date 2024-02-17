#!/usr/bin/python3
"""
Script that prints all City objects from the database
"""
from model_city import Base, City
from model_state import State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Creating an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Creating a Session class using sessionmaker
    Session = sessionmaker(bind=engine)

    # Creating an instance of the Session class
    session = Session()

    # Querying and printing all City objects from the database
    cities = (
        session.query(State.name, City.id, City.name)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )

    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))

    # Closing the session
    session.close()
