#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    new_list = set(my_list)

    for elem in range(len(new_list)):
        result += new_list[elem]

    return result
