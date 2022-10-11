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
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except IndexError as ie:
            raise
        except Exception as e:
            pass
    print('')
    return count
