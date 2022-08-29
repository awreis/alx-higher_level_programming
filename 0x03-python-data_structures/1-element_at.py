#!/usr/bin/python3
def element_at(my_list, idx):
    for i in element_at(my_list, idx):
        if idx < 1:
            return None
        if idx > len(my_list):
            return None
