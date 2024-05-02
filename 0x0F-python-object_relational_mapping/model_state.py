#!/usr/bin/python3
"""
This script connects to a MySQL server, defines a State class,
creates the necessary table, and then closes the connection.
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class represents a table 'states' in the MySQL database."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":

    try:
        # Extract command line arguments
        usr, pss, db = sys.argv[1], sys.argv[2], sys.argv[3]

        # Connect to MySQL server running on localhost at port 3306
        engine = create_engine(f"mysql://{usr}:{pss}@localhost:3306/{db}")

        # Create a connection
        connection = engine.connect()

        # Create tables if they do not exist
        Base.metadata.create_all(engine)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the connection
        if connection:
            connection.close()
