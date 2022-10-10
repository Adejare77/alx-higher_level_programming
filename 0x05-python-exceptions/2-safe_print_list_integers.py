#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ function that prints the first x element
        of a list and only integers

        Args:
            my_list: contains any type of data type
            x: number of elements to access in my_list

        Returns:
            real number
    """
    count = 0
    if my_list != []:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except IndexError as idx:
                print("IndexError:", idx)
            except Exception:
                pass
        print('')
        return count
