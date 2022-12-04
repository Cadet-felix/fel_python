#!/usr/bin/python3

def element_at(my_list, idx):
    """Function that retrieves an element from a list

    Args:
        my_list: The list of elements
        idex: The element to retrieve

    Returns:
        The return value. None
    """

    if idx < 0 or idx >= len(my_list):
        return
    return my_list[idx]
