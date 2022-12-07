#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """function that replaces all occurrences of an element by another

    Args:
        my_list: Initial list
        search: The element to replace in the list
        replace: The new element 

    Returns:
        the return value. New list
    """
    new_list = my_list.copy()

    for k in range(0, len(new_list)):
        if new_list[k] == search:
            new_list[k] = replace
        
        return new_list
