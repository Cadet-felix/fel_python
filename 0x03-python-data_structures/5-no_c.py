#!/usr/bin/python3

def no_c(my_string):
    """Function that removes all charaters of c and C from a string

    Args:
        my_string: string to modify

    Returns:
        The return value. new string
    """
    new_s = my_string.translate({ord('c'): None})
    new_s = new_s.translate({ord('C'): None})
    return new_s
