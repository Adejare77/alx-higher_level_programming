#!/usr/bin/python3
""" Deletes an item """

def delete_at(my_list=[], idx=0):
    """ function deletes item as specific position
        in a list

        Args:
            my_list: list to go through
            idx: position of the item to delete
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return my_list
    my_list.remove(my_list[idx])
    return my_list
