#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = num_printed = 0
    while True:
        try:
            if index < x:
                print("{:d}".format(my_list[index]), end='')
                index += 1
                num_printed += 1
            else:
                print()
                return num_printed
        except (ValueError, TypeError):
            index += 1
