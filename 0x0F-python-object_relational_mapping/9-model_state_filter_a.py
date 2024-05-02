#!/usr/bin/python3
"""
What this script does
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    try:
        # Extract command line arguments
        usr, pss, db = sys.argv[1], sys.argv[2], sys.argv[3]

        # Connect to MySQL server running on localhost at port 3306
        engine = create_engine(f"mysql://{usr}:{pss}@localhost:3306/{db}")

        # Create a connection
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and print the first state

        with_a = session.query(State).filter(State.name.contains('a%'))
        order_by = with_a.order_by(State.id.asc()).all()
        if with_a:
            for state in order_by:
                print(state.id, state.name, sep=": ")
        else:
            print("Nothing")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection
        if session:
            session.close()
