#!/usr/bin/python3
def element_at(my_list, idx):
    str_len = 0
    for i in my_list:
        str_len += 1

    if  idx < 0 or idx > str_len:
        return None
    else:
        return my_list[idx]
