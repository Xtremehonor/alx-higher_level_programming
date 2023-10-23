#!usr/bin/python3
def safe_print_list(my_list=[], x=0):

    y = 0

    while True:
        try:
            if y < x:
                print(my_list[y], end='')
                y += 1
            else:
                print()
                return y
        except IndexError:
            print()
            return y
