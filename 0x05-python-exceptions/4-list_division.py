#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ function that divides element by element 2 lists

    Args:
        my_list_1: first list
        my_list_2: second list

    Return:
        the division of the lists
    """
    if (my_list_1 or my_list_2):
        new_list = []
        for i in range(list_length):
            try:
                c = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                c = "{:d}".format(0)
            except IndexError:
                print("out of range")
                c = "{:d}".format(0)
            except TypeError:
                print("wrong type")
                c = "{:d}".format(0)
            except Exception:
                c = "{:d}".format(0)
            finally:
                new_list.append(c)
        return new_list
