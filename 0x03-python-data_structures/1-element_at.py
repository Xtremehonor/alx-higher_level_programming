#!/usr/bin/python3
def element_at(my_list, idx):
    str_len = len(my_list)
    if  idx < 0 or idx > str_len:
        return None
    else:
        return my_list[idx]
