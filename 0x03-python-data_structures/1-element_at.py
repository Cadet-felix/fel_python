#!/usr/bin/pyton3

def element_at(my_list, idx):
    """Function that retrieves an element from a list

    Args:
        my_list: The list of elements
        idex: The element to retrieve

    Returns:
        The return value. None
    """
    num = len(my_list) - 1
    if idx < 0:
        return
    elif idx > num:
        return
    else:
        return my_list[idx]
