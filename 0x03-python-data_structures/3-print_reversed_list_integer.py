def print_reversed_list_integer(my_list=[]):
    j = -1
    for i in my_list:
        print("{:d}".format(my_list[j]))
        j -= 1
