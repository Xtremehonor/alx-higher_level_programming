#!/usr/bin/python3
'''
a script that lists all State objects
from the database hbtn_0e_6_usa
'''
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    update = session.query(State).filter_by(id=2).first()
    update.name = "New Mexico"
    session.commit()
    session.close()
