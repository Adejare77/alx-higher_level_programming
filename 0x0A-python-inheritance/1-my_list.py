#!/usr/bin/python3
""" Inherinting from the class "list" """


class MyList(list):
    """ child MyList inheriting from the parent list """

    def print_sorted(self):
        """ print the list in ascending order """
        print(sorted(self))
