#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Function that replace an element of a list

    Args:
        my_list: The list of elements
        idx: The index of the element to be replaced
        element: The element that will replace

    Returns:
        The return value. None
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
