#!/usr/bin/python3


from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':

    try:
        usr, pss, db = sys.argv[1], sys.argv[2], sys.argv[3]

        engine = create_engine(f"mysql://{usr}:{pss}@localhost:3306/{db}")
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        print(new_state.id)

    except Exception as e:
        print("An error occured", e)
    finally:
        if session:
            session.close()
