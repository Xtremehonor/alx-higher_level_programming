#!/usr/bin/python3/
"""
This module prints first and Last name
"""
def say_my_name(first_name, last_name=""):
    """
    say_my_name: gets first and last name and prints
    """
    if not isinstance(first_name, str) :
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))


if __name__ == ("__main__"):

    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)