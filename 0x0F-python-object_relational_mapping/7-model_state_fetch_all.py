#!/usr/bin/python3
"""
What this script does
"""
from sqlalchemy import create_engine
from model_state import Base, State
import sys


if __name__ == "__main__":
    try:
        # Extract command line arguments
        usr, pss, db = sys.argv[1], sys.argv[2], sys.argv[3]

        # Connect to MySQL server running on localhost at port 3306
        engine = create_engine(f"mysql://{usr}:{pss}@localhost:3306/{db}")

        # Create a connection
        connection = engine.connect()

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection
        if connection:
            connection.close()
