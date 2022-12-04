#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Function that replaces an element in a list

    Args:
        my-list: The list whose an element is replaced
        idx: The index of element to be replaced
        element: The element that will replace

    Returns:
        The return value. list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list

