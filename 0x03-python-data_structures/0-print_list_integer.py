#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """My print all integer function

    Args:
        my_list: the list to add the integer

    Returns:
        The integers
    """
    for i in my_list:
        print("{:d}".format(i))
