# Python Object-Relational Mapping (ORM)

## Overview
This repository contains scripts that demonstrate the integration of Python with a MySQL database using both direct queries and SQLAlchemy ORM.

## Technologies
- Python 3.8.5
- MySQL 8.0
- SQLAlchemy 1.4.x
- MySQLdb 2.0.x
- Ubuntu 20.04 LTS

## Setup and Installation
1. Ensure Python 3.8 and MySQL 8.0 are installed on your system.
2. Install the required Python packages:
   ```bash
   $ sudo apt-get install python3.8-venv python3-dev libmysqlclient-dev zlib1g-dev
   $ python3 -m venv venv
   $ source venv/bin/activate
   $ pip install mysqlclient SQLAlchemy
   ```

## Project Files
- `0-select_states.py`: Script to list all states from the database.
- `1-filter_states.py`: Script to filter states with names starting with 'N'.
- `2-my_filter_states.py`: Script to filter states by user input.
- `3-my_safe_filter_states.py`: Improved script to filter states by user input, safe from SQL injections.
- `4-cities_by_state.py`: Script to list all cities by state.
- `5-filter_cities.py`: Script to list all cities of a given state.
- `model_state.py`: Contains the class definition of a State.
- `6-model_state.py`: Script to link a class to a table in the database.
- `7-model_state_fetch_all.py`: Script to list all State objects from the database.
- `8-model_state_fetch_first.py`: Script to display the first State object from the database.
- `9-model_state_filter_a.py`: Script to list all State objects that contain the letter 'a'.
- `10-model_state_my_get.py`: Script to display the State object with a name passed as an argument.
- `11-model_state_insert.py`: Script to add a new State named "Louisiana".
- `12-model_state_update_id_2.py`: Script to change the name of the State with id=2 to "New Mexico".
- `13-model_state_delete_a.py`: Script to delete all State objects with a name containing the letter 'a'.
- `model_city.py`: Contains the class definition of a City.
- `14-model_city_fetch_by_state.py`: Script to print all City objects from the database by state.

## Features
- Connection to MySQL database using MySQLdb and SQLAlchemy.
- Use of Python to manage database operations.
- ORM mapping with SQLAlchemy to simplify database interactions.

## Author
- Getayawkal Wondimagegnehu