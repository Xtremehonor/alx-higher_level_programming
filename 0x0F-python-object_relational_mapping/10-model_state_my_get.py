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
        usr, pss, db, city = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

        # Connect to MySQL server running on localhost at port 3306
        engine = create_engine(f"mysql://{usr}:{pss}@localhost:3306/{db}")

        # Create a connection
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and print the first state

        City_name = session.query(State).filter_by(name=city).first()

        if City_name:
            print(City_name.id)
        else:
            print("Not found")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection
        if session:
            session.close()
