#!/usr/bin/python3
def element_at(my_list, idx):
    str_len = len(my_list)
    if idx > str_len and idx < 0:
        return None
    else:
        return my_list[idx]
