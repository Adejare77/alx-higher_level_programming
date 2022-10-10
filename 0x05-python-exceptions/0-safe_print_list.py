#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ prints x elements of a list

        Args:
            my_list: list that contains the element to be printed
            x: number of elements to print

        Return: real number of elements printed
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except Exception as e:
            continue
    print("")
    return count
