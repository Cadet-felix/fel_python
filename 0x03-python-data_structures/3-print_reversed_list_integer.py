#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Function that prints all integer of a list

    Args:
        my_list: The list of integers

    Return:
        Return value. integers of list
    """
    if my_list:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
